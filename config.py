# ===========================
# ⚙️ CONFIGURATION FILE
# ===========================

import os
from dotenv import load_dotenv
load_dotenv()

# Bot Identity
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "NaGIOsintProBot")

# Channel Enforcement (Only MAIN channel check)
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "@AbdulBotz")

# Backup (no check, only display)
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "@darknagibackup")
PRIVATE_INVITE = os.getenv("PRIVATE_INVITE", "https://t.me/+hyVTTQkfJS41NTFl")

# Credits
START_CREDITS = 10

# APIs
MOBILE_API = "https://ph-ng-pi.vercel.app/?number="
PINCODE_API = "https://pincode-ng.vercel.app/lookup?pincode="
RC_API = "https://vvvin-ng.vercel.app/lookup?rc="
IMEI_API = "https://ng-imei-info.vercel.app/?imei_num="

# Coming Soon
GST_API = ""
IFSC_API = ""

COMING_SOON_LIST = [
    "Aadhaar Lookup",
    "PAN Lookup",
    "Passport Lookup",
    "Email OSINT",
    "Voter ID Lookup"
]
