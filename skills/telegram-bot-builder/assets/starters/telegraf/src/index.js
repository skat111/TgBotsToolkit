import { Markup, Telegraf } from "telegraf";
import { pathToFileURL } from "node:url";

const token = process.env.BOT_TOKEN;
const menuPhoto = process.env.MENU_PHOTO;
const customEmoji = process.env.CUSTOM_EMOJI_ENABLED?.toLowerCase() === "true";
const webhookBaseUrl = process.env.WEBHOOK_BASE_URL?.replace(/\/$/, "");
const webhookPath = process.env.WEBHOOK_PATH || "/telegram/webhook";
const webhookSecret = process.env.WEBHOOK_SECRET;
const port = Number(process.env.PORT || 8080);

const escapeHtml = (value = "") => value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
const icons = { profile: ["👤", "5814247475141153332"], settings: ["⚙", "5877260593903177342"], catalog: ["📁", "5875206779196935950"], warning: ["⚠️", "5881702736843511327"] };
const icon = (role) => {
  const [fallback, id] = icons[role];
  return customEmoji ? `<tg-emoji emoji-id="${id}">${fallback}</tg-emoji>` : fallback;
};

export function screen(name, userName = "") {
  const safeName = escapeHtml(userName);
  const screens = {
    home: [`<b>Красивый бот</b>\n<blockquote>Все важные действия находятся в одном меню.</blockquote>\n\nРады видеть, ${safeName || "вас"}!`, [["Открыть каталог", "nav:catalog"], [["Профиль", "nav:profile"], ["Настройки", "nav:settings"]]]],
    profile: [`<b>${icon("profile")} Профиль</b>\n\nИмя: <b>${safeName || "не указано"}</b>\n<blockquote>Здесь появятся данные аккаунта и история.</blockquote>`, [["← Назад", "nav:home"]]],
    settings: [`<b>${icon("settings")} Настройки</b>\n\nЯзык: <b>Русский</b>\nУведомления: <b>Включены</b>`, [["Язык · RU", "settings:language"], ["Уведомления · Вкл", "settings:notifications"], ["← Назад", "nav:home"]]],
    catalog: [`<b>${icon("catalog")} Каталог</b>\n<i>2 предложения</i>\n\nВыберите карточку:`, [["Базовый · 490 ₽", "nav:product"], ["Премиум · 990 ₽", "nav:product"], ["← Назад", "nav:home"]]],
    product: ["<b>Премиум</b>\nПолный набор возможностей.\n\n<b>990 ₽</b>\n<blockquote expandable>Подробности предложения и условия использования.</blockquote>", [["Выбрать · 990 ₽", "nav:confirm"], [["← К списку", "nav:catalog"], ["Главное меню", "nav:home"]]]],
    confirm: [`<b>${icon("warning")} Подтвердите действие</b>\n\nВы собираетесь оформить заказ.\n<blockquote>Перед подключением оплаты перечитайте цену на сервере.</blockquote>`, [["Отмена", "nav:product"], ["Подтвердить заказ", "confirm:order"]]],
  };
  const [html, rows] = screens[name] ?? screens.home;
  const normalized = rows.map((row) => Array.isArray(row[0]) ? row : [row]);
  return { html, keyboard: Markup.inlineKeyboard(normalized.map((row) => row.map(([label, data]) => Markup.button.callback(label, data)))) };
}

export function createBot(botToken) {
  const bot = new Telegraf(botToken);
  bot.start(async (ctx) => {
    const view = screen("home", [ctx.from?.first_name, ctx.from?.last_name].filter(Boolean).join(" "));
    const extra = { parse_mode: "HTML", ...view.keyboard };
    if (menuPhoto) await ctx.replyWithPhoto(menuPhoto, { caption: view.html, ...extra });
    else await ctx.reply(view.html, extra);
  });
  bot.action(/^nav:(.+)$/, async (ctx) => {
    await ctx.answerCbQuery();
    const view = screen(ctx.match[1], [ctx.from?.first_name, ctx.from?.last_name].filter(Boolean).join(" "));
    const extra = { parse_mode: "HTML", ...view.keyboard };
    if (ctx.callbackQuery.message?.photo) await ctx.editMessageCaption(view.html, extra);
    else await ctx.editMessageText(view.html, extra);
  });
  bot.action(/^settings:/, (ctx) => ctx.answerCbQuery("Настройка сохранена"));
  bot.action("confirm:order", (ctx) => ctx.answerCbQuery("Демо: подключите серверную оплату", { show_alert: true }));
  bot.catch((error) => console.error("Bot error", error));
  return bot;
}

async function main() {
  if (!token) throw new Error("BOT_TOKEN is required");
  const bot = createBot(token);
  if (webhookBaseUrl) {
    if (!webhookSecret) throw new Error("WEBHOOK_SECRET is required in webhook mode");
    await bot.launch({ webhook: { domain: webhookBaseUrl, port, hookPath: webhookPath, secretToken: webhookSecret } });
  } else {
    await bot.launch();
  }
  const stop = (signal) => bot.stop(signal);
  process.once("SIGINT", () => stop("SIGINT"));
  process.once("SIGTERM", () => stop("SIGTERM"));
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) main();
