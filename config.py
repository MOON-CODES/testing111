import os

class Config(object):
    BOT_TOKEN = os.environ.get("8062254368:AAE0Tf5lwvtpPbGb-r5hEFi3t4Kso5Tc3mE")
    API_ID = int(os.environ.get("22940312"))
    API_HASH = os.environ.get("82fb5cd2de25e4c01021b8bbae9909bb")
    AUTH_USER = os.environ.get('6818594183', '').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝐔ɴᴛᴏʟᴅ 𝐂ᴏᴅᴇʀ™"#Here You Can Change with Your Name  or any custom name or title you prefer
