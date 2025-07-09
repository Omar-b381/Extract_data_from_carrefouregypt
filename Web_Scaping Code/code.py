from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Firefox()
driver.get("https://www.carrefouregypt.com/mafegy/ar/c/FEGY1760404?currentPage=1")



product = []
price = []
link = []
image  = []
elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="product_name"]')
for e in elements:
    product.append(e.text.strip())

major_prices = driver.find_elements(By.CSS_SELECTOR, 'div.css-14zpref')
for p in major_prices:
    price.append(p.text.strip())

product_links = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="product_name"]')
for l in product_links:
    link.append(l.get_attribute("href"))
    
images = driver.find_elements(By.CSS_SELECTOR, 'img[data-testid="product_image_main"]')
for i in images:
    image.append(i.get_attribute("src"))





import pandas as pd
df = pd.DataFrame({'product':product,'price':price,'link':link,'image':image})
df.head()
df.shape



df.to_excel('Carfoor_oil.xlsx',index=False)