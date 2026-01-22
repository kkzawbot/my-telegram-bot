import telebot
from telebot import types

# --- Configuration ---
API_TOKEN = '8377346830:AAGVWfasXHc2AP3Q_z8VyT3WG0GyBer6Sh0'
bot = telebot.TeleBot(API_TOKEN)

# --- Helper function for Main Menu ---
def main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်ရန်", callback_data="movies_main")
    btn2 = types.InlineKeyboardButton("📱 Mod APK များ", url="https://t.me/khantzipmodapk")
    btn3 = types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses")
    btn4 = types.InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data="trusted_sellers")
    btn5 = types.InlineKeyboardButton("💎 Pro/Premium များ", callback_data="premium_info")
    btn6 = types.InlineKeyboardButton("📦 တခြားဝယ်ယူနိုင်သောအရာများ", callback_data="others")
    btn7 = types.InlineKeyboardButton("⭐ Rating ပေးရန်", url="https://t.me/khantziprating")
    btn8 = types.InlineKeyboardButton("🤵 Admin နဲ့စကားပြောမယ်", url="https://t.me/khantzip")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup.add(btn7)
    markup.add(btn8)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.first_name
    welcome_text = (
        f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {username} ခင်ဗျာ။\n\n"
        "Khantzip bot ကနေ ကြိုဆိုပါတယ် ✨\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # --- ဇာတ်ကားကြည့်ရန် ---
    if call.data == "movies_main":
        markup = types.InlineKeyboardMarkup(row_width=1)
        m_links = [
            ("📺 ဇာတ်ကားအစုံအဓိက channel", "https://t.me/khantzipmainmovie"),
            ("🇨🇳 တရုတ်ဇာတ်ကား", "https://t.me/khantzipchinamovies"),
            ("🇰🇷 ကိုရီးယားဇာတ်ကား", "https://t.me/khantzipkoreamovies"),
            ("🇮🇳 အိန္ဒိယဇာတ်ကား", "https://t.me/khanzipindiamovie"),
            ("🇹🇭 ထိုင်းဇာတ်ကား", "https://t.me/khantzipthaimovie"),
            ("🎨 Anime,cartoon,animation", "https://t.me/khantzipmovie"),
            ("🌍 နိုင်ငံခြားဇာတ်လမ်း", "https://t.me/khantzipmovies")
        ]
        for name, url in m_links:
            markup.add(types.InlineKeyboardButton(name, url=url))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("ကြည့်ရှုလိုသော Channel ကို ရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- သင်တန်းများ ---
    elif call.data == "courses":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("💎 Mlbb diamondရောင်းနည်း", callback_data="price_10000"),
            types.InlineKeyboardButton("Facebook account သစ်ဖွင့်နည်း", callback_data="price_10000"),
            types.InlineKeyboardButton("Tiktok Japan accountဖွင့်နည်း", callback_data="price_10000"),
            types.InlineKeyboardButton("Gmail new accountနှင့် နိုင်ငံချိန်းနည်း", callback_data="price_20000"),
            types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        )
        bot.edit_message_text("khantzipမှ လောလောဆယ်ရရှိသောသင်တန်းများ\nသင်တန်းဈေးနှုန်းသိချင်ရင်သိချင်‌သောသင်တန်းကိုထပ်နှိပ်ကြည့်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "price_10000":
        bot.send_message(call.message.chat.id, "သင်တန်းကြေး - 10000ks\n\nAdmin 👉 @khantzip")
    elif call.data == "price_20000":
        bot.send_message(call.message.chat.id, "သင်တန်းကြေး - 20000ks\n\nAdmin 👉 @khantzip")

    # --- ယုံကြည်ရသူများ ---
    elif call.data == "trusted_sellers":
        text = "လူအများအလိမ်မခံရအောင် ကျွန်တော်သိတဲ့သူများကိုညွှန်းပေးထားပါတယ် နောက်ထပ်ယုံကြည်စိတ်ချရသူများလည်း လာရောက်အပ်နှံနိုင်ပါတယ်"
        markup = types.InlineKeyboardMarkup(row_width=1)
        trust_btns = [
            ("ရန်ကုန်အဝေးပြေးလက်မှတ်", "https://t.me/khantzip"), ("Mlbb diamond reseller gp", "https://t.me/khantzip"),
            ("ဖုန်းMB, ဖုန်းပြောမိနစ်", "https://t.me/khantzip"), ("Atomwifiကဒ် reseller gp", "https://t.me/khantzip"),
            ("Tiktok(JP)အကောင့်အရောင်းအဝယ်", "https://t.me/khantzip"), ("ဗေဒင်ဆရာ", "https://t.me/khantzip"),
            ("အကျိုးရှိသော သင်တန်းများ", "https://t.me/khantzip")
        ]
        for name, url in trust_btns:
            markup.add(types.InlineKeyboardButton(name, url=url))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- Pro/Premium ---
    elif call.data == "premium_info":
        markup = types.InlineKeyboardMarkup(row_width=2)
        p_btns = [
            ("Canva Edu", "prem_canva"), ("Capcut", "prem_capcut"),
            ("Alightmotion", "prem_alight"), ("Wink", "prem_wink"),
            ("Inshot", "prem_inshot"), ("Express vpn", "prem_vpn")
        ]
        for name, callback in p_btns:
            markup.add(types.InlineKeyboardButton(name, callback_data=callback))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("ရရှိနိုင်သော Premium ဝန်ဆောင်မှုများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- တခြားဝယ်ယူရန် ---
    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=2)
        o_btns = [
            ("MLBB Diamond", "mlbb_servers"), ("Facebook account", "oth_fb"),
            ("Mbccs", "oth_mbccs"), ("Gmail account", "oth_gmail"),
            ("Real Email", "oth_realmail"), ("Outlook/Hotmail", "oth_outlook"),
            ("PUBG", "oth_pubg"), ("Magic chess", "oth_magic")
        ]
        for name, callback in o_btns:
            markup.add(types.InlineKeyboardButton(name, callback_data=callback))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("တခြားဝယ်ယူနိုင်သော အမျိုးအစားများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- MLBB Servers ---
    elif call.data == "mlbb_servers":
        markup = types.InlineKeyboardMarkup(row_width=1)
        servers = [
            ("Normal sever 🇲🇲", "ml_mm"), ("Indonesia sever", "ml_indo"),
            ("Russia sever", "ml_ru"), ("Malaysia & Singapore sever", "ml_mysg"),
            ("Philippines", "ml_ph")
        ]
        for name, data in servers:
            markup.add(types.InlineKeyboardButton(name, callback_data=data))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="others"))
        bot.edit_message_text("Server ကိုရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- MLBB Prices (MM Server - Example of Formatting) ---
    elif call.data == "ml_mm":
        price_list = (
            "MLBB Normal sever (🇲🇲)\n"
            "weekly pass ➡️ 5700Ks\n50+50 ➡️ 3100Ks\n150+150 ➡️ 10000Ks\n250+250 ➡️ 16000Ks\n500+500 ➡️ 31000Ks\n\n"
            "3 ➡️ 500Ks\n5 ➡️ 700Ks\n11 ➡️ 1000Ks\n22 ➡️ 2000Ks\n33 ➡️ 2800Ks\n44 ➡️ 3600Ks\n55 ➡️ 4000Ks\n"
            "86 ➡️ 5500Ks\n110 ➡️ 7000Ks\n172 ➡️ 11000Ks\n257 ➡️ 15000Ks\n343 ➡️ 20000Ks\n429 ➡️ 25000Ks\n"
            "514 ➡️ 30000Ks\n600 ➡️ 35000Ks\n706 ➡️ 40000Ks\n878 ➡️ 50000Ks\n963 ➡️ 55000Ks\n"
            "1049 ➡️ 60000Ks\n1135 ➡️ 65000Ks\n1412 ➡️ 80000Ks\n2195 ➡️ 120000Ks\n3688 ➡️ 200000Ks\n"
            "5532 ➡️ 300000Ks\n9288 ➡️ 480000Ks\n\nAdmin 👉 @khantzip"
        )
        bot.edit_message_text(price_list, call.message.chat.id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 Back", callback_data="mlbb_servers")))

    # --- Back Home ---
    elif call.data == "back_home":
        username = call.from_user.first_name
        welcome_text = f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {username} ခင်ဗျာ။\n\nKhantzip bot ကနေ ကြိုဆိုပါတယ် ✨\nကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
        bot.edit_message_text(welcome_text, call.message.chat.id, call.message.message_id, reply_markup=main_menu_markup())

bot.polling()
