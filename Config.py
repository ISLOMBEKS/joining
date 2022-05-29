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

        "**Men guruhda sizning kanalingizga azol bo'lmagan odamlarni azo bo'lmagunlaricha yozdirmayman, azo bo'lganidan keyin ular ✅ Tekshirish tugmasini bosishlari kerak",
        
        "**Meni faqat guruh yaratuvchisi boshqara oladi",
        
        "**Commmands**\n__/ForceSubscribe - Ulangan kanalni tekshirish.\n/ForceSubscribe off - Kanalni o'chirish.\n/ForceSubscribe {username yoki kanal ID} - Kanal ulash.\n/ForceSubscribe clear - Barchadan muteni olish.__",
        
       "**Devloped By @UniversalBotsUpdate**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
