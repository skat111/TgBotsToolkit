from html import escape
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
MENU_PHOTO = os.environ.get("MENU_PHOTO")
CUSTOM_EMOJI = os.environ.get("CUSTOM_EMOJI_ENABLED", "false").lower() == "true"
WEBHOOK_BASE_URL = os.environ.get("WEBHOOK_BASE_URL", "").rstrip("/")
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH", "/telegram/webhook")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")
PORT = int(os.environ.get("PORT", "8080"))
ICONS = {"profile": ("👤", "5814247475141153332"), "settings": ("⚙", "5877260593903177342"), "catalog": ("📁", "5875206779196935950"), "warning": ("⚠️", "5881702736843511327")}


def icon(role: str) -> str:
    fallback, emoji_id = ICONS[role]
    return f'<tg-emoji emoji-id="{emoji_id}">{fallback}</tg-emoji>' if CUSTOM_EMOJI else fallback


def screen(name: str, user_name: str = "") -> tuple[str, InlineKeyboardMarkup]:
    safe_name = escape(user_name)
    screens = {
        "home": (f"<b>Красивый бот</b>\n<blockquote>Все важные действия находятся в одном меню.</blockquote>\n\nРады видеть, {safe_name or 'вас'}!", [[("Открыть каталог", "nav:catalog")], [("Профиль", "nav:profile"), ("Настройки", "nav:settings")]]),
        "profile": (f"<b>{icon('profile')} Профиль</b>\n\nИмя: <b>{safe_name or 'не указано'}</b>\n<blockquote>Здесь появятся данные аккаунта и история.</blockquote>", [[("← Назад", "nav:home")]]),
        "settings": (f"<b>{icon('settings')} Настройки</b>\n\nЯзык: <b>Русский</b>\nУведомления: <b>Включены</b>", [[("Язык · RU", "settings:language")], [("Уведомления · Вкл", "settings:notifications")], [("← Назад", "nav:home")]]),
        "catalog": (f"<b>{icon('catalog')} Каталог</b>\n<i>2 предложения</i>\n\nВыберите карточку:", [[("Базовый · 490 ₽", "nav:product")], [("Премиум · 990 ₽", "nav:product")], [("← Назад", "nav:home")]]),
        "product": ("<b>Премиум</b>\nПолный набор возможностей.\n\n<b>990 ₽</b>\n<blockquote expandable>Подробности предложения и условия использования.</blockquote>", [[("Выбрать · 990 ₽", "nav:confirm")], [("← К списку", "nav:catalog"), ("Главное меню", "nav:home")]]),
        "confirm": (f"<b>{icon('warning')} Подтвердите действие</b>\n\nВы собираетесь оформить заказ.\n<blockquote>Перед подключением оплаты перечитайте цену на сервере.</blockquote>", [[("Отмена", "nav:product")], [("Подтвердить заказ", "confirm:order")]]),
    }
    text, rows = screens.get(name, screens["home"])
    return text, InlineKeyboardMarkup([[InlineKeyboardButton(label, callback_data=data) for label, data in row] for row in rows])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    user = update.effective_user
    text, markup = screen("home", user.full_name if user else "")
    if MENU_PHOTO:
        await message.reply_photo(MENU_PHOTO, caption=text, parse_mode=ParseMode.HTML, reply_markup=markup)
    else:
        await message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)


async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = query.data or ""
    if data.startswith("settings:"):
        await query.answer("Настройка сохранена")
        return
    if data == "confirm:order":
        await query.answer("Демо: подключите серверную оплату", show_alert=True)
        return
    await query.answer()
    name = data.split(":", 1)[1] if data.startswith("nav:") else "home"
    text, markup = screen(name, query.from_user.full_name)
    if query.message.photo:
        await query.edit_message_caption(caption=text, parse_mode=ParseMode.HTML, reply_markup=markup)
    else:
        await query.edit_message_text(text=text, parse_mode=ParseMode.HTML, reply_markup=markup)


def main() -> None:
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is required")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback))
    if WEBHOOK_BASE_URL:
        if not WEBHOOK_SECRET:
            raise RuntimeError("WEBHOOK_SECRET is required in webhook mode")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=WEBHOOK_PATH.lstrip("/"),
            webhook_url=WEBHOOK_BASE_URL + WEBHOOK_PATH,
            secret_token=WEBHOOK_SECRET,
            allowed_updates=Update.ALL_TYPES,
        )
    else:
        app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
