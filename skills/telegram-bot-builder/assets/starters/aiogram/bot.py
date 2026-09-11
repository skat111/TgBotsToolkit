import asyncio
from html import escape
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

TOKEN = os.environ.get("BOT_TOKEN")
MENU_PHOTO = os.environ.get("MENU_PHOTO")
CUSTOM_EMOJI = os.environ.get("CUSTOM_EMOJI_ENABLED", "false").lower() == "true"
WEBHOOK_BASE_URL = os.environ.get("WEBHOOK_BASE_URL", "").rstrip("/")
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH", "/telegram/webhook")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")
PORT = int(os.environ.get("PORT", "8080"))

ICONS = {
    "profile": ("👤", "5814247475141153332"),
    "settings": ("⚙", "5877260593903177342"),
    "catalog": ("📁", "5875206779196935950"),
    "warning": ("⚠️", "5881702736843511327"),
}


def icon(role: str) -> str:
    fallback, emoji_id = ICONS[role]
    return f'<tg-emoji emoji-id="{emoji_id}">{fallback}</tg-emoji>' if CUSTOM_EMOJI else fallback


def keyboard(rows: list[list[tuple[str, str]]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, callback_data=data) for text, data in row] for row in rows
    ])


def screen(name: str, user_name: str = "") -> tuple[str, InlineKeyboardMarkup]:
    safe_name = escape(user_name)
    screens = {
        "home": (
            f"<b>Красивый бот</b>\n<blockquote>Все важные действия находятся в одном меню.</blockquote>\n\nРады видеть, {safe_name or 'вас'}!",
            [[("Открыть каталог", "nav:catalog")], [("Профиль", "nav:profile"), ("Настройки", "nav:settings")]],
        ),
        "profile": (
            f"<b>{icon('profile')} Профиль</b>\n\nИмя: <b>{safe_name or 'не указано'}</b>\n<blockquote>Здесь появятся данные аккаунта и история.</blockquote>",
            [[("← Назад", "nav:home"), ("Главное меню", "nav:home")]],
        ),
        "settings": (
            f"<b>{icon('settings')} Настройки</b>\n\nЯзык: <b>Русский</b>\nУведомления: <b>Включены</b>",
            [[("Язык · RU", "settings:language")], [("Уведомления · Вкл", "settings:notifications")], [("← Назад", "nav:home")]],
        ),
        "catalog": (
            f"<b>{icon('catalog')} Каталог</b>\n<i>2 предложения</i>\n\nВыберите карточку:",
            [[("Базовый · 490 ₽", "nav:product")], [("Премиум · 990 ₽", "nav:product")], [("← Назад", "nav:home")]],
        ),
        "product": (
            "<b>Премиум</b>\nПолный набор возможностей.\n\n<b>990 ₽</b>\n<blockquote expandable>Подробности предложения и условия использования.</blockquote>",
            [[("Выбрать · 990 ₽", "nav:confirm")], [("← К списку", "nav:catalog"), ("Главное меню", "nav:home")]],
        ),
        "confirm": (
            f"<b>{icon('warning')} Подтвердите действие</b>\n\nВы собираетесь оформить заказ.\n<blockquote>Перед подключением оплаты перечитайте цену на сервере.</blockquote>",
            [[("Отмена", "nav:product")], [("Подтвердить заказ", "confirm:order")]],
        ),
    }
    text, rows = screens.get(name, screens["home"])
    return text, keyboard(rows)


async def show(message: Message, name: str, user_name: str) -> None:
    text, markup = screen(name, user_name)
    if message.photo:
        await message.edit_caption(caption=text, reply_markup=markup)
    else:
        await message.edit_text(text=text, reply_markup=markup)


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    text, markup = screen("home", message.from_user.full_name if message.from_user else "")
    if MENU_PHOTO:
        await message.answer_photo(MENU_PHOTO, caption=text, reply_markup=markup)
    else:
        await message.answer(text, reply_markup=markup)


@dp.callback_query(F.data.startswith("nav:"))
async def navigate(query: CallbackQuery) -> None:
    await query.answer()
    if query.message:
        await show(query.message, query.data.split(":", 1)[1], query.from_user.full_name)


@dp.callback_query(F.data.startswith("settings:"))
async def setting(query: CallbackQuery) -> None:
    await query.answer("Настройка сохранена")


@dp.callback_query(F.data == "confirm:order")
async def confirm(query: CallbackQuery) -> None:
    await query.answer("Демо: подключите серверную оплату", show_alert=True)


async def main() -> None:
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is required")
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


def run_webhook() -> None:
    from aiohttp import web
    from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    app = web.Application()

    async def startup(_: web.Application) -> None:
        await bot.set_webhook(WEBHOOK_BASE_URL + WEBHOOK_PATH, secret_token=WEBHOOK_SECRET)

    async def health(_: web.Request) -> web.Response:
        return web.json_response({"status": "ok"})

    app.on_startup.append(startup)
    app.router.add_get("/health", health)
    SimpleRequestHandler(dp, bot, secret_token=WEBHOOK_SECRET).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    if WEBHOOK_BASE_URL:
        if not TOKEN or not WEBHOOK_SECRET:
            raise RuntimeError("BOT_TOKEN and WEBHOOK_SECRET are required in webhook mode")
        run_webhook()
    else:
        asyncio.run(main())
