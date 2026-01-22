import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- CONFIGURATION ---
TOKEN = '8377346830:AAFVtsPT3BHAWS9Vtl6pjj2BanW9LnhGtII'
ADMIN_ID = 7072756798 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "မင်္ဂလာရှိအပေါင်းနဲ့ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ Khant Zip ခင်ဗျာ။\n\n"
        "Khantzip bot ကနေ ကြိုဆိုပါတယ် ✨\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း နှစ်သက်ရာ ရွေးချယ်ပါ👇"
    )
    
    keyboard = [
        [InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်ရန်", callback_data='movies_menu'), 
         InlineKeyboardButton("📱 Mod App များ", url='https://t.me/khantzip')],
        [InlineKeyboardButton("🎓 သင်တန်းများ", callback_data='courses_menu'), 
         InlineKeyboardButton("✅ ယုံကြည်ရသူများ", url='https://t.me/khantzip')],
        [InlineKeyboardButton("💎 Pro/Premium များ", url='https://t.me/khantzip'), 
         InlineKeyboardButton("📦 တခြားရရှိသောအရာများ", url='https://t.me/khantzip')],
        [InlineKeyboardButton("🤵 Admin နဲ့ စကားပြောမယ်", url='https://t.me/khantzip')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Start message ပို့ခြင်း
    if update.message:
        await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)
    else:
        await update.callback_query.message.edit_text(text=welcome_text, reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ဇာတ်ကားကြည့်ရန် Menu
    if query.data == 'movies_menu':
        movie_keyboard = [
            [InlineKeyboardButton("🎞 ဇာတ်ကားအစုံအဓိက channel", url='https://t.me/khantzipmainmovie')],
            [InlineKeyboardButton("🇨🇳 တရုတ်ဇာတ်ကား", url='https://t.me/khantzipchinamovies'),
             InlineKeyboardButton("🇰🇷 ကိုရီးယားဇာတ်ကား", url='https://t.me/khantzipkoreamovies')],
            [InlineKeyboardButton("🇮🇳 အိန္ဒိယဇာတ်ကား", url='https://t.me/khanzipindiamovie'),
             InlineKeyboardButton("🇹🇭 ထိုင်းဇာတ်ကား", url='https://t.me/khantzipthaimovie')],
            [InlineKeyboardButton("🐱 Anime/Cartoon/Animation", url='https://t.me/khantzipmovie')],
            [InlineKeyboardButton("🌍 နိုင်ငံခြားဇာတ်လမ်း", url='https://t.me/khantzipmovies')],
            [InlineKeyboardButton("🔙 နောက်သို့", callback_data='back_to_start')]
        ]
        await query.message.edit_text("ကြည့်ရှုလိုသည့် ဇာတ်ကားအမျိုးအစားကို ရွေးချယ်ပါ 👇", reply_markup=InlineKeyboardMarkup(movie_keyboard))

    # သင်တန်းများ Menu
    elif query.data == 'courses_menu':
        course_text = "သင်တန်းဈေးနှုန်းသိချင်ရင်သိချင်‌သောသင်တန်းကိုထပ်နှိပ်ကြည့်ပါ ထိုစာတန်းအောက်က‌buttonများကိုနှိပ်ကြည့်ပါ"
        course_keyboard = [
            [InlineKeyboardButton("💎 Mlbb diamondရောင်းနည်း", callback_data='price_10000')],
            [InlineKeyboardButton("📘 Facebook account သစ်ဖွင့်နည်း", callback_data='price_10000')],
            [InlineKeyboardButton("🇯🇵 Tiktok Japan accountဖွင့်နည်း", callback_data='price_10000')],
            [InlineKeyboardButton("📧 Gmail new accountနှင့် နိုင်ငံချိန်းနည်း", callback_data='price_20000')],
            [InlineKeyboardButton("🤵 Admin Account", url='https://t.me/khantzip')],
            [InlineKeyboardButton("🔙 နောက်သို့", callback_data='back_to_start')]
        ]
        await query.message.edit_text(text=course_text, reply_markup=InlineKeyboardMarkup(course_keyboard))

    # ဈေးနှုန်းပြသခြင်း
    elif query.data == 'price_10000':
        await query.message.reply_text("သင်တန်းကြေး - 10,000 MMK ပါခင်ဗျာ။ ✅\nAdmin သို့ ဆက်သွယ်ရန် - @khantzip")
    elif query.data == 'price_20000':
        await query.message.reply_text("သင်တန်းကြေး - 20,000 MMK ပါခင်ဗျာ။ ✅\nAdmin သို့ ဆက်သွယ်ရန် - @khantzip")
    
    # နောက်သို့ပြန်သွားခြင်း
    elif query.data == 'back_to_start':
        await start(update, context)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Khantzip Bot is running...")
    app.run_polling()
        
