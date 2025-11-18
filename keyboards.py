# ===============================================
# 📌 keyboards.py — All Buttons & Inline Keyboards
# ===============================================

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import MAIN_CHANNEL, BACKUP_CHANNEL, PRIVATE_INVITE


# ============================
# 🔐 JOIN CHANNELS KEYBOARD
# ============================
def join_channels_kb():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 Join Main Channel", url=f"https://t.me/{MAIN_CHANNEL.replace('@', '')}")
        ],
        [
            InlineKeyboardButton("🔰 Join Backup Channel", url=f"https://t.me/{BACKUP_CHANNEL.replace('@', '')}")
        ],
        [
            InlineKeyboardButton("🔐 Private Access Link", url=PRIVATE_INVITE)
        ],
        [
            InlineKeyboardButton("✅ I Have Joined", callback_data="verify_join")
        ]
    ])


# ============================
# 🏠 MAIN MENU KEYBOARD
# ============================
def main_menu_kb():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📱 Mobile Lookup", callback_data="mobile_lookup"),
            InlineKeyboardButton("🚗 RC Lookup", callback_data="rc_lookup")
        ],
        [
            InlineKeyboardButton("📦 Pincode Lookup", callback_data="pincode_lookup"),
            InlineKeyboardButton("🧾 IMEI Lookup", callback_data="imei_lookup")
        ],
        [
            InlineKeyboardButton("🏢 GST Lookup", callback_data="gst_lookup"),
            InlineKeyboardButton("🏦 IFSC Lookup", callback_data="ifsc_lookup")
        ],
        [
            InlineKeyboardButton("🎁 Refer & Earn", callback_data="refer")
        ],
        [
            InlineKeyboardButton("🚧 Coming Soon", callback_data="coming_soon")
        ]
    ])


# ============================
# ✏️ ASK INPUT KEYBOARD
# ============================
def ask_input_kb():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔙 Back", callback_data="back_home")
        ]
    ])


# ============================
# 🚧 COMING SOON MENU
# ============================
def coming_soon_kb():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔐 Aadhaar Lookup", callback_data="soon"),
            InlineKeyboardButton("🧾 PAN Lookup", callback_data="soon")
        ],
        [
            InlineKeyboardButton("🛂 Passport Lookup", callback_data="soon"),
            InlineKeyboardButton("🗳 Voter ID Lookup", callback_data="soon")
        ],
        [
            InlineKeyboardButton("📧 Email OSINT", callback_data="soon")
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="back_home")
        ]
    ])
