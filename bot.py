import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURATION ---
TOKEN = '8377346830:AAFVtsPT3BHAWS9Vtl6pjj2BanW9LnhGtII'
ADMIN_ID = 5334758537  # <--- ဒီနေရာမှာ @userinfobot ကရတဲ့ သင့် ID ကို အစားထိုးပါ

# ခလုတ်များ၏ အချက်အလက်များ
buttons_data = {
    "btn_1": {"name": "🎬 ဇာတ်ကားကြည့်မယ်", "text": "ဇာတ်ကားကြည့်ရန် အောက်ပါလင့်ကို နှိပ်ပါ", "url": "https://t.me/khantzip"},
    "btn_2": {"name": "📚 သင်တန်းများ", "text": "လက်ရှိတက်ရောက်နိုင်သော သင်တန်းများမှာ...", "url": "https://t.me/khantzip"},
    "btn_3": {"name": "👨‍💻 Admin ဆက်သွယ်ရန်", "text": "အကူအညီလိုအပ်ပါက မေးမြန်းနိုင်ပါသည်", "url": "https://t.me/khantzip"}
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for key, data in buttons_data.items():
        keyboard.append([InlineKeyboardButton(data["name"], url=data["url"])])
    
    if update.effective_user.id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("⚙️ Admin Panel (ခလုတ်ပြင်ရန်)", callback_data='admin_panel')])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Khantzip Bot မှ ကြိုဆိုပါတယ်ဗျာ။", reply_markup=reply_markup)

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton(f"ပြင်မယ်: {data['name']}", callback_data=f"setup_{key}")] for key, data in buttons_data.items()]
    await query.message.edit_text("ဘယ်ခလုတ်ကို ပြင်ချင်ပါသလဲ?", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    btn_key = query.data.replace('setup_', '')
    context.user_data['editing_btn'] = btn_key
    await query.message.reply_text(f"ယခု '{buttons_data[btn_key]['name']}' ကို ပြင်နေပါသည်။\n\nပုံစံ: ခလုတ်နာမည် | ပေါ်မယ့်စာ | လင့်ခ်")

async def update_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID and 'editing_btn' in context.user_data:
        try:
            btn_key = context.user_data['editing_btn']
            new_data = update.message.text.split('|')
            buttons_data[btn_key]['name'], buttons_data[btn_key]['text'], buttons_data[btn_key]['url'] = [i.strip() for i in new_data]
            del context.user_data['editing_btn']
            await update.message.reply_text("✅ အောင်မြင်စွာ ပြင်ဆင်ပြီးပါပြီ။")
        except:
            await update.message.reply_text("❌ ပုံစံမမှန်ပါ။ နာမည် | စာ | လင့်ခ် ပုံစံအတိုင်း ပို့ပေးပါ။")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(admin_panel, pattern='^admin_panel$'))
    app.add_handler(CallbackQueryHandler(handle_setup, pattern='^setup_'))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), update_button))
    app.run_polling()
    
