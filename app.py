from telegram.ext import Updater, CommandHandler
import logging

logger = logging.getLogger(__name__)

TOKEN = '540596573:AAFRPD64sPWVP04tNzNpCAARj13L7dYpF1k'
REQUEST_KWARGS = {
    'proxy_url': "socks5://127.0.0.1:9050",
    'urllib3_proxy_kwargs': {}
}


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


def start_app():
    logging.info("Start app")

    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    start_app()
