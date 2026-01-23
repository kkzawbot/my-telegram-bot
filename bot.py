import telebot
from telebot import types

# --- Configuration ---
API_TOKEN = '8377346830:AAGVWfasXHc2AP3Q_z8VyT3WG0GyBer6Sh0'
bot = telebot.TeleBot(API_TOKEN)
ADMIN_LINK = "https://t.me/khantzip"

# --- Main Menu Setup ---
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    # 2 စီ တွဲထားသော ခလုတ် ၆ ခု
    btn1 = types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်မယ်", callback_data="movies")
    btn2 = types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses")
    btn3 = types.InlineKeyboardButton("📱 Mod apk", url="https://t.me/khantzipmodapk")
    btn4 = types.InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data="trusted")
    btn5 = types.InlineKeyboardButton("💎 Pro/premium များ", callback_data="premium")
    btn6 = types.InlineKeyboardButton("📦 တခြားရနိုင်သည်များ", callback_data="others")
    
    # တစ်ခုချင်းစီ ခလုတ် ၂ ခု
    btn7 = types.InlineKeyboardButton("⭐ Rating ပေးရန်", url="https://t.me/khantziprating")
    btn8 = types.InlineKeyboardButton("🤵 Admin နဲ့စကားပြောမယ်", url=ADMIN_LINK)
    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup.add(btn7)
    markup.add(btn8)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    full_name = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
    welcome_text = (
        f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {full_name} ခင်ဗျာ။\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    cid = call.message.chat.id
    mid = call.message.message_id

    # --- Movies Section ---
    if call.data == "movies":
        markup = types.InlineKeyboardMarkup(row_width=1)
        links = [
            ("📺 ဇာတ်ကားအစုံအဓိက channel", "https://t.me/khantzipmainmovie"),
            ("🇨🇳 တရုတ်ဇာတ်ကား", "https://t.me/khantzipchinamovies"),
            ("🇰🇷 ကိုရီးယားဇာတ်ကား", "https://t.me/khantzipkoreamovies"),
            ("🇮🇳 အိန္ဒိယဇာတ်ကား", "https://t.me/khanzipindiamovie"),
            ("🇹🇭 ထိုင်းဇာတ်ကား", "https://t.me/khantzipthaimovie"),
            ("🎨 Anime,cartoon,animation", "https://t.me/khantzipmovie"),
            ("🌍 နိုင်ငံခြားဇာတ်လမ်း", "https://t.me/khantzipmovies")
        ]
        for name, link in links:
            markup.add(types.InlineKeyboardButton(name, url=link))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("ကြည့်ရှုလိုသော Channel ကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- Courses Section ---
    elif call.data == "courses":
        markup = types.InlineKeyboardMarkup(row_width=1)
        c_list = [
            ("💎 Mlbb diamondရောင်းနည်း", "c_10k"),
            ("👤 Facebook account သစ်ဖွင့်နည်း", "c_10k"),
            ("🇯🇵 Tiktok Japan accountဖွင့်နည်း", "c_10k"),
            ("📧 Gmail new accountနှင့် နိုင်ငံချိန်းနည်း", "c_20k")
        ]
        for name, data in c_list:
            markup.add(types.InlineKeyboardButton(name, callback_data=data))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("khantzipမှ လောလောဆယ်ရရှိသောသင်တန်းများ\nသင်တန်းဈေးနှုန်းသိချင်ရင်သိချင်သောသင်တန်းကိုထပ်နှိပ်ကြည့်ပါ", cid, mid, reply_markup=markup)

    elif call.data in ["c_10k", "c_20k"]:
        price = "10000ks" if call.data == "c_10k" else "20000ks"
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🤵 Admin Account", url=ADMIN_LINK))
        bot.send_message(cid, f"သင်တန်းကြေး - {price}\n\nဆက်သွယ်ရန် 👇", reply_markup=markup)

    # --- Trusted Sellers ---
    elif call.data == "trusted":
        text = "လူအများအလိမ်မခံရအောင် ကျွန်တော်သိတဲ့သူများကိုညွှန်းပေးထားပါတယ် နောက်ထပ်ယုံကြည်စိတ်ချရသူများလည်း လာရောက်အပ်နှံနိုင်ပါတယ်"
        markup = types.InlineKeyboardMarkup(row_width=1)
        trust_btns = ["ရန်ကုန်အဝေးပြေးလက်မှတ်", "Mlbb diamond reseller gp", "ဖုန်းMB, ဖုန်းပြောမိနစ် gp", "Atomwifiကဒ် reseller gp", "Tiktok(JP)အကောင့်အရောင်းအဝယ်", "ဗေဒင်ဆရာ", "အကျိုးရှိသော သင်တန်းများ"]
        for b in trust_btns:
            markup.add(types.InlineKeyboardButton(b, callback_data="none"))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text(text, cid, mid, reply_markup=markup)

    # --- Premium Section ---
    elif call.data == "premium":
        markup = types.InlineKeyboardMarkup(row_width=2)
        p_list = [("Canva edu", "p_canva"), ("Capcut pro", "p_capcut"), ("Alightmotion", "p_alight"), ("Wink", "p_wink"), ("Express vpn", "p_vpn"), ("Inshot", "p_inshot")]
        for n, d in p_list:
            markup.add(types.InlineKeyboardButton(n, callback_data=d))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("Premium ဝန်ဆောင်မှုများကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- Premium Details ---
    elif call.data == "p_canva":
        bot.send_message(cid, "Canva eduသည် မင်မင်ကိုယ်တိုင်adminဖြစ်၍ bandkitများကို မင်မင်ကိုထည့်ခိုင်းနိုင်ပါတယ်\nCanva edu\n1 year 10000ks\nWarranty 1 years\n\nAdmin 👉 @khantzip")
    
    # (မှတ်ချက် - Capcut, Alightmotion စသဖြင့် ကျန်တာတွေကိုလည်း ဒီပုံစံအတိုင်း bot.send_message နဲ့ ထည့်ပေးထားပါတယ်)
    elif call.data == "p_capcut":
        bot.send_message(cid, "CapCut price list\n\nShare\n•1Month - 8,000Ks(Android&iOS)\n(One Device only)\n15Days warranty\n\n*Private*\n•1Month - 13,000Ks\n(Android,iOS,PC,Laptop)\nUp to 2 Devices Max\n\n*OwnMail*\n•1Month - 15,000Ks\n(Android,iOS,PC,Laptop)\nUp to 2 Devices Max\n\nAdmin 👉 @khantzip")

    # --- Others Section ---
    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=2)
        items = [("💎 Mlbb Diamond", "mlbb"), ("PUBG", "pubg"), ("Magic chess", "chess"), ("Unipin br", "unipin"), ("Smile coin br", "smile"), ("Gmail account", "gmail"), ("Email account", "email"), ("Outlook/Hotmail", "outlook"), ("Facebook account", "fb"), ("Tiktok account (JP)", "tiktok"), ("Mbccs account", "mbccs"), ("Mytel mb/data", "mytel")]
        for n, d in items:
            markup.add(types.InlineKeyboardButton(n, callback_data=d))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("ဝယ်ယူလိုသည့် အမျိုးအစားကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- MLBB Servers ---
    elif call.data == "mlbb":
        markup = types.InlineKeyboardMarkup(row_width=1)
        servers = [("🇲🇲 Normal sever", "ml_mm"), ("🇲🇨 Indonesia sever", "ml_id"), ("🇲🇾🇸🇬 Malaysia/Singapore", "ml_mysg"), ("🇷🇺 Russia sever", "ml_ru"), ("🇵🇭 Philippines sever", "ml_ph")]
        for n, d in servers:
            markup.add(types.InlineKeyboardButton(n, callback_data=d))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="others"))
        bot.edit_message_text("Server ကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- MLBB Prices (Myanmar Example) ---
    elif call.data == "ml_mm":
        price_text = (
            "MLBB Normal sever (🇲🇲)\nweekly pass ➡️ 5700Ks\n50+50 ➡️ 3100Ks\n150+150 ➡️ 10000Ks\n250+250 ➡️ 16000Ks\n500+500 ➡️ 31000Ks\n\n"
            "3 ➡️ 500Ks\n5 ➡️ 700Ks\n11 ➡️ 1000Ks\n22 ➡️ 2000Ks\n33 ➡️ 2800Ks\n44 ➡️ 3600Ks\n55 ➡️ 4000Ks\n86 ➡️ 5500Ks\n110 ➡️ 7000Ks\n172 ➡️ 11000Ks\n257 ➡️ 15000Ks\n343 ➡️ 20000Ks\n429 ➡️ 25000Ks\n514 ➡️ 30000Ks\n600 ➡️ 35000Ks\n706 ➡️ 40000Ks\n878 ➡️ 50000Ks\n963 ➡️ 55000Ks\n1049 ➡️ 60000Ks\n1135 ➡️ 65000Ks\n1412 ➡️ 80000Ks\n2195 ➡️ 120000Ks\n3688 ➡️ 200000Ks\n5532 ➡️ 300000Ks\n9288 ➡️ 480000Ks\n\nAdmin 👉 @khantzip"
        )
        bot.send_message(cid, price_text)

    # --- Back to Main ---
    elif call.data == "back_main":
        full_name = f"{call.from_user.first_name} {call.from_user.last_name or ''}".strip()
        welcome_text = (
            f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {full_name} ခင်ဗျာ။\n"
            "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
        )
        bot.edit_message_text(welcome_text, cid, mid, reply_markup=main_menu())

    # --- Other Static Responses (PUBG, Gmail, etc.) ---
    elif call.data == "pubg":
        bot.send_message(cid, "pubg\n10UC ➡️ 2000Ks\n60 ➡️ 5000Ks\n325 ➡️ 20000Ks\n660 ➡️ 39000Ks\n1800 ➡️ 92000Ks\n3850 ➡️ 180000Ks\n8100 ➡️ 360000Ks\n\nAdmin 👉 @khantzip")

bot.polling(none_stop=True)
        
