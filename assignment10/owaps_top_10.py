from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get('https://owasp.org/www-project-top-ten/')

owasp_top_10 = []
top_10 = driver.find_elements(By.XPATH,"//a[contains(@href, 'A0') or contains(@href, 'A1')]")

for item in top_10:
    title = item.text.strip()
    url = item.get_attribute('href')

    if title and url:
        owasp_top_10.append({'Title': title, 'URL': url})

driver.quit()

print(owasp_top_10)

df = pd.DataFrame(owasp_top_10)
df.to_csv('owasp_top_10.csv', index = False)