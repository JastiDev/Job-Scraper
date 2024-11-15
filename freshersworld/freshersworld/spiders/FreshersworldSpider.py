import logging
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv
import json
import pandas as pd

class FreshersworldSpider(scrapy.Spider):
    name = "freshersworld_spider"
    start_urls = ['https://www.freshersworld.com/jobs/category/work-from-home-job-vacancies']
    max_pages = 5  # Limit the number of pages to scrape
    page_counter = 0
    all_data = []

    def start_requests(self):
        yield SeleniumRequest(
            url=self.start_urls[0],
            callback=self.parse,
            wait_time=2,
            wait_until=lambda driver: driver.find_element(By.CSS_SELECTOR, "div.job-container")
        )

    def parse(self, response):
        # Initialize Chrome options
        options = Options()
        options.add_argument("--headless")  # Uncomment if you want to run in headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Initialize the Chrome driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Navigate to the URL
        driver.get(response.url)
        time.sleep(2)  # Wait for the page to load

        # Extract data from the first page
        self.extract_and_save_data(driver)

        # Handle pagination and navigate through the pages
        while self.page_counter < self.max_pages:
            try:
                # Find the "Next" button and click it
                next_page = driver.find_element(By.CSS_SELECTOR, "li.next a")
                driver.execute_script("arguments[0].click();", next_page)
                self.page_counter += 1
                time.sleep(3)  # Wait for the page to load

                # Extract data from the current page
                self.extract_and_save_data(driver)

            except Exception as e:
                self.logger.error(f"Error during pagination: {e}")
                break

        # Close the driver after scraping
        driver.quit()

        # Save data to CSV, Excel, and JSON
        if self.all_data:
            self.save_data(self.all_data)

    def extract_and_save_data(self, driver):
        # Get the page source and parse it with BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Extract job details from the current page
        job_listings = soup.select('div.job-container')  # Adjusted to match the outer job container

        for job in job_listings:
            title = job.select_one('span.wrap-title').get_text(strip=True)  # Title selector
            company = job.select_one('h3.company-name').get_text(strip=True)  # Company name selector
            location = ', '.join([loc.get_text(strip=True) for loc in job.select('span.job-location a')])  # Combined location selector
            description = job.select_one('span.desc').get_text(strip=True)  # Description selector
            experience = job.select_one('span.experience').get_text(strip=True)  # Experience
            salary = job.select_one('span.qualifications').get_text(strip=True)  # Salary
            link = job.select_one('div.job-desc-block a')['href']  # Link to job details
            posted_on = job.select_one('div.text-ago .ago-text').get_text(strip=True) if job.select_one('div.text-ago .ago-text') else 'N/A'
            # Create a job item dictionary
            job_item = {
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'experience': experience,
                'salary': salary,
                'link': link,
                'posted_on': posted_on 
            }

            self.all_data.append(job_item)

        self.logger.info(f"Page {self.page_counter + 1} data collected")

    def save_data(self, data):
        # Save data to CSV
        csv_file = "wfh_job.csv"
        keys = data[0].keys()
        with open(csv_file, "w", newline="", encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()  # Write the header (column names)
            dict_writer.writerows(data)  # Write the data rows

        self.logger.info(f"Data saved to {csv_file}")

          # Save data to JSON
        json_file = "wfh_job.json"
        with open(json_file, "w", encoding="utf-8") as json_output_file:
            json.dump(data, json_output_file, ensure_ascii=False, indent=4)

        self.logger.info("Data saved to CSV, Excel, and JSON files.")