from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time
from config import CONFIG  # Import configuration from external file

# Auto-download and install ChromeDriver
chromedriver_autoinstaller.install()

def test_divar():
    print("🚀 Starting Selenium in headless mode...")

    # Configure Chrome to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Step 1: Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Step 2: Open Divar website
    driver.get(CONFIG["url"])
    print(f"🌍 Opened Divar website: {CONFIG['url']}")

    try:
        wait = WebDriverWait(driver, 10)

        # Step 3: Click on the city selection button
        print(f"⏳ Waiting for the {CONFIG['city']} button...")
        city_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class, 'city-card-fffcd')]//h2[contains(text(), '{CONFIG['city']}')]")
        ))
        print(f"✅ {CONFIG['city']} button found! Clicking now...")
        city_button.click()
        time.sleep(CONFIG['sleep_time'])

        # Step 4: Verify city is selected
        print(f"🔍 Checking if {CONFIG['city']} is selected...")
        selected_city = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'nav-bar__city-button')]//span"))
        )
        assert CONFIG['city'] in selected_city.text, f"❌ ERROR: {CONFIG['city']} was not selected correctly!"
        print(f"✅ Verified: {CONFIG['city']} is selected! Found: {selected_city.text}")

        # Step 5: Select Amlak (Real Estate) category
        print("⏳ Waiting for Amlak category...")
        amlak_category = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//li[@role='button']//a[contains(@href, '{CONFIG['amlak_category']}')]"))
        )
        print("✅ Amlak category found! Clicking now...")
        amlak_category.click()
        time.sleep(CONFIG['sleep_time'])

        # Step 6: Select Forosh Maskuni (Residential Sales)
        print("⏳ Waiting for Residential Sales category...")
        residential_sales_category = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//li[@role='button']//a[contains(@href, '{CONFIG['residential_sales']}')]"))
        )
        print("✅ Residential Sales category found! Clicking now...")
        residential_sales_category.click()
        time.sleep(2)

        # Step 7: Select House & Villa category
        print("⏳ Waiting for House & Villa category...")
        house_villa_category = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '{CONFIG['house_villa_category']}')]"))
        )
        print("✅ House & Villa category found! Clicking now...")
        house_villa_category.click()
        time.sleep(2)

        # Step 8: Click on 'محل' (Location) filter
        print(f"⏳ Waiting for '{CONFIG['location_filter']}' button...")
        location_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(@class, 'kt-toolbox-header__title-group') and span[contains(text(), '{CONFIG['location_filter']}')]]"))
        )
        print(f"✅ '{CONFIG['location_filter']}' button found! Clicking now...")
        location_button.click()
        time.sleep(2)

        # Step 9: Click on 'تعیین محل' (Set Location)
        print(f"⏳ Waiting for '{CONFIG['set_location']}' button...")
        set_location_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='actionField' and contains(@class, 'kt-action-field')]")
        ))
        print(f"✅ '{CONFIG['set_location']}' button found! Clicking now...")
        set_location_button.click()
        time.sleep(2)

        # Step 10: Select 'آبشار' location
        print(f"⏳ Waiting for '{CONFIG['location_name']}' location option...")
        abshar_location = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='listitem']//p[contains(text(), '{CONFIG['location_name']}')]"))
        )
        print(f"✅ '{CONFIG['location_name']}' location found! Selecting now...")
        abshar_location.click()
        time.sleep(2)

        print("🎉 All tests passed successfully!")

    except Exception as e:
        print(f"🚨 ERROR OCCURRED: {e}")

    finally:
        driver.quit()
        print("🛑 Browser closed.")


