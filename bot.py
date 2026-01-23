import telebot
from telebot import types

# --- Configuration ---
API_TOKEN = '8377346830:AAGVWfasXHc2AP3Q_z8VyT3WG0GyBer6Sh0'
bot = telebot.TeleBot(API_TOKEN)
ADMIN_LINK = "https://t.me/khantzip"

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်မယ်", callback_data="movies"),
        types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses"),
        types.InlineKeyboardButton("📱 Mod apk", url="https://t.me/khantzipmodapk"),
        types.InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data="trusted"),
        types.InlineKeyboardButton("💎 Pro/premium များ", callback_data="premium"),
        types.InlineKeyboardButton("📦 တခြားရနိုင်သည်များ", callback_data="others")
    )
    markup.add(types.InlineKeyboardButton("⭐ Rating ပေးရန်", url="https://t.me/khantziprating"))
    markup.add(types.InlineKeyboardButton("🤵 Admin နဲ့စကားပြောမယ်", url=ADMIN_LINK))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    full_name = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
    welcome_text = f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {full_name} ခင်ဗျာ။\nကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    cid = call.message.chat.id
    mid = call.message.message_id

    # --- ဇာတ်ကားကြည့်မယ် ---
    if call.data == "movies":
        markup = types.InlineKeyboardMarkup(row_width=1)
        links = [("📺 ဇာတ်ကားအစုံအဓိက channel", "https://t.me/khantzipmainmovie"), ("🇨🇳 တရုတ်ဇာတ်ကား", "https://t.me/khantzipchinamovies"), ("🇰🇷 ကိုရီးယားဇာတ်ကား", "https://t.me/khantzipkoreamovies"), ("🇮🇳 အိန္ဒိယဇာတ်ကား", "https://t.me/khanzipindiamovie"), ("🇹🇭 ထိုင်းဇာတ်ကား", "https://t.me/khantzipthaimovie"), ("🎨 Anime,cartoon,animation", "https://t.me/khantzipmovie"), ("🌍 နိုင်ငံခြားဇာတ်လမ်း", "https://t.me/khantzipmovies")]
        for n, u in links: markup.add(types.InlineKeyboardButton(n, url=u))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("ကြည့်ရှုလိုသော Channel ကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- သင်တန်းများ ---
    elif call.data == "courses":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("💎 Mlbb diamondရောင်းနည်း", callback_data="c_10k"), types.InlineKeyboardButton("👤 Facebook account သစ်ဖွင့်နည်း", callback_data="c_10k"), types.InlineKeyboardButton("🇯🇵 Tiktok Japan accountဖွင့်နည်း", callback_data="c_10k"), types.InlineKeyboardButton("📧 Gmail new accountနှင့် နိုင်ငံချိန်းနည်း", callback_data="c_20k"), types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("khantzipမှ လောလောဆယ်ရရှိသောသင်တန်းများ\nသင်တန်းဈေးနှုန်းသိချင်ရင် ထပ်နှိပ်ကြည့်ပါ 👇", cid, mid, reply_markup=markup)

    elif call.data == "c_10k": bot.send_message(cid, "သင်တန်းကြေး - 10000ks\nAdmin 👉 @khantzip")
    elif call.data == "c_20k": bot.send_message(cid, "သင်တန်းကြေး - 20000ks\nAdmin 👉 @khantzip")

    # --- ယုံကြည်ရသူများ ---
    elif call.data == "trusted":
        text = "လူအများအလိမ်မခံရအောင် ကျွန်တော်သိတဲ့သူများကိုညွှန်းပေးထားပါတယ် နောက်ထပ်ယုံကြည်စိတ်ချရသူများလည်း လာရောက်အပ်နှံနိုင်ပါတယ်"
        markup = types.InlineKeyboardMarkup(row_width=1)
        btns = ["ရန်ကုန်အဝေးပြေးလက်မှတ်", "Mlbb diamond reseller gp", "ဖုန်းMB, ဖုန်းပြောမိနစ် gp", "Atomwifiကဒ် reseller gp", "Tiktok(JP)အကောင့်အရောင်းအဝယ်", "ဗေဒင်ဆရာ", "အကျိုးရှိသော သင်တန်းများ"]
        for b in btns: markup.add(types.InlineKeyboardButton(b, callback_data="none"))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text(text, cid, mid, reply_markup=markup)

    # --- Pro/Premium ---
    elif call.data == "premium":
        markup = types.InlineKeyboardMarkup(row_width=2)
        p_list = [("Canva edu", "p_canva"), ("Capcut pro", "p_capcut"), ("Alightmotion", "p_alight"), ("Wink", "p_wink"), ("Express vpn", "p_vpn"), ("Inshot", "p_inshot")]
        for n, d in p_list: markup.add(types.InlineKeyboardButton(n, callback_data=d))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("Premium ဝန်ဆောင်မှုများကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    elif call.data == "p_canva": bot.send_message(cid, "Canva eduသည် မင်မင်ကိုယ်တိုင်adminဖြစ်၍ bandkitများကို မင်မင်ကိုထည့်ခိုင်းနိုင်ပါတယ်\n1 year 10000ks\nWarranty 1 years\nAdmin 👉 @khantzip")
    elif call.data == "p_capcut": bot.send_message(cid, "CapCut price list\n\nShare: 1Month - 8,000Ks\nPrivate: 1Month - 13,000Ks\nOwnMail: 1Month - 15,000Ks\nAdmin 👉 @khantzip")
    elif call.data == "p_alight": bot.send_message(cid, "✨ Alight Motion ✨\nShare: 1Year - 5,000Ks\nPrivate: 1Year - 7,000Ks\nOwnMail: 1Year - 10,000Ks\nAdmin 👉 @khantzip")
    elif call.data == "p_wink": bot.send_message(cid, "✨ Wink ✨\nShare: 1Month - 10,000Ks / 1Year - 60,000Ks\nPrivate: 1Month - 20,000Ks\nOwnMail: 1Month - 25,000Ks\nAdmin 👉 @khantzip")
    elif call.data == "p_vpn": bot.send_message(cid, "Express Vpn\nShare: 1Month - 2,000Ks(Phone) / 3,500Ks(PC)\nPrivate: 1Month - 10,000Ks\nAdmin 👉 @khantzip")
    elif call.data == "p_inshot": bot.send_message(cid, "✨ InShot ✨\nShare Plan: Lifetime - 20,000 Ks\nOrder: @khantzip")

    # --- တခြားရနိုင်သည်များ ---
    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=2)
        items = [("MLBB Diamond", "mlbb"), ("PUBG", "pubg"), ("Magic chess", "chess"), ("Unipin br", "unipin"), ("Smile coin br", "smile"), ("Gmail account", "gmail"), ("Email account", "email"), ("Outlook/Hotmail", "outlook"), ("Facebook account", "fb"), ("Tiktok account (JP)", "tiktok"), ("Mbccs account", "mbccs"), ("Mytel mb/data", "mytel")]
        for n, d in items: markup.add(types.InlineKeyboardButton(n, callback_data=d))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_main"))
        bot.edit_message_text("ဝယ်ယူလိုသည့် အမျိုးအစားကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- MLBB Servers ---
    elif call.data == "mlbb":
        markup = types.InlineKeyboardMarkup(row_width=1)
        s = [("🇲🇲 Normal sever", "ml_mm"), ("🇲🇨 Indonesia sever", "ml_id"), ("🇲🇾🇸🇬 Malaysia/Singapore", "ml_mysg"), ("🇷🇺 Russia sever", "ml_ru"), ("🇵🇭 Philippines sever", "ml_ph")]
        for n, d in s: markup.add(types.InlineKeyboardButton(n, callback_data=d))
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="others"))
        bot.edit_message_text("Server ကို ရွေးချယ်ပါ 👇", cid, mid, reply_markup=markup)

    # --- Malaysia & Singapore (🇲🇾🇸🇬) ---
elif call.data == "ml_mysg":
    text = (
        "Malaysia & Singapore ( 🇲🇾🇸🇬 )\n"
        "weekly pass sg  ➡️ 8600Ks\n"
        "weekly pass my  ➡️ 8500Ks\n"
        "50+50  ➡️ 4500Ks\n"
        "150+150  ➡️ 13000Ks\n"
        "250+250  ➡️ 21000Ks\n"
        "500+500  ➡️ 42000Ks\n\n"
        "14➡️1500Ks | 28➡️2500Ks | 42➡️4000Ks\n"
        "56➡️5500Ks | 70➡️7000Ks | 84➡️8500Ks\n"
        "112➡️11000Ks | 140➡️14000Ks | 154➡️16000Ks\n"
        "210➡️20000Ks | 284➡️25000Ks | 355➡️30000Ks\n"
        "429➡️35000Ks | 569➡️46000Ks | 716➡️57000Ks\n"
        "856➡️68000Ks | 898➡️73000Ks | 1000➡️82000Ks\n"
        "1084➡️89000Ks | 1145➡️95000Ks | 1284➡️110000Ks\n"
        "1446➡️130000Ks | 2162➡️180000Ks | 2976➡️230000Ks\n"
        "3692➡️285000Ks | 4422➡️335000Ks | 5952➡️440000Ks\n"
        "6012➡️450000Ks | 7502➡️550000Ks | 8948➡️660000Ks\n"
        "10478➡️760000Ks | 11924➡️870000Ks | 13454➡️960000Ks\n"
        "15004➡️1080000Ks\n\n"
        "Admin 👉 @khantzip"
    )
    bot.send_message(cid, text)

# --- Philippines ( 🇵🇭 ) ---
elif call.data == "ml_ph":
    text = (
        "Philippines ( 🇵🇭 )\n"
        "weekly pass  ➡️ 6600Ks\n"
        "50+50  ➡️ 4100Ks\n"
        "150+150  ➡️ 11000Ks\n"
        "250+250  ➡️ 17000Ks\n"
        "500+500 ➡️  35000Ks\n\n"
        "5➡️700Ks | 11➡️1100Ks | 22➡️2000Ks\n"
        "56➡️4200Ks | 112➡️7500Ks | 223➡️15000Ks\n"
        "336➡️22000Ks | 570➡️35000Ks | 1163➡️69000Ks\n"
        "2398➡️140000Ks | 6042➡️330000Ks\n\n"
        "Admin 👉 @khantzip"
    )
    bot.send_message(cid, text)

# --- Outlook/Hotmail & Mbccs ---
elif call.data == "outlook":
    bot.send_message(cid, "Outlook/Hotmail\n1 account 5000ks\nAvailable 30\nစိတ်ကြိုက်ရ\n\nAdmin 👉 @khantzip")

elif call.data == "mbccs":
    bot.send_message(cid, "လူကြီးမင်းရဲ့ ကိုယ်ပိုင်မိုင်တဲလ်ဖုန်းနံပါတ်နဲ့\n40000ks\n\nAdmin 👉 @khantzip")
# --- Server Prices (အကုန်ထည့်ပေးထားပါတယ်) ---
    elif call.data == "ml_mm":
        bot.send_message(cid, "MLBB Normal sever (🇲🇲)\nweekly pass ➡️ 5700Ks\n50+50 ➡️ 3100Ks\n150+150 ➡️ 10000Ks\n250+250 ➡️ 16000Ks\n500+500 ➡️ 31000Ks\n\n3➡️500Ks / 5➡️700Ks / 11➡️1000Ks / 22➡️2000Ks / 33➡️2800Ks / 44➡️3600Ks / 55➡️4000Ks / 86➡️5500Ks / 110➡️7000Ks / 172➡️11000Ks / 257➡️15000Ks / 343➡️20000Ks / 429➡️25000Ks / 514➡️30000Ks / 600➡️35000Ks / 706➡️40000Ks / 878➡️50000Ks / 963➡️55000Ks / 1049➡️60000Ks / 1135➡️65000Ks / 1412➡️80000Ks / 2195➡️120000Ks / 3688➡️200000Ks / 5532➡️300000Ks / 9288➡️480000Ks\n\nAdmin 👉 @khantzip")
    elif call.data == "ml_ru":
        bot.send_message(cid, "Russia (🇷🇺)\nweekly pass ➡️ 9000Ks\n\n8➡️1200Ks / 35➡️3300Ks / 55➡️5000Ks / 165➡️14000Ks / 275➡️23000Ks / 565➡️45000Ks / 1155➡️90000Ks / 1765➡️135000Ks / 2975➡️230000Ks / 6000➡️450000Ks\n\nAdmin 👉 @khantzip")
    elif call.data == "ml_id":
        bot.send_message(cid, "Indonesia (🇲🇨)\nweekly pass ➡️ 7500Ks\n50+50 ➡️ 5000Ks\n150+150 ➡️ 14000Ks\n250+250 ➡️ 22000Ks\n500+500 ➡️ 42000Ks\n\n5➡️500Ks / 12➡️1200Ks / 28➡️3000Ks / 44➡️4000Ks / 85➡️7000Ks / 170➡️14000Ks / 240➡️19000Ks / 355➡️28000Ks / 514➡️42000Ks / 716➡️53000Ks / 2010➡️140000Ks / 4830➡️300000Ks\n\nAdmin 👉 @khantzip")
    elif call.data == "chess":
        bot.send_message(cid, "Magic chess\nweekly pass ➡️ 6500 Ks\n50+50➡️3500Ks / 150+150➡️10000Ks / 250+250➡️17000Ks / 500+500➡️32000Ks\n\n5➡️550 / 11➡️1000 / 19➡️1500 / 22➡️2000 / 59➡️4500 / 86➡️6000 / 172➡️12000 / 257➡️17000 / 296➡️20000 / 344➡️24000 / 408➡️28000 / 516➡️35000 / 706➡️45000 / 875➡️55000 / 1346➡️79000 / 1825➡️105000 / 2010➡️120000 / 2195➡️130000 / 3688➡️205000 / 4830➡️270000 / 5532➡️310000 / 9288➡️500000\n\nAdmin 👉 @khantzip")
    
    # --- Others Details ---
    elif call.data == "pubg": bot.send_message(cid, "PUBG\n10UC➡️2000Ks / 60➡️5000Ks / 325➡️20000Ks / 660➡️39000Ks / 1800➡️92000Ks / 3850➡️180000Ks / 8100➡️360000Ks\nAdmin 👉 @khantzip")
    elif call.data == "unipin": bot.send_message(cid, "Unipin BR\n100 - 70000 ks\nAdmin 👉 @khantzip")
    elif call.data == "smile": bot.send_message(cid, "Smile coin BR 🇧🇷\n1K - 78000 ks\nAdmin 👉 @khantzip")
    elif call.data == "mytel": bot.send_message(cid, "Mytel MB/Call\n✓2GB+22min=2000Ks(7D)\n✓11000Ks(30D) Data+Voice\n✓20000MB=20000Ks(30D)\n✓12GB+1000min=15000Ks(30D)\n3333MB=3500Ks(7D)\n300MB=999Ks(30D)\n1GB=950Ks(3D)")
    elif call.data == "gmail": bot.send_message(cid, "Gmail Account\nAny countries: 10000ks (3mo warranty)\nMyanmar: 5000ks (No warranty)\nAdmin 👉 @khantzip")
    elif call.data == "fb": bot.send_message(cid, "Facebook Account\nEmail ဖြင့် - 5000ks\nAdmin 👉 @khantzip")

    elif call.data == "back_main":
        bot.edit_message_text(call.message.text, cid, mid, reply_markup=main_menu())

bot.polling(none_stop=True)
    
