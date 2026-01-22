import telebot
from telebot import types

# သင့်ရဲ့ Bot Token ကို ဒီမှာ ထည့်ပါ
API_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(API_TOKEN)

# ၁။ ခလုတ်အသစ်တိုးချင်ရင် သို့မဟုတ် စာသားပြင်ချင်ရင် ဒီနေရာမှာ ပြင်ပါ
prices_data = {
    "Capcut": {
        "text": "🎬 CapCut Price List\n\n• 1 Month - 1,000 Ks\n• Admin: @khantzip",
        "image": "https://example.com/capcut_photo.jpg" # ပုံ Link ရှိရင် ဒီမှာ ထည့်ပါ
    },
    "Canva": {
        "text": "🎨 Canva Education\n\n• 1 Year - 10,000 Ks\n• Warranty: 1 Year",
        "image": "" # ပုံမရှိရင် ဒီလို အလွတ်ထားပါ
    },
    "Alightmotion": {
        "text": "✨ Alight Motion Price List\n\n• Share Plan - 5,000 Ks",
        "image": ""
    }
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # ပင်မ Menu ခလုတ်များ
    btn1 = types.InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်ရန်", callback_data="movies")
    btn2 = types.InlineKeyboardButton("📱 Mod App များ", callback_data="mod_apps")
    btn3 = types.InlineKeyboardButton("💎 Pro/Premium များ", callback_data="premium_list")
    btn4 = types.InlineKeyboardButton("👨‍🏫 သင်တန်းများ", callback_data="courses")
    admin_btn = types.InlineKeyboardButton("👤 Admin နဲ့ စကားပြောမယ်", url="https://t.me/khantzip")
    
    markup.add(btn1, btn2, btn3, btn4)
    markup.add(admin_btn)
    
    bot.send_message(message.chat.id, f"မင်္ဂလာပါ {message.from_user.first_name} ခင်ဗျာ။ ✨\nကိုယ်သိချင်တာကို အောက်မှာ ရွေးချယ်ပါ 👇", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "premium_list":
        # Google Sheet အစား ဒီထဲက ခလုတ်တွေ ပေါ်လာပါမယ်
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [types.InlineKeyboardButton(name, callback_data=f"price_{name}") for name in prices_data.keys()]
        back_btn = types.InlineKeyboardButton("⬅️ နောက်သို့", callback_data="main_menu")
        markup.add(*buttons)
        markup.add(back_btn)
        bot.edit_message_text("💎 ရရှိနိုင်သော Premium များမှာ-", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data.startswith("price_"):
        item_name = call.data.replace("price_", "")
        data = prices_data.get(item_name)
        
        if data["image"]:
            bot.send_photo(call.message.chat.id, data["image"], caption=data["text"])
        else:
            bot.send_message(call.message.chat.id, data["text"])

    elif call.data == "main_menu":
        start(call.message)

bot.polling()
