class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6977793872"
    sudo_users = "7053677913", "1732582235", "6977793872"
    GROUP_ID = -1002452053306,
    TOKEN = "7882935920:AAE5mwgEExPP00Tw5xe_o4Al4FoBYE2np6g"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Get_waifu_character_bot"
    UPDATE_CHAT = "Get_waifu_character_bot"
    BOT_USERNAME = "Get_waifu_character_bot"
    CHARA_CHANNEL_ID = "-1002452053306"
    api_id = 28735016
    api_hash = "395761ed41e18de91ee4e18ff99afc81"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
