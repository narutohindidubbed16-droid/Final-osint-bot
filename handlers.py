import aiohttp
from telegram import Update
from telegram.ext import ContextTypes
from config import (
    MAIN_CHANNEL, BACKUP_CHANNEL,
    API_MOBILE, API_PINCODE, API_VEHICLE,
    API_IMEI, API_GST, API_IFSC
)
from keyboards import join_channels_kb, main_menu_kb


# ------------------ CHANNEL CHECK ------------------
async def check_join(bot, user_id):
    try:
        a = await bot.get_chat_member(MAIN_CHANNEL, user_id)
        b = await bot.get_chat_member(BACKUP_CHANNEL, user_id)
        return a.status in ["member", "administrator", "creator"] \
           and b.status in ["member", "administrator", "creator"]
    except:
        return False


# ------------------ START ------------------
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if not await check_join(ctx.bot, user.id):
        await update.message.reply_text("🔐 Join required channels:", reply_markup=join_channels_kb())
        return

    await update.message.reply_text("🔥 Welcome to Nagi OSINT PRO\nChoose an option:", reply_markup=main_menu_kb())


# ------------------ VERIFY JOIN BUTTON ------------------
async def verify(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if await check_join(ctx.bot, q.from_user.id):
        await q.message.reply_text("✅ Verified!", reply_markup=main_menu_kb())
    else:
        await q.message.reply_text("❌ Join both channels!", reply_markup=join_channels_kb())


# ------------------ BUTTON HANDLER ------------------
async def menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    d = q.data
    await q.answer()

    ctx.user_data["mode"] = d
    await q.message.reply_text("✍️ Send Input:")


# ------------------ PROCESS INPUT ------------------
async def process(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if "mode" not in ctx.user_data:
        return

    mode = ctx.user_data["mode"]
    text = update.message.text.strip()

    api_url = {
        "mobile": API_MOBILE + text,
        "pincode": API_PINCODE + text,
        "vehicle": API_VEHICLE + text,
        "imei": API_IMEI + text,
        "gst": API_GST + text,
        "ifsc": API_IFSC + text
    }.get(mode)

    await update.message.reply_text("⏳ Fetching data...")

    async with aiohttp.ClientSession() as s:
        try:
            r = await s.get(api_url)
            js = await r.json(content_type=None)
        except:
            await update.message.reply_text("⚠️ API Error.")
            return

    await update.message.reply_text(f"📄 *Result:*\n```{js}```", parse_mode="Markdown")
