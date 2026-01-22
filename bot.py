import logging
import gspread
from google.oauth2.service_account import Credentials
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- CONFIGURATION ---
TOKEN = '8377346830:AAFVtsPT3BHAWS9Vtl6pjj2BanW9LnhGtII'
SHEET_NAME = 'Khantzip_Prices'
ADMIN_ID = 7072756798 

CREDENTIALS_DICT = {
  "type": "service_account",
  "project_id": "khantzipbot",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1rJIzLdSB6GYq\nEdqT+tYm3jDpSVLhmNzgZalkk5+A3PG8h73/t9Au/m7niM/fSFv6T+su7PBOgjlA\noT6JVWbu7MFnPOuW31rVYHwfYdJ7rLVuLANo+GOpwjX8ldZpo4h0znvqddiL3vPJ\nAm/Q2g+zkF+WWYjOKAm/c++xyVBcM2kkswwb9kCGt3UiKkRo2eykowZ6A+c7aBtJ\nln/MSvKDPfAk9LE+ANGpilYoxnguDj/lG3YfrCaeIj+swa5/jV2FkMh2qc/b4mxH\nK8LJJYbIzMsZilvkW/tKcRhPsIJGJIgf+aMFo5HuFFQH/NjJVh6bLKXMQ10SSMJS\n+heC0Ir7AgMBAAECggEAAWSZ2F+dFgPoqKDraqANPU4N1PQVeRpZczUEV/uTyQKo\nrdfimo/XvkyAIDFZ2q3s2p37QSha7VctRjQWTSpE+EcDcp2ydr0urp0nRnxTB1S7\nLWWT/x2MchRForKparTwymh85b7Skrv6ZYupvNG3NhrAyN/V3zLKZFfouhW/kn1l\nFae4Cd46sYwlxOE2pb35iRggccXEH+9GLVGJqwCCTI1UPMTY8UZ/ivuUtqrfdcle\naRwkjOgO7Q1Nxiqrf9UWztYNmZ78d4Z8I7XrQ2MRQ+Wf/9OQV/6ao7PhUtWe67cx\AdhfHhIbD96uHDil07fZ65WAHVXkyGzIAFb7SPE/jQKBgQD32YPTFGkOP7GqXYsQ\noqqdxvnLTDQnhxCQgvqErAs1A66ZI+GSaOt0+vhBBPJe9Sm+EEegnQPRKp1ocvSu\nS8o8/f3Hw3Fw6saCEfWDzxW8+rj/rNDdUayEwQiBK0h/3LhF1EFDPWF2AMne0HTf\LrdmIKv/PfFvAgeLatCt0XA4RQKBgQC7pfeX/4TCT8OoHILp7Rh++Vf0KV+4uXzu\nEmiIepYxn1XhBBaUMtpbrDcLlqqDXKQ3NRY8ZQ3M3JqUwdpqrTi9OXGqg4rbf0VZ\n7uCr2AO9FjiHLss9FBztVnQKK0/vZAQ3lB/P5CoY4fWk5qbFtUaDyH087ZVfQSEo\nEjNIngAKPwKBgFobGBPbLb5iZaL8Uxx/JuwpdJL2Z1efgOQo2g71xTVG22kNZGqn\n/kIPI8XvmHXxR3Wz0XaQ3txiU8uvT0k2gJXf+S1w3oMgt35+LPX4iXyk4jEBkQWF\nNeUlkIP1SmxBwDSS0A8z94TBEKMSwgqJn19frWgkCuxCnp+O+8LVi6jJAoGBAJML\nb4YwuTv7fXsTPJNLNFLr2bx/X39F+1wkGL46MdAY6Bc4OOlRIEOOJGR0YJIn2pdY\nhmA1YCcVCB1h+2J08210wlm4UuvGQ/ZBdtWypNtbulhUlvb59+EUSkJdxnn1ikhz\nTqp+RW7SQshB5pYvg15pkZpZIyBNzUm1WXKiPa3JAoGBAO6lui/KTsKEFcAeFLZr\nBbiP/JgKZ4l6C08sGQY++b5BjGYRnrEeMenT0uL54Z4jGG2lsvpZO97KQHoIs6b1\n9AwpCvSLsINDBPsXJzjqIp/IUtQDC/8/dsY5dO0iXBsyb9pnRPc6uVIL8ywgOAXO\nJwfxeJTFF51lp5Flm6zc9QNJ\n-----END PRIVATE KEY-----\n",
  "client_email": "khant-bot@khantzipbot.iam.gserviceaccount.com"
}

def get_sheet_data():
    try:
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(CREDENTIALS_DICT, scopes=scope)
        client = gspread.authorize(creds)
        # Tab နာမည်ကို အတိအကျ စစ်ဆေးဖတ်ရှုခြင်း
        sheet = client.open(SHEET_NAME).worksheet(SHEET_NAME)
        return sheet.get_all_records()
    except Exception as e:
        logging.error(f"Sheet Error: {e}")
        return []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "မင်္ဂလာရှိအပေါင်းနဲ့ ပြည့်စုံသောနေ့လေးတစ်နေ့ပါ Khant Zip ခင်ဗျာ ✨\n\n"
        "Khantzip bot ကနေ ကြိုဆိုပါတယ် ✨\n"
        "ကိုယ်သိချင်တာကို အားမနာတမ်း အောက်မှာ ရွေးချယ်ပါ 👇"
    )
    keyboard = [
        [InlineKeyboardButton("🎬 ဇာတ်ကားကြည့်ရန်", url='https://t.me/khantzip'), InlineKeyboardButton("📱 Mod App များ", url='https://t.me/khantzip')],
        [InlineKeyboardButton("✅ ယုံကြည်ရသူများ", callback_data='trusted'), InlineKeyboardButton("💎 Pro/Premium များ", callback_data='premium')],
        [InlineKeyboardButton("🤵 Admin နဲ့ စကားပြောမယ်", url='https://t.me/khantzip')]
    ]
    if update.effective_user.id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("⚙️ Admin Settings", callback_data='admin_panel')])

    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message: await update.message.reply_text(text, reply_markup=reply_markup)
    else: await update.callback_query.message.edit_text(text, reply_markup=reply_markup)

async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'premium':
        data = get_sheet_data()
        if not data:
            await query.message.edit_text("⚠️ Google Sheet ထဲက Tab နာမည်ကို 'Khantzip_Prices' လို့ မှန်အောင်ပေးပြီး Share ပေးထားပါဦးဗျ။", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data='back')]]))
            return
        kb = [[InlineKeyboardButton(row['Item'], callback_data=f"info_{row['Item']}")] for row in data if row.get('Item')]
        kb.append([InlineKeyboardButton("🔙 နောက်သို့", callback_data='back')])
        await query.message.edit_text("သိလိုသော အမျိုးအစားကို ရွေးပါ 👇", reply_markup=InlineKeyboardMarkup(kb))

    elif query.data == 'admin_panel':
        await query.message.edit_text("🛠 Admin Panel ကြိုဆိုပါတယ်\n\n- Sheet ထဲမှာ စာသားတွေပြင်လိုက်ရင် Bot မှာ လိုက်ပြောင်းပါမယ်။\n- Image_URL ထဲမှာ Link ထည့်ရင် ပုံပါပြပါမယ်။", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data='back')]]))

    elif query.data.startswith('info_'):
        item_name = query.data.replace('info_', '')
        data = get_sheet_data()
        for row in data:
            if str(row.get('Item')) == item_name:
                info_text = f"✨ {row['Item']} ✨\n\n{row['Information']}\n\nAdmin 👉 @khantzip"
                img_url = row.get('Image_URL')
                if img_url and img_url.startswith('http'):
                    await query.message.reply_photo(photo=img_url, caption=info_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙", callback_data='premium')]]))
                else:
                    await query.message.edit_text(info_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙", callback_data='premium')]]))

    elif query.data == 'back': await start(update, context)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_click))
    app.run_polling()
      
