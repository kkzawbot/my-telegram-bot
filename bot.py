import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# သင့် Bot Token
TOKEN = '8377346830:AAFVtsPT3BHAWS9Vtl6pjj2BanW9LnhGtII'

# Bot Start လုပ်တဲ့အခါ ပို့မယ့်စာနဲ့ Button များ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.full_name
    
    # သင်ပေးထားတဲ့ Logo ပုံကို စာနဲ့အတူ ပို့ပေးပါမယ်
    welcome_text = (
        f"မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ {user_name} ခင်ဗျာ။\n\n"
        "Khantzip bot ကနေ ကြိုဆိုပါတယ် ✨\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    )

    # Buttons ဆောက်ခြင်း
    keyboard = [
        [
            InlineKeyboardButton("🎓 ရနိုင်သောသင်တန်းများ", callback_data='courses'),
            InlineKeyboardButton("📶 ရနိုင်သော MB/Min ဈေးနှုန်း", callback_data='data_price')
        ],
        [
            InlineKeyboardButton("💎 Pro/Premium ဈေးများ", callback_data='premium_price'),
            InlineKeyboardButton("✅ 100% ယုံကြည်စိတ်ချရသူများ", callback_data='trusted')
        ],
        [
            InlineKeyboardButton("👨‍💻 Admin နဲ့ စကားပြောမယ်", url='https://t.me/kkzawbot') # သင့် Username ပြောင်းထားပေးပါတယ်
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)

# ခလုတ်တွေနှိပ်ရင် စာပြန်ဖို့
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'courses':
        await query.message.reply_text(text="📚 လက်ရှိတက်ရောက်နိုင်သော သင်တန်းများမှာ... \n(ဒီနေရာမှာ သင်တန်းစာရင်းတွေ ပြန်ဖြည့်နိုင်ပါတယ်)")
    elif query.data == 'data_price':
        await query.message.reply_text(text="📶 အသက်သာဆုံး MB/Min ဈေးနှုန်းများမှာ... \n(ဒီနေရာမှာ ဈေးနှုန်းတွေ ပြန်ဖြည့်နိုင်ပါတယ်)")
    elif query.data == 'premium_price':
        await query.message.reply_text(text="💎 Pro/Premium ဝန်ဆောင်မှု ဈေးနှုန်းများမှာ... \n(ဒီနေရာမှာ ဈေးနှုန်းတွေ ပြန်ဖြည့်နိုင်ပါတယ်)")
    elif query.data == 'trusted':
        await query.message.reply_text(text="✅ ကျွန်ုပ်တို့သည် 100% ယုံကြည်စိတ်ချရသော ဝန်ဆောင်မှုများကို ပေးအပ်နေပါသည်။")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Khantzip Bot is running...")
    app.run_polling()
