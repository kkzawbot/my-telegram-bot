import telebot
from telebot import types

# --- Configuration ---
API_TOKEN = '8377346830:AAGVWfasXHc2AP3Q_z8VyT3WG0GyBer6Sh0'
bot = telebot.TeleBot(API_TOKEN)
ADMIN_ACCOUNT = "@khantzip"

# --- Main Start Command ---
@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.first_name
    welcome_text = (
        f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {username} ခင်ဗျာ။\n\n"
        "Khantzip bot ကနေ ကြိုဆိုပါတယ် ✨\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Buttons Grouped by 2
    btn1 = types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်ရန်", callback_data="movies_main")
    btn2 = types.InlineKeyboardButton("📱 Mod APK များ", url="https://t.me/khantzipmodapk")
    btn3 = types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses")
    btn4 = types.InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data="trusted_sellers")
    btn5 = types.InlineKeyboardButton("💎 Pro/Premium များ", callback_data="premium_info")
    btn6 = types.InlineKeyboardButton("📦 တခြားဝယ်ယူနိုင်သောအရာများ", callback_data="others")
    
    # Single Buttons at Bottom
    btn7 = types.InlineKeyboardButton("⭐ Rating ပေးရန်", url="https://t.me/khantziprating")
    btn8 = types.InlineKeyboardButton("🤵 Admin နဲ့စကားပြောမယ်", url="https://t.me/khantzip")
    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup.add(btn7)
    markup.add(btn8)
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# --- Callback Query Handler ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # --- ဇာတ်ကားကြည့်ရန် ---
    if call.data == "movies_main":
        markup = types.InlineKeyboardMarkup(row_width=2)
        m_links = [
            ("📺 ဇာတ်ကားအစုံ", "https://t.me/khantzipmainmovie"),
            ("🇨🇳 တရုတ်ဇာတ်ကား", "https://t.me/khantzipchinamovies"),
            ("🇰🇷 ကိုရီးယားဇာတ်ကား", "https://t.me/khantzipkoreamovies"),
            ("🇮🇳 အိန္ဒိယဇာတ်ကား", "https://t.me/khanzipindiamovie"),
            ("🇹🇭 ထိုင်းဇာတ်ကား", "https://t.me/khantzipthaimovie"),
            ("🎨 Anime/Cartoon", "https://t.me/khantzipmovie"),
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
            types.InlineKeyboardButton("💎 Mlbb Diamond ရောင်းနည်း", callback_data="course_10k"),
            types.InlineKeyboardButton("👤 FB Account သစ်ဖွင့်နည်း", callback_data="course_10k"),
            types.InlineKeyboardButton("🇯🇵 Tiktok Japan ဖွင့်နည်း", callback_data="course_10k"),
            types.InlineKeyboardButton("📧 Gmail New/နိုင်ငံချိန်းနည်း", callback_data="course_20k"),
            types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        )
        bot.edit_message_text("Khantzip မှ လောလောဆယ်ရရှိသောသင်တန်းများ ✨\nသင်တန်းဈေးနှုန်းသိချင်ရင် ထပ်နှိပ်ကြည့်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- Premium များ ---
    elif call.data == "premium_info":
        markup = types.InlineKeyboardMarkup(row_width=2)
        p_btns = ["Canva Edu", "Capcut", "Alightmotion", "Wink", "Inshot", "Express vpn"]
        for name in p_btns:
            markup.add(types.InlineKeyboardButton(name, callback_data=f"prem_{name.lower().replace(' ', '')}"))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("ရရှိနိုင်သော Premium ဝန်ဆောင်မှုများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- တခြားဝယ်ယူနိုင်သောအရာများ (Others Main) ---
    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=2)
        o_btns = ["MLBB Diamond", "Facebook Account", "Mbccs", "Gmail Account", "Real Email", "Outlook/Hotmail", "PUBG", "Magic Chess"]
        for name in o_btns:
            markup.add(types.InlineKeyboardButton(name, callback_data=f"oth_{name.lower().replace(' ', '')}"))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("တခြားဝယ်ယူနိုင်သော အမျိုးအစားများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- MLBB Diamond Servers ---
    elif call.data == "oth_mlbbdiamond":
        markup = types.InlineKeyboardMarkup(row_width=1)
        servers = [
            ("🇲🇲 Normal sever", "ml_mm"), ("🇮🇩 Indonesia sever", "ml_indo"),
            ("🇷🇺 Russia sever", "ml_ru"), ("🇲🇾🇸🇬 Malaysia & Singapore", "ml_mysg"),
            ("🇵🇭 Philippines", "ml_ph")
        ]
        for name, data in servers:
            markup.add(types.InlineKeyboardButton(name, callback_data=data))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="others"))
        bot.edit_message_text("MLBB Diamond ဝယ်ယူရန် Server ကိုရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- Server Prices Data ---
    elif call.data == "ml_mm":
        text = "MLBB Normal sever (🇲🇲)\nweekly pass ➡️ 5700Ks\n50+50 ➡️ 3100Ks\n150+150 ➡️ 10000Ks\n250+250 ➡️ 16000Ks\n500+500 ➡️ 31000Ks\n\n3➡️500 | 5➡️700 | 11➡️1000 | 22➡️2000 | 33➡️2800 | 44➡️3600 | 55➡️4000\n86➡️5500 | 110➡️7000 | 172➡️11000 | 257➡️15000 | 343➡️20000 | 429➡️25000\n514➡️30000 | 600➡️35000 | 706➡️40000 | 878➡️50000 | 963➡️55000 | 1049➡️60000\n1135➡️65000 | 1412➡️80000 | 2195➡️120000 | 3688➡️200000 | 5532➡️300000 | 9288➡️480000\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "ml_mysg":
        text = "Malaysia & Singapore ( 🇲🇾🇸🇬 )\nweekly pass sg ➡️ 8600Ks\nweekly pass my ➡️ 8500Ks\n50+50 ➡️ 4500Ks | 150+150 ➡️ 13000Ks | 250+250 ➡️ 21000Ks | 500+500 ➡️ 42000Ks\n\n14➡️1500 | 28➡️2500 | 42➡️4000 | 56➡️5500 | 70➡️7000 | 84➡️8500 | 112➡️11000\n140➡️14000 | 154➡️16000 | 210➡️20000 | 284➡️25000 | 355➡️30000 | 429➡️35000\n569➡️46000 | 716➡️57000 | 856➡️68000 | 898➡️73000 | 1000➡️82000 | 1084➡️89000\n1145➡️95000 | 1284➡️110000 | 1446➡️130000 | 2162➡️180000 | 2976➡️230000\n3692➡️285000 | 4422➡️335000 | 5952➡️440000 | 6012➡️450000 | 7502➡️550000\n8948➡️660000 | 10478➡️760000 | 11924➡️870000 | 13454➡️960000 | 15004➡️1080000\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "ml_ph":
        text = "Philippines ( 🇵🇭 )\nweekly pass ➡️ 6600Ks\n50+50 ➡️ 4100Ks | 150+150 ➡️ 11000Ks | 250+250 ➡️ 17000Ks | 500+500 ➡️ 35000Ks\n\n5➡️700 | 11➡️1100 | 22➡️2000 | 56➡️4200 | 112➡️7500 | 223➡️15000 | 336➡️22000\n570➡️35000 | 1163➡️69000 | 2398➡️140000 | 6042➡️330000\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    # --- Other Items Detailed ---
    elif call.data == "oth_gmailaccount":
        text = "Gmail (Any countries)\n1acc 10000ks 3months warranty\nအကောင့်အဟောင်းပါ lockမကျ (Userဘက်က ဖြစ်တာတော့ အာမမခံပါ)\nAvailable: 100\n\nမြန်မာ gmail (အာမခံမပါ) 1acc 5000ks\nAvailable: 20\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "oth_realemail":
        bot.send_message(call.message.chat.id, "Email (real mail)\n1account 3000ks\nAvailable 100\n\nAdmin 👉 @khantzip")

    elif call.data == "oth_outlook/hotmail":
        bot.send_message(call.message.chat.id, "Outlook/Hotmail\n1 account 5000ks (စိတ်ကြိုက်ရ)\nAvailable 30\n\nAdmin 👉 @khantzip")

    elif call.data == "oth_mbccs":
        bot.send_message(call.message.chat.id, "Mbccs account\nလူကြီးမင်းရဲ့ ကိုယ်ပိုင်မိုင်တဲလ်ဖုန်းနံပါတ်နဲ့\nဈေးနှုန်း - 40000ks\n\nAdmin 👉 @khantzip")

    elif call.data == "oth_facebookaccount":
        bot.send_message(call.message.chat.id, "Facebook account (Email ဖြင့်)\nဈေးနှုန်း - 5000ks\n\nAdmin 👉 @khantzip")

    elif call.data == "oth_pubg":
        text = "PUBG UC List\n10UC ➡️ 2000Ks\n60 ➡️ 5000Ks\n325 ➡️ 20000Ks\n660 ➡️ 39000Ks\n1800 ➡️ 92000Ks\n3850 ➡️ 180000Ks\n8100 ➡️ 360000Ks\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "oth_magicchess":
        text = "Magic Chess\nweekly pass ➡️ 6500 Ks\n50+50 ➡️ 3500Ks | 150+150 ➡️ 10000Ks | 250+250 ➡️ 17000Ks | 500+500 ➡️ 32000Ks\n\n5➡️550 | 11➡️1000 | 19➡️1500 | 22➡️2000 | 59➡️4500 | 86➡️6000 | 172➡️12000\n257➡️17000 | 296➡️20000 | 344➡️24000 | 408➡️28000 | 516➡️35000 | 706➡️45000\n875➡️55000 | 1346➡️79000 | 1825➡️105000 | 2010➡️120000 | 2195➡️130000\n3688➡️205000 | 4830➡️270000 | 5532➡️310000 | 9288➡️500000\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    # --- Premium Detailed ---
    elif call.data == "prem_canvaedu":
        bot.send_message(call.message.chat.id, "Canva Edu\n1 year 10000ks\nWarranty 1 years\n\nAdmin 👉 @khantzip")

    elif call.data == "prem_capcut":
        text = "CapCut price list\n\nShare: •1Month-8,000Ks (1 Device)\nPrivate: •1Month-13,000Ks (2 Devices)\nOwnMail: •1Month-15,000Ks (2 Devices)\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "prem_alightmotion":
        text = "✨ Alight Motion ✨\n\nShare: 1Year ≈ 5,000Ks (1 Device)\nPrivate: 1Year ≈ 7,000Ks (8 Devices)\nOwnMail: 1Year ≈ 10,000Ks (8 Devices)\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "prem_wink":
        text = "✨ Wink ✨\n\nShare: 1Mo-10k / 1Yr-60k\nPrivate: 1Mo-20k\nOwnmail: 1Mo-25k\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "prem_expressvpn":
        text = "Express Vpn\n\nShare: 1Mo-2,000Ks(Mobile) / 3,500Ks(PC)\nPrivate: 1Mo-10,000Ks (9 Devices)\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "prem_inshot":
        bot.send_message(call.message.chat.id, "✨ InShot ✨\nLifetime Premium — 20,000 Ks\n(1 Device Only/Not MOD)\n\nOrder: @khantzip")

    # --- Standard Handlers ---
    elif call.data == "back_home":
        start(call.message)

bot.polling()
        
