import { createServer } from "node:http";
import { pathToFileURL } from "node:url";
import { Bot, InlineKeyboard, webhookCallback } from "grammy";

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
  const keyboard = new InlineKeyboard();
  for (const rawRow of rows) {
    const row = Array.isArray(rawRow[0]) ? rawRow : [rawRow];
    for (const [label, data] of row) keyboard.text(label, data);
    keyboard.row();
  }
  return { html, keyboard };
}

export function createBot(botToken) {
  const bot = new Bot(botToken);
  bot.command("start", async (ctx) => {
    const view = screen("home", [ctx.from?.first_name, ctx.from?.last_name].filter(Boolean).join(" "));
    const options = { parse_mode: "HTML", reply_markup: view.keyboard };
    if (menuPhoto) await ctx.replyWithPhoto(menuPhoto, { caption: view.html, ...options });
    else await ctx.reply(view.html, options);
  });
  bot.callbackQuery(/^nav:(.+)$/, async (ctx) => {
    await ctx.answerCallbackQuery();
    const view = screen(ctx.match[1], [ctx.from?.first_name, ctx.from?.last_name].filter(Boolean).join(" "));
    const options = { parse_mode: "HTML", reply_markup: view.keyboard };
    if (ctx.callbackQuery.message?.photo) await ctx.editMessageCaption({ caption: view.html, ...options });
    else await ctx.editMessageText(view.html, options);
  });
  bot.callbackQuery(/^settings:/, (ctx) => ctx.answerCallbackQuery({ text: "Настройка сохранена" }));
  bot.callbackQuery("confirm:order", (ctx) => ctx.answerCallbackQuery({ text: "Демо: подключите серверную оплату", show_alert: true }));
  bot.catch((error) => console.error("Bot error", error.error));
  return bot;
}

async function main() {
  if (!token) throw new Error("BOT_TOKEN is required");
  const bot = createBot(token);
  if (webhookBaseUrl) {
    if (!webhookSecret) throw new Error("WEBHOOK_SECRET is required in webhook mode");
    await bot.init();
    await bot.api.setWebhook(webhookBaseUrl + webhookPath, { secret_token: webhookSecret });
    const handleWebhook = webhookCallback(bot, "http", { secretToken: webhookSecret });
    createServer((request, response) => {
      if (request.method === "GET" && request.url === "/health") {
        response.writeHead(200, { "content-type": "application/json" });
        response.end('{"status":"ok"}');
        return;
      }
      if (request.url !== webhookPath) {
        response.writeHead(404).end();
        return;
      }
      handleWebhook(request, response);
    }).listen(port, "0.0.0.0");
  } else {
    bot.start();
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) main();
