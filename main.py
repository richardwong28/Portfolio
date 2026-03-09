import asyncio
import os
from scraper import PriceScraper
from processor import clean_and_save
import logging

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/scraper.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    print("--- MEMULAI PROYEK SCRAPING ---")
    scraper = PriceScraper()
    
    try:
        raw_data = await scraper.fetch_data("https://books.toscrape.com/")
        
        path = clean_and_save(raw_data, "laporan_harga_buku")

        print(f"Selesai! Data disimpan di: {path}")
        logging.info("Scraping berhasil diselesaikan.")

    except Exception as e:
        print(f"Terjadi error, cek folder logs!")
        logging.error(f"Error utama: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())