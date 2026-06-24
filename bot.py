from telegram import InlineQueryResultCachedDocument
from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler, Filters

TOKEN = "8596547767:AAEU-sklvhsgDjGS2ewVi8n8UzQ0-5g7Q7U"

file_store = {}

def start(bot, update):
    update.message.reply_text("سلام! یه فایل برام بفرست تا ذخیره کنم.")

def handle_file(bot, update):
    file = update.message.document or update.message.photo or update.message.video or update.message.audio
    if file:
        file_id = file.file_id
        file_store['last_file'] = file_id
        update.message.reply_text("فایل ذخیره شد! حالا در هر چتی @YourBotUsername رو تایپ کن و فایل رو بفرست.")
    else:
        update.message.reply_text("لطفاً یه فایل برام بفرست.")

def inline_query(bot, update):
    if 'last_file' in file_store:
        results = [
            InlineQueryResultCachedDocument(
                id="1",
                title="ارسال فایل ذخیره‌شده",
                document_file_id=file_store['last_file'],
                description="همین فایل رو بدون آپلود مجدد بفرست"
            )
        ]
        update.inline_query.answer(results)
    else:
        update.inline_query.answer([])

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all, handle_file))
    dp.add_handler(InlineQueryHandler(inline_query))
    
    print("ربات روشن شد!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all, handle_file))
    dp.add_handler(InlineQueryHandler(inline_query))
    
    print("ربات روشن شد!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all & ~Filters.command, handle_file))
    dp.add_handler(InlineQueryHandler(inline_query))
    
    print("ربات روشن شد!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all & ~Filters.command, handle_file))
    dp.add_handler(InlineQueryHandler(inline_query))
    
    print("ربات روشن شد!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_file))
    app.add_handler(InlineQueryHandler(inline_query))
    print("ربات روشن شد!")
    app.run_polling()

if __name__ == "__main__":
    main()
