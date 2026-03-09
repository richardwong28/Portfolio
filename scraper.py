import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

class PriceScraper: #scrap
    def __init__(self):
        self.results = []

    async def fetch_data(self, url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(channel="msedge", headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            await Stealth().apply_stealth_async(page)

            print(f"Mengunjungi: {url}")
            await page.goto(url, wait_until="networkidle")

            # Ambil data (contoh selektor umum)
            cards = await page.query_selector_all(".product_pod")  # ← selector yang benar
            for card in cards:
                link = await card.query_selector("h3 a")
                title = await link.get_attribute("title")
                price = await card.query_selector(".product_price .price_color")
    
                self.results.append({
                "nama": title if title else "N/A",
                "harga_raw": await price.inner_text() if price else "0"
                })

            await browser.close()
            return self.results   
    