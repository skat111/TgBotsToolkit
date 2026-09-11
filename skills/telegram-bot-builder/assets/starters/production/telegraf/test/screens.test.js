import assert from "node:assert/strict";
import test from "node:test";
import { screen } from "../src/index.js";

test("all routes render", () => {
  for (const route of ["home", "profile", "settings", "catalog", "product", "confirm"]) {
    const view = screen(route, "Иван");
    assert.ok(view.html);
    assert.ok(view.keyboard.reply_markup.inline_keyboard.length);
  }
});

test("user name is HTML escaped", () => {
  assert.match(screen("profile", "<Иван & Co>").html, /&lt;Иван &amp; Co&gt;/);
});
