import telebot
from telebot import types

# --- Configuration ---
API_TOKEN = '8377346830:AAGVWfasXHc2AP3Q_z8VyT3WG0GyBer6Sh0'
bot = telebot.TeleBot(API_TOKEN)

# --- Main Menu Function ---
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
    # --- ၁။ ယုံကြည်ရသူများ ---
    if call.data == "trusted_sellers":
        text = "လူအများအလိမ်မခံရအောင် ကျွန်တော်သိတဲ့သူများကိုညွှန်းပေးထားပါတယ် နောက်ထပ်ယုံကြည်စိတ်ချရသူများလည်း လာရောက်အပ်နှံနိုင်ပါတယ်"
        markup = types.InlineKeyboardMarkup(row_width=1)
        trust_btns = [
            types.InlineKeyboardButton("🚌 ရန်ကုန်အဝေးပြေးလက်မှတ်", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("💎 Mlbb diamond reseller gp", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("📞 ဖုန်းMB, ဖုန်းပြောမိနစ်", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("📶 Atomwifiကဒ် reseller gp", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("🇯🇵 Tiktok(JP)အကောင့်အရောင်းအဝယ်", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("🔮 ဗေဒင်ဆရာ", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("🎓 အကျိုးရှိသော သင်တန်းများ", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        ]
        markup.add(*trust_btns)
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- ၂။ MLBB Normal Server (🇲🇲) တစ်ကြောင်းချင်းစီ စီခြင်း ---
    elif call.data == "ml_mm":
        price_list = (
            "MLBB Normal sever (🇲🇲)\n"
            "weekly pass ➡️ 5700Ks\n"
            "50+50 ➡️ 3100Ks\n"
            "150+150 ➡️ 10000Ks\n"
            "250+250 ➡️ 16000Ks\n"
            "500+500 ➡️ 31000Ks\n\n"
            "3 ➡️ 500Ks\n"
            "5 ➡️ 700Ks\n"
            "11 ➡️ 1000Ks\n"
            "22 ➡️ 2000Ks\n"
            "33 ➡️ 2800Ks\n"
            "44 ➡️ 3600Ks\n"
            "55 ➡️ 4000Ks\n"
            "86 ➡️ 5500Ks\n"
            "110 ➡️ 7000Ks\n"
            "172 ➡️ 11000Ks\n"
            "257 ➡️ 15000Ks\n"
            "343 ➡️ 20000Ks\n"
            "429 ➡️ 25000Ks\n"
            "514 ➡️ 30000Ks\n"
            "600 ➡️ 35000Ks\n"
            "706 ➡️ 40000Ks\n"
            "878 ➡️ 50000Ks\n"
            "963 ➡️ 55000Ks\n"
            "1049 ➡️ 60000Ks\n"
            "1135 ➡️ 65000Ks\n"
            "1412 ➡️ 80000Ks\n"
            "2195 ➡️ 120000Ks\n"
            "3688 ➡️ 200000Ks\n"
            "5532 ➡️ 300000Ks\n"
            "9288 ➡️ 480000Ks\n\n"
            "Admin 👉 @khantzip"
        )
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 Back", callback_data="oth_mlbbdiamond"))
        bot.edit_message_text(price_list, call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- ၃။ တခြား Server များ (ဥပမာ Indo, Russia) ---
    elif call.data == "ml_indo":
        text = "indonisia sever ( 🇲🇨 )\nweekly pass ➡️ 7500Ks\n50+50 ➡️ 5000Ks\n150+150 ➡️ 14000Ks\n250+250 ➡️ 22000Ks\n500+500 ➡️ 42000Ks\n\n5 ➡️ 500Ks\n12 ➡️ 1200Ks\n28 ➡️ 3000Ks\n44 ➡️ 4000Ks\n85 ➡️ 7000Ks\n170 ➡️ 14000Ks\n240 ➡️ 19000Ks\n355 ➡️ 28000Ks\n514 ➡️ 42000Ks\n716 ➡️ 53000Ks\n2010 ➡️ 140000Ks\n4830 ➡️ 300000Ks\n\nAdmin 👉 @khantzip"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 Back", callback_data="oth_mlbbdiamond")))

    # --- ၄။ Back to Home (Edit Message စနစ်ဖြင့် အရင်စာကို ဖျက်ခြင်း) ---
    elif call.data == "back_home":
        username = call.from_user.first_name
        text = f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {username} ခင်ဗျာ။\n\nKhantzip bot ကနေ ကြိုဆိုပါတယ် ✨\nကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=main_menu_markup())

    # (မှတ်ချက် - ကျန်ရှိသော Premium, Movies စသည့် Callback များအားလုံးကိုလည်း edit_message_text ဖြင့် ထည့်သွင်းပေးထားပါသည်)
    elif call.data == "premium_info":
        markup = types.InlineKeyboardMarkup(row_width=2)
        p_btns = [types.InlineKeyboardButton(x, callback_data=f"prem_{x.lower().replace(' ', '')}") for x in ["Canva Edu", "Capcut", "Alightmotion", "Wink", "Inshot", "Express vpn"]]
        markup.add(*p_btns)
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("ရရှိနိုင်သော Premium ဝန်ဆောင်မှုများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=2)
        o_btns = [types.InlineKeyboardButton(x, callback_data=f"oth_{x.lower().replace(' ', '')}") for x in ["MLBB Diamond", "Facebook Account", "Mbccs", "Gmail Account", "Real Email", "Outlook/Hotmail", "PUBG", "Magic Chess"]]
        markup.add(*o_btns)
        markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("တခြားဝယ်ယူနိုင်သော အမျိုးအစားများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "oth_mlbbdiamond":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🇲🇲 Normal sever", callback_data="ml_mm"),
                   types.InlineKeyboardButton("🇮🇩 Indonesia sever", callback_data="ml_indo"),
                   types.InlineKeyboardButton("🔙 Back", callback_data="others"))
        bot.edit_message_text("MLBB Diamond ဝယ်ယူရန် Server ကိုရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

bot.polling()
    
