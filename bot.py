from telegram import Update, InlineQueryResultCachedDocument
from telegram.ext import Application, CommandHandler, MessageHandler, InlineQueryHandler, filters, ContextTypes

TOKEN = "8743941600:AAEnpafnAFN4yuzvo84gO4Ex9unnj1xnzv0"

file_store = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! یه فایل برام بفرست تا ذخیره کنم. بعداً با @YourBotUsername در هر چتی می‌تونی بفرستیش.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.photo or update.message.video or update.message.audio
    if file:
        file_id = file.file_id
        file_name = file.file_name if hasattr(file, 'file_name') else "file"
        file_store['last_file'] = file_id
        await update.message.reply_text(f"فایل '{file_name}' با موفقیت ذخیره شد! حالا با @YourBotUsername در حالت اینلاین بفرستش.")
    else:
        await update.message.reply_text("لطفاً یه فایل برام بفرست.")

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'last_file' in file_store:
        results = [
            InlineQueryResultCachedDocument(
                id="1",
                title="ارسال فایل ذخیره‌شده",
                document_file_id=file_store['last_file'],
                description="همین فایل رو بدون آپلود مجدد بفرست"
            )
        ]
        await update.inline_query.answer(results)
    else:
        await update.inline_query.answer([])

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_file))
    app.add_handler(InlineQueryHandler(inline_query))
    print("ربات روشن شد!")
    app.run_polling()

if __name__ == "__main__":
    main()
