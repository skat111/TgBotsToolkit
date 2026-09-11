import unittest

import bot


class ScreenTests(unittest.TestCase):
    def test_all_routes_render(self):
        for route in ("home", "profile", "settings", "catalog", "product", "confirm"):
            text, markup = bot.screen(route, "Иван")
            self.assertTrue(text)
            self.assertTrue(markup.inline_keyboard)

    def test_user_name_is_html_escaped(self):
        text, _ = bot.screen("profile", "<Иван & Co>")
        self.assertIn("&lt;Иван &amp; Co&gt;", text)


if __name__ == "__main__":
    unittest.main()
