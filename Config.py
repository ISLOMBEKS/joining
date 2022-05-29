import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 123456)
  API_HASH = os.environ.get("API_HASH", "")
  # Sudo users( goto @JVToolsBot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1204927413 1405957830").split()))
  SUDO_USERS.append(1204927413)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Men guruhda sizning kanalingizga azo bo'lmagan odamlarni azo bo'lmagunlaricha yozdirmayman, azo bo'lganidan keyin ular ✅ Tekshirish tugmasini bosishlari kerak",
        
        "**Meni faqat guruh yaratuvchisi boshqara oladi",
        
        "**Commmands**\n__/ForceSubscribe - Ulangan kanalni tekshirish.\n/ForceSubscribe off - Kanalni o'chirish.\n/ForceSubscribe {username yoki kanal ID} - Kanal ulash.\n/ForceSubscribe clear - Barchadan muteni olish.__"
        
            ]
      SC_MSG = ""

      START_MSG = ["**👋Salom [{}](tg://user?id={})**\n__Men kanalingizda azo bo'lmagan odamlarni guruhingizda yozdirmayman.",

                   "**Men guruhda sizning kanalingizga azo bo'lmagan odamlarni azo bo'lmagunlaricha yozdirmayman, azo bo'lganidan keyin ular ✅ Tekshirish tugmasini bosishlari kerak",
        
                   "**Meni faqat guruh yaratuvchisi boshqara oladi",
        
                   "**Commmands**\n__/ForceSubscribe - Ulangan kanalni tekshirish.\n/ForceSubscribe off - Kanalni o'chirish.\n/ForceSubscribe {username yoki kanal ID} - Kanal ulash.\n/ForceSubscribe clear - Barchadan muteni olish.__"]
