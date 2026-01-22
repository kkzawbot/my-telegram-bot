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
    
    # Admin Panel ကို သင့်အတွက်ပဲ ပေါ်အောင် လုပ်ထားပေးသည်
    if update.effective_user.id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("⚙️ Admin Settings", callback_data='admin_panel')])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ဇာတ်ကားကြည့်ရန် Menu
    if query.data == 'movies_menu':
        movie_keyboard = [
            [InlineKeyboardButton("🎞 ဇာတ်ကားအစုံအဓိက channel", url='https://t.me/khantzipmainmovie')],
            [InlineKeyboardButton("🇨🇳 တရုတ်ဇာတ်ကား", url='https://t.me/khantzipchinamovies'),
             InlineKeyboardButton("🇰🇷 ကိုရီးယားဇာတ်ကား", url='
                                  
