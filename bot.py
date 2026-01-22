import telebot
from telebot import types

# --- Configuration (New Token Updated) ---
API_TOKEN = '8377346830:AAFVtsPT3BHAWS9Vtl6pjj2BanW9LnhGtII'
bot = telebot.TeleBot(API_TOKEN)

def main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်ရန်", callback_data="movies_main"),
        types.InlineKeyboardButton("📱 Mod APK များ", url="https://t.me/khantzipmodapk"),
        types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses"),
        types.InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data="trusted_sellers"),
        types.InlineKeyboardButton("💎 Pro/Premium များ", callback_data="premium_info"),
        types.InlineKeyboardButton("📦 တခြားဝယ်ယူနိုင်သောအရာများ", callback_data="others"),
        types.InlineKeyboardButton("⭐ Rating ပေးရန်", url="https://t.me/khantziprating"),
        types.InlineKeyboardButton("🤵 Admin နဲ့စကားပြောမယ်", url="https://t.me/khantzip")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    # နာမည်အပြည့်အစုံ (First Name + Last Name) ပေါ်ရန် ပြင်ဆင်ထားသည်
    full_name = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
    welcome_text = (
        f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {full_name} ခင်ဗျာ။\n\n"
        "Khantzip bot ကနေ ကြိုဆိုပါတယ် ✨\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    full_name = f"{call.from_user.first_name} {call.from_user.last_name or ''}".strip()

    # --- MLBB Servers ---
    if call.data == "mlbb_servers":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🇲🇲 Normal sever", callback_data="ml_mm"),
            types.InlineKeyboardButton("🇮🇩 Indonesia sever", callback_data="ml_indo"),
            types.InlineKeyboardButton("🇷🇺 Russia sever", callback_data="ml_ru"),
            types.InlineKeyboardButton("🇲🇾🇸🇬 Malaysia & Singapore sever", callback_data="ml_mysg"),
            types.InlineKeyboardButton("🇵🇭 Philippines", callback_data="ml_ph"),
            types.InlineKeyboardButton("🔙 Back", callback_data="others")
        )
        bot.edit_message_text("Server ကိုရွေးချယ်ပါ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- MLBB Prices (Myanmar Server) ---
    elif call.data == "ml_mm":
        price = (
            "MLBB Normal sever (🇲🇲)\n"
            "weekly pass ➡️ 5700Ks\n50+50 ➡️ 3100Ks\n150+150 ➡️ 10000Ks\n250+250 ➡️ 16000Ks\n500+500 ➡️ 31000Ks\n\n"
            "3➡️500 | 5➡️700 | 11➡️1000 | 22➡️2000 |\n33➡️2800 | 44➡️3600 | 55➡️4000\n"
            "86➡️5500 | 110➡️7000 | 172➡️11000 | 257➡️15000 |\n343➡️20000 | 429➡️25000\n"
            "514➡️30000 | 600➡️35000 | 706➡️40000 | 878➡️50000 |\n963➡️55000 | 1049➡️60000\n"
            "1135➡️65000 | 1412➡️80000 | 2195➡️120000 |\n3688➡️200000 | 5532➡️300000 | 9288➡️480000\n\n"
            "Admin 👉 @khantzip"
        )
        bot.edit_message_text(price, call.message.chat.id, call.message.message_id, 
                              reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 Back", callback_data="mlbb_servers")))

    # --- Premium Prices ---
    elif call.data == "premium_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # ပုံထဲမှ ဈေးနှုန်းများအတိုင်း ထည့်သွင်းပေးထားပါသည်
        markup.add(
            types.InlineKeyboardButton("Canva Edu - 1000Ks", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("Capcut Premium - 3000Ks", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("Alight Motion - 2000Ks", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("Wink Premium - 2000Ks", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("Inshot Premium - 2000Ks", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        )
        bot.edit_message_text("ရရှိနိုင်သော Premium ဝန်ဆောင်မှုများနှင့် ဈေးနှုန်းများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    # --- Magic Chess Prices ---
    elif call.data == "magic_chess":
        price = (
            "Magic Chess\nweekly pass ➡️ 6500 Ks\n50+50 ➡️ 3500Ks | 150+150 ➡️ 10000Ks |\n"
            "250+250 ➡️ 17000Ks | 500+500 ➡️ 32000Ks\n\n"
            "5➡️550 | 11➡️1000 | 19➡️1500 | 22➡️2000 |\n59➡️4500 | 86➡️6000 | 172➡️12000\n"
            "257➡️17000 | 296➡️20000 | 344➡️24000 |\n408➡️28000 | 516➡️35000 | 706➡️45000 |\n"
            "875➡️55000 | 1346➡️79000 | 1825➡️105000 |\n2010➡️120000 | 2195➡️130000 | 3688➡️205000 |\n"
            "4830➡️270000 | 5532➡️310000 | 9288➡️500000\n\n"
            "Admin 👉 @khantzip"
        )
        bot.edit_message_text(price, call.message.chat.id, call.message.message_id, 
                              reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 Back", callback_data="others")))

    # --- Others Menu ---
    elif call.data == "others":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("💎 MLBB Diamond", callback_data="mlbb_servers"),
            types.InlineKeyboardButton("👤 Facebook account", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("💰 Mbccs", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("📧 Gmail account", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("♟️ Magic chess", callback_data="magic_chess"),
            types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        )
        bot.edit_message_text("တခြားဝယ်ယူနိုင်သော အမျိုးအစားများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "back_home":
        text = f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {full_name} ခင်ဗျာ။\n\nကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=main_menu_markup())

    # --- Additional Menus ---
    elif call.data == "courses":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("💎 Mlbb diamond ရောင်းနည်း - 10000Ks", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("👤 FB Account သစ်ဖွင့်နည်း - 10000Ks", url="https://t.me/khantzip"),
            types.InlineKeyboardButton("🔙 Back", callback_data="back_home")
        )
        bot.edit_message_text("သင်တန်းဈေးနှုန်းများ 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "trusted_sellers":
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("ယုံကြည်ရသူများစာရင်းကို Admin ထံ မေးမြန်းနိုင်ပါသည်", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "movies_main":
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 Back", callback_data="back_home"))
        bot.edit_message_text("ဇာတ်ကား Channel များသို့ Admin ထံမှ link တောင်းယူနိုင်ပါသည်", call.message.chat.id, call.message.message_id, reply_markup=markup)

bot.polling()
        
