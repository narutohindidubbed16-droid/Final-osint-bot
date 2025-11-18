import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "123456"))

# CHANNELS
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "@YourMainChannel")
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "@YourBackupChannel")
PRIVATE_CHANNEL = os.getenv("PRIVATE_CHANNEL", "https://t.me/YourPrivateChannel")  # 🔥 No check join

# API LINKS
API_MOBILE = "https://ph-ng-pi.vercel.app/?number="
API_PINCODE = "https://pincode-ng.vercel.app/lookup?pincode="
API_VEHICLE = "https://vvvin-ng.vercel.app/lookup?rc="
API_IMEI = "https://ng-imei-info.vercel.app/?imei_num="
API_GST = "https://api-v1.bsite.net/gst?id="
API_IFSC = "https://ifsc.razorpay.com/"
