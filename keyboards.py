from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import MAIN_CHANNEL, BACKUP_CHANNEL, PRIVATE_CHANNEL

def join_channels_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Join Main Channel", url=f"https://t.me/{MAIN_CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("🛡 Join Backup Channel", url=f"https://t.me/{BACKUP_CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("🔐 Private Channel", url=PRIVATE_CHANNEL)],   # ❌ No join check
        [InlineKeyboardButton("✅ I Have Joined", callback_data="verify")]
    ])

def main_menu_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📱 Mobile Lookup", callback_data="mobile"),
         InlineKeyboardButton("🏢 GST Lookup", callback_data="gst")],
        [InlineKeyboardButton("🏦 IFSC", callback_data="ifsc"),
         InlineKeyboardButton("📦 Pincode", callback_data="pincode")],
        [InlineKeyboardButton("🚗 Vehicle Lookup", callback_data="vehicle")],
        [InlineKeyboardButton("📘 Help Guide", callback_data="help")]
    ])
