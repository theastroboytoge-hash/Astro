from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler, Filters
from telegram import InlineQueryResultCachedDocument
TOKEN = "8596547767:AAEU-sklvhsgDjGS2ewVi8n8UzQ0-5g7Q7U"
file_store = {}
def start(bot, update):
    update.message.reply_text("سلام! فایل بفرست.")
def handle_file(bot, update):
    if update.message.document:
        file_store['last_file'] = update.message.document.file_id
        update.message.reply_text("ذخیره شد!")
    else:
        update.message.reply_text("فایل بفرست.")
def inline_query(bot, update):
    if 'last_file' in file_store:
        results = [InlineQueryResultCachedDocument("1", "فایل", file_store['last_file'])]
        update.inline_query.answer(results)
updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.document, handle_file))
dp.add_handler(InlineQueryHandler(inline_query))
print("ربات روشن شد!")
updater.start_polling()
updater.idle()
