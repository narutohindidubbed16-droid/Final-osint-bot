# ============================================
# ⚙️ CONFIGURATION FILE (FINAL – PYROGRAM v2)
# ============================================

import os
from dotenv import load_dotenv
load_dotenv()

# ---------------------------
# 🔥 BOT SETTINGS
# ---------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "NaGIOsintProBot")

# PUBLIC CHANNEL (only this must be checked)
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "@AbdulBotz")

# PRIVATE CHANNEL (only for display)
PRIVATE_INVITE = os.getenv("PRIVATE_INVITE", "https://t.me/+hyVTTQkfJS41NTFl")

# BACKUP CHANNEL (only for display)
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "https://t.me/+mPzuc3vtf0c0ZWI9")

# STARTING USER CREDITS
START_CREDITS = 5

# ---------------------------
# 🔥 API LINKS
# ---------------------------
MOBILE_API = "https://ph-ng-pi.vercel.app/?number="
PINCODE_API = "https://pincode-ng.vercel.app/lookup?pincode="
RC_API = "https://vvvin-ng.vercel.app/lookup?rc="
IMEI_API = "https://ng-imei-info.vercel.app/?imei_num="

# Empty = Coming soon
GST_API = ""
IFSC_API = ""

# ---------------------------
# 🚀 COMING SOON FEATURES
# ---------------------------
COMING_SOON_LIST = [
    "Aadhaar Lookup",
    "PAN Lookup",
    "Voter ID Lookup",
    "Passport OSINT",
    "Email OSINT"
]

# ---------------------------
# 🔥 OWNER / SUPPORT
# ---------------------------
OWNER_USER = "@AbdulBotz"
