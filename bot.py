import telebot
from telebot import types

# --- Configuration ---
API_TOKEN = '8377346830:AAGVWfasXHc2AP3Q_z8VyT3WG0GyBer6Sh0'
bot = telebot.TeleBot(API_TOKEN)
ADMIN_LINK = "https://t.me/khantzip"

def main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်မယ်", callback_data="movies_main"),
        types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses"),
        types.InlineKeyboardButton("📱 Mod APK များ", url="https://t.me/khantzipmodapk"),
        types.InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data="trusted_sellers"),
        types.InlineKeyboardButton("💎 Pro/Premium များ", callback_data="premium_info"),
        types.InlineKeyboardButton("📦 တခြားရနိုင်သည်များ", callback_data="others")
    )
    markup.add(types.InlineKeyboardButton("⭐ Rating ပေးရန်", url="https://t.me/khantziprating"))
    markup.add(types.InlineKeyboardButton("🤵 Admin နဲ့စကားပြောမယ်", url=ADMIN_LINK))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    full_name = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
    welcome_text = (
        f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {full_name} ခင်ဗျာ။\n\n"
        "Khantzip bot ကနေ ကြိုဆိုပါတယ် ✨\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    full_name = f"{call.from_user.first_name} {call.from_user.last_name or ''}".strip()

    # --- Movies & Courses (Already Fine) ---
    if call.data == "movies_main":
        markup = types.InlineKeyboardMarkup(row_width=1)
        m_links = [("📺 ဇာတ်ကားအစုံအဓိက channel", "https://t.me/khantzipmainmovie"), ("🇨🇳 တရုတ်ဇာတ်ကား", "https://t.me/khantzipchinamovies"), ("🇰🇷 ကိုရီးယားဇာတ်ကား", "https://t.me/khantzipkoreamovies"), ("🇮🇳 အိန္ဒိယဇာတ်ကား", "https://t.me/khanzipindiamovie"), ("🇹🇭 ထိုင်းဇာတ်ကား", "https://t.me/khantzipthaimovie"), ("🎨 Anime,cartoon,animation", "https://t.me/khantzipmovie"), ("🌍 နိုင်ငံခြားဇာတ်လမ်း", "https://t.me/khantzipmovies")]
        for name, url in m_links: markup.add(types.InlineKeyboardButton(name, url=url))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("ကြည့်ရှုလိုသော Channel ကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    elif call.data == "courses":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("💎 Mlbb diamondရောင်းနည်း", callback_data="c_10k"), types.InlineKeyboardButton("👤 Facebook account သစ်ဖွင့်နည်း", callback_data="c_10k"), types.InlineKeyboardButton("🇯🇵 Tiktok Japan accountဖွင့်နည်း", callback_data="c_10k"), types.InlineKeyboardButton("📧 Gmail new accountနှင့် နိုင်ငံချိန်းနည်း", callback_data="c_20k"), types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("khantzipမှ လောလောဆယ်ရရှိသောသင်တန်းများ 👇", cid, mid, reply_markup=markup)

    # --- MLBB Servers & Others ---
    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=2)
        items = [("MLBB Diamond", "mlbb_servers"), ("PUBG", "pubg"), ("Magic chess", "chess"), ("Unipin br", "unipin"), ("Smile coin br", "smile"), ("Gmail account", "gmail"), ("Email account", "email"), ("Outlook/Hotmail", "outlook"), ("Facebook account", "fb"), ("Tiktok account (JP)", "tiktok"), ("Mbccs account", "mbccs"), ("Mytel mb/data", "mytel")]
        for n, d in items: markup.add(types.InlineKeyboardButton(n, callback_data=d))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("တခြားဝယ်ယူနိုင်သော အမျိုးအစားများ 👇", cid, mid, reply_markup=markup)

    elif call.data == "mlbb_servers":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🇲🇲 Normal sever", callback_data="ml_mm"), types.InlineKeyboardButton("🇮🇩 Indonesia sever", callback_data="ml_indo"), types.InlineKeyboardButton("🇲🇾🇸🇬 Malaysia/Singapore", callback_data="ml_mysg"), types.InlineKeyboardButton("🇷🇺 Russia sever", callback_data="ml_ru"), types.InlineKeyboardButton("🇵🇭 Philippines", callback_data="ml_ph"), types.InlineKeyboardButton("🔙 Back", callback_data="others"))
        bot.edit_message_text("Server ကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- Malaysia & Singapore (🇲🇾🇸🇬) ---
    elif call.data == "ml_mysg":
        text = (
            "malaysia & singapore ( 🇲🇾🇸🇬 )\n"
            "weekly pass sg  ➡️ 8600Ks\nweekly pass my  ➡️ 8500Ks\n"
            "50+50  ➡️ 4500Ks\n150+150  ➡️ 13000Ks\n250+250  ➡️ 21000Ks\n500+500  ➡️ 42000Ks\n\n"
            "14➡️1500Ks | 28➡️2500Ks | 42➡️4000Ks\n56➡️5500Ks | 70➡️7000Ks | 84➡️8500Ks\n112➡️11000Ks | 140➡️14000Ks | 154➡️16000Ks\n"
            "210➡️20000Ks | 284➡️25000Ks | 355➡️30000Ks\n429➡️35000Ks | 569➡️46000Ks | 716➡️57000Ks\n856➡️68000Ks | 898➡️73000Ks | 1000➡️82000Ks\n"
            "1084➡️89000Ks | 1145➡️95000Ks | 1284➡️110000Ks\n1446➡️130000Ks | 2162➡️180000Ks | 2976➡️230000Ks\n3692➡️285000Ks | 4422➡️335000Ks | 5952➡️440000Ks\n"
            "6012➡️450000Ks | 7502➡️550000Ks | 8948➡️660000Ks\n10478➡️760000Ks | 11924➡️870000Ks | 13454➡️960000Ks\n15004➡️1080000Ks\n\n"
            "Admin 👉 @khantzip"
        )
        bot.send_message(cid, text)

    # --- Philippines (🇵🇭) ---
    elif call.data == "ml_ph":
        text = (
            "philippines ( 🇵🇭 )\n"
            "weekly pass  ➡️ 6600Ks\n50+50  ➡️ 4100Ks\n150+150  ➡️ 11000Ks\n250+250  ➡️ 17000Ks\n500+500 ➡️  35000Ks\n\n"
            "5➡️700Ks | 11➡️1100Ks | 22➡️2000Ks\n56➡️4200Ks | 112➡️7500Ks | 223➡️15000Ks\n336➡️22000Ks | 570➡️35000Ks | 1163➡️69000Ks\n"
            "2398➡️140000Ks | 6042➡️330000Ks\n\n"
            "Admin 👉 @khantzip"
        )
        bot.send_message(cid, text)

    # --- Outlook/Hotmail & Mbccs ---
    elif call.
    
