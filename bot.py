import telebot
from telebot import types

# --- Configuration ---
API_TOKEN = '8377346830:AAFVtsPT3BHAWS9Vtl6pjj2BanW9LnhGtII'
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
    
    btn1 = types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်ရန်", callback_data="movies_main")
    btn2 = types.InlineKeyboardButton("📱 Mod APK များ", url="https://t.me/khantzipmodapk")
    btn3 = types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses")
    btn4 = types.InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data="trusted_sellers")
    btn5 = types.InlineKeyboardButton("💎 Pro/Premium များ", callback_data="premium_info")
    btn6 = types.InlineKeyboardButton("📦 တခြားဝယ်ယူနိုင်သောရာများ", callback_data="others")
    btn7 = types.InlineKeyboardButton("🤵 Admin နဲ့စကားပြောမယ်", url="https://t.me/khantzip")
    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup.add(btn7)
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# --- Callback Query Handler ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # --- ဇာတ်ကားကြည့်ရန် ---
    if call.data == "movies_main":
        markup = types.InlineKeyboardMarkup(row_width=2)
        m_btn1 = types.InlineKeyboardButton("📺 ဇာတ်ကားအစုံ", url="https://t.me/khantzipmainmovie")
        m_btn2 = types.InlineKeyboardButton("🇨🇳 တရုတ်ဇာတ်ကား", url="https://t.me/khantzipchinamovies")
        m_btn3 = types.InlineKeyboardButton("🇰🇷 ကိုရီးယားဇာတ်ကား", url="https://t.me/khantzipkoreamovies")
        m_btn4 = types.InlineKeyboardButton("🇮🇳 အိန္ဒိယဇာတ်ကား", url="https://t.me/khanzipindiamovie")
        m_btn5 = types.InlineKeyboardButton("🇹🇭 ထိုင်းဇာတ်ကား", url="https://t.me/khantzipthaimovie")
        m_btn6 = types.InlineKeyboardButton("🎨 Anime/Cartoon", url="https://t.me/khantzipmovie")
        m_btn7 = types.InlineKeyboardButton("🌍 နိုင်ငံခြားဇာတ်လမ်း", url="https://t.me/khantzipmovies")
        back = types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        markup.add(m_btn1, m_btn2, m_btn3, m_btn4, m_btn5, m_btn6, m_btn7)
        markup.add(back)
        bot.edit_message_text("ကြည့်ရှုလိုသော Channel ကို ရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- သင်တန်းများ ---
    elif call.data == "courses":
        markup = types.InlineKeyboardMarkup(row_width=1)
        c_btn1 = types.InlineKeyboardButton("💎 Mlbb Diamond ရောင်းနည်း", callback_data="course_10k")
        c_btn2 = types.InlineKeyboardButton("👤 FB Account သစ်ဖွင့်နည်း", callback_data="course_10k")
        c_btn3 = types.InlineKeyboardButton("🇯🇵 Tiktok Japan ဖွင့်နည်း", callback_data="course_10k")
        c_btn4 = types.InlineKeyboardButton("📧 Gmail New/နိုင်ငံချိန်းနည်း", callback_data="course_20k")
        back = types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        markup.add(c_btn1, c_btn2, c_btn3, c_btn4, back)
        bot.edit_message_text("Khantzip မှ လောလောဆယ်ရရှိသောသင်တန်းများ ✨\nသင်တန်းဈေးနှုန်းသိချင်ရင် သိချင်သောသင်တန်းကို ထပ်နှိပ်ကြည့်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "course_10k":
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🤵 Admin Account", url="https://t.me/khantzip"))
        bot.send_message(call.message.chat.id, "သင်တန်းကြေး - 10000 Ks\n\nဝယ်ယူရန် Admin ကို ဆက်သွယ်ပါ 👇", reply_markup=markup)
        
    elif call.data == "course_20k":
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🤵 Admin Account", url="https://t.me/khantzip"))
        bot.send_message(call.message.chat.id, "သင်တန်းကြေး - 20000 Ks\n\nဝယ်ယူရန် Admin ကို ဆက်သွယ်ပါ 👇", reply_markup=markup)

    # --- ယုံကြည်ရသူများ ---
    elif call.data == "trusted_sellers":
        markup = types.InlineKeyboardMarkup(row_width=1)
        t_btn1 = types.InlineKeyboardButton("🚌 ရန်ကုန်အဝေးပြေးလက်မှတ်", url="https://t.me/khantzip")
        t_btn2 = types.InlineKeyboardButton("💎 Mlbb diamond reseller gp", url="https://t.me/khantzip")
        t_btn3 = types.InlineKeyboardButton("📞 ဖုန်းMB, ဖုန်းပြောမိနစ်", url="https://t.me/khantzip")
        t_btn4 = types.InlineKeyboardButton("📶 Atomwifiကဒ် reseller gp", url="https://t.me/khantzip")
        t_btn5 = types.InlineKeyboardButton("🇯🇵 Tiktok(JP)အကောင့်အရောင်းအဝယ်", url="https://t.me/khantzip")
        t_btn6 = types.InlineKeyboardButton("🔮 ဗေဒင်ဆရာ", url="https://t.me/khantzip")
        t_btn7 = types.InlineKeyboardButton("🎓 အကျိုးရှိသော သင်တန်းများ", url="https://t.me/khantzip")
        back = types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        markup.add(t_btn1, t_btn2, t_btn3, t_btn4, t_btn5, t_btn6, t_btn7, back)
        bot.edit_message_text("လူအများအလိမ်မခံရအောင် ကျွန်တော်သိတဲ့သူများကိုညွှန်းပေးထားပါတယ် နောက်ထပ်ယုံကြည်စိတ်ချရသူများလည်း လာရောက်အပ်နှံနိုင်ပါတယ် 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- MLBB Diamond ---
    elif call.data == "premium_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        d_btn1 = types.InlineKeyboardButton("🇲🇲 MLBB Normal sever", callback_data="mlbb_mm")
        d_btn2 = types.InlineKeyboardButton("🇮🇩 Indonesia sever", callback_data="mlbb_indo")
        d_btn3 = types.InlineKeyboardButton("🇷🇺 Russia sever", callback_data="mlbb_ru")
        back = types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        markup.add(d_btn1, d_btn2, d_btn3, back)
        bot.edit_message_text("MLBB Diamond ဝယ်ယူရန် Server ကိုရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "mlbb_mm":
        text = "🇲🇲 MLBB Normal sever (🇲🇲)\n\nweekly pass ➡️ 5700Ks\n50+50 ➡️ 3100Ks\n150+150 ➡️ 10000Ks\n250+250 ➡️ 16000Ks\n500+500 ➡️ 31000Ks\n\n3 ➡️ 500Ks\n5 ➡️ 700Ks\n11 ➡️ 1000Ks\n22 ➡️ 2000Ks\n33 ➡️ 2800Ks\n44 ➡️ 3600Ks\n55 ➡️ 4000Ks\n86 ➡️ 5500Ks\n110 ➡️ 7000Ks\n172 ➡️ 11000Ks\n257 ➡️ 15000Ks\n343 ➡️ 20000Ks\n429 ➡️ 25000Ks\n514 ➡️ 30000Ks\n600 ➡️ 35000Ks\n706 ➡️ 40000Ks\n878 ➡️ 50000Ks\n963 ➡️ 55000Ks\n1049 ➡️ 60000Ks\n1135 ➡️ 65000Ks\n1412 ➡️ 80000Ks\n2195 ➡️ 120000Ks\n3688 ➡️ 200000Ks\n5532 ➡️ 300000Ks\n9288 ➡️ 480000Ks\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "mlbb_indo":
        text = "🇮🇩 Indonesia sever (🇲🇨)\n\nweekly pass ➡️ 7500Ks\n50+50 ➡️ 5000Ks\n150+150 ➡️ 14000Ks\n250+250 ➡️ 22000Ks\n500+500 ➡️ 42000Ks\n\n5 ➡️ 500Ks\n12 ➡️ 1200Ks\n28 ➡️ 3000Ks\n44 ➡️ 4000Ks\n85 ➡️ 7000Ks\n170 ➡️ 14000Ks\n240 ➡️ 19000Ks\n355 ➡️ 28000Ks\n514 ➡️ 42000Ks\n716 ➡️ 53000Ks\n2010 ➡️ 140000Ks\n4830 ➡️ 300000Ks\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    elif call.data == "mlbb_ru":
        text = "🇷🇺 Russia sever (🇷🇺)\n\nweekly pass ➡️ 9000Ks\n\n8 ➡️ 1200Ks\n35 ➡️ 3300Ks\n55 ➡️ 5000Ks\n165 ➡️ 14000Ks\n275 ➡️ 23000Ks\n565 ➡️ 45000Ks\n1155 ➡️ 90000Ks\n1765 ➡️ 135000Ks\n2975 ➡️ 230000Ks\n6000 ➡️ 450000Ks\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)

    # --- အခြားရရှိနိုင်သည်များ ---
    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=1)
        o_btn1 = types.InlineKeyboardButton("📞 Mytel MB/Call Package", callback_data="mytel_info")
        o_btn2 = types.InlineKeyboardButton("🇧🇷 Unipin BRL", callback_data="unipin_info")
        o_btn3 = types.InlineKeyboardButton("🇧🇷 Smile BRL", callback_data="smile_info")
        back = types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        markup.add(o_btn1, o_btn2, o_btn3, back)
        bot.edit_message_text("အခြားရရှိနိုင်သော ဝန်ဆောင်မှုများကို ရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "mytel_info":
        text = "Mytel Package များ ✨\n\n✓2GB + 22min onnet = 2000Ks 7days\n✓11000Ks/30D for Data + Anynet Voice/SMS=1000Ks 30days\n✓20000MB/30D = 20000Ks 30days\n✓2GB(Share) + 12GB + 1000min(Mytel) + 50min(Offnet) = 15000Ks 30days\n✓3333MB/7D = 3500Ks 7days\n✓300MB/30D = 999Ks 30days\n✓1GB/3D = 950Ks 3days\n\nAdmin 👉 @khantzip"
        bot.send_message(call.message.chat.id, text)
        
    elif call.data == "unipin_info":
        bot.send_message(call.message.chat.id, "Unipin BRL 🇧🇷\n100 - 70000 ks\n\nAdmin 👉 @khantzip")
    
    elif call.data == "smile_info":
        bot.send_message(call.message.chat.id, "Smile BRL 🇧🇷\n1K - 77000 ks\n\nAdmin 👉 @khantzip")

    elif call.data == "back_home":
        start(call.message)

bot.polling()
        
