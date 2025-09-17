from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
from time import sleep

#Task 3
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'
driver.get(url)

search_list_results = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')

results = []

for li in search_list_results:
    try:
        title = li.find_element(By.CSS_SELECTOR, 'span.title-content')
        titles = title.text.strip()

        author_section = li.find_elements(By.CSS_SELECTOR, 'span.cp-author-link')
        authors = []

        for a in author_section:
            authors.append(a.text.strip())
        
        authors = '; '.join(authors) 

        format = li.find_element(By.CSS_SELECTOR, 'div.cp-format-info')
        year = format.text.strip()

        results.append({
            'Title': titles, 
            'Author': authors,
            'Format-Year': year
        })

    except Exception as e:
        print('Error:', e)

driver.quit()

df = pd.DataFrame(results)
print(df)

#Task 4
df.to_csv('get_books.csv', index = False)

with open('get_books.json', 'w') as file:
    json.dump(results, file, indent = 4)