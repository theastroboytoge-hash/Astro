from telegram.ext import Updater, CommandHandler, MessageHandler, InlineQueryHandler, Filters
from telegram import InlineQueryResultCachedDocument
TOKEN = "8596547767:AAEU-sklvhsgDjGS2ewVi8n8UzQ0-5g7Q7U"
file_store = {}
def start(bot, update):
    update.message.reply_text("سلام! برای ذخیره فایل با اسم از /save [اسم] استفاده کن. مثال: /save logo")
def save_file(bot, update, args):
    if not args:
        update.message.reply_text("لطفاً یک اسم برای فایل وارد کن: /save [اسم]")
        return
    file_name = args[0]
    file_store[file_name] = {'waiting': True, 'user': update.message.from_user.id}
    update.message.reply_text(f"حالا فایل رو برای اسم '{file_name}' بفرست.")
def handle_file(bot, update):
    user_id = update.message.from_user.id
    for name, data in file_store.items():
        if data.get('waiting') and data.get('user') == user_id:
            if update.message.document:
                file_store[name]['file_id'] = update.message.document.file_id
                file_store[name]['waiting'] = False
                update.message.reply_text(f"فایل با اسم '{name}' ذخیره شد!")
                return
            elif update.message.photo:
                file_store[name]['file_id'] = update.message.photo[-1].file_id
                file_store[name]['waiting'] = False
                update.message.reply_text(f"عکس با اسم '{name}' ذخیره شد!")
                return
            elif update.message.video:
                file_store[name]['file_id'] = update.message.video.file_id
                file_store[name]['waiting'] = False
                update.message.reply_text(f"ویدیو با اسم '{name}' ذخیره شد!")
                return
            elif update.message.audio:
                file_store[name]['file_id'] = update.message.audio.file_id
                file_store[name]['waiting'] = False
                update.message.reply_text(f"آهنگ با اسم '{name}' ذخیره شد!")
                return
    update.message.reply_text("اول با دستور /save [اسم] شروع کن، بعد فایل رو بفرست.")
def inline_query(bot, update):
    query = update.inline_query.query.strip()
    if not query:
        update.inline_query.answer([])
        return
    results = []
    for name, data in file_store.items():
        if 'file_id' in data and query.lower() in name.lower():
            results.append(InlineQueryResultCachedDocument(id=name, title=f"📁 {name}", document_file_id=data['file_id'], description="ارسال فایل ذخیره‌شده"))
    if results:
        update.inline_query.answer(results[:50])
    else:
        update.inline_query.answer([])
updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("save", save_file, pass_args=True))
dp.add_handler(MessageHandler(Filters.all & ~Filters.command, handle_file))
dp.add_handler(InlineQueryHandler(inline_query))
print("ربات روشن شد!")
updater.start_polling()
updater.idle()
