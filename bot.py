import asyncio
from playwright.async_api import async_playwright
from telegram import Bot

TOKEN = "SIZNING_TOKENINGIZ"
CHAT_ID = "SIZNING_CHAT_ID"

bot = Bot(token=TOKEN)

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.taobao.com")
        await page.screenshot(path="screenshot.png")
        await browser.close()
        await bot.send_message(chat_id=CHAT_ID, text="✅ Sahifa ochildi va screenshot olindi.")

if __name__ == "__main__":
    asyncio.run(run())
