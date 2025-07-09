


# 🛒 Carrefour Egypt Product Scraper

This project scrapes product data from **Carrefour Egypt** using **Selenium**, then exports structured datasets for further analysis.

It currently supports:

* 🫒 Olive Oil (`Carfoor_oil.xlsx`)
* 🍯 Honey (`Carfoor_Honey.xlsx`)
* 🌴 Dates / Tamr (`Carfoor_tamr.xlsx`)
* 🥒 Pickles (`Carfoor_pickles.xlsx`)

---

## 📂 Extracted Data Includes:

* ✅ Product name
* ✅ Price (main value only)
* ✅ Product link
* ✅ Image URL

Each product category is stored in its own Excel file, and accompanied by an exploratory notebook for quick analysis.

---

## 🧪 Folder Structure

```
web-scraping/
├── oil_scraping/
│   ├── Web_Scaping Code/
│   │   └── python scraper_honey.py
│   ├── notebooks/
│   │   ├── Carfoor_Honey.xlsx
│   │   ├── Carfoor_pickles.xlsx
│   │   ├── Carfoor_tamr.xlsx
│   │   ├── Honeycarrefouregypt.ipynb
│   │   ├── Tamrcarrefouregypt.ipynb
│   │   └── pickles.ipynb
│   └── ...
```

---

## 🚀 How to Run

Install dependencies:

```bash
pip install selenium pandas openpyxl
```

Then run any scraper script. Example:

```bash
python "Web_Scaping Code/python scraper_honey.py"
```

An Excel file will be generated under `notebooks/`.

---

## 💡 Example Code Snippet

```python
elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="product_name"]')
for e in elements:
    product.append(e.text.strip())

major_prices = driver.find_elements(By.CSS_SELECTOR, 'div.css-14zpref')
for p in major_prices:
    price.append(p.text.strip())

images = driver.find_elements(By.CSS_SELECTOR, 'img[data-testid="product_image_main"]')
for i in images:
    image.append(i.get_attribute("src"))
```

---

## 🗃 Git Status & Notes

To add your current untracked files to Git:

```bash
git add .
git commit -m "Add honey scraper, Excel files, and notebooks"
git push
```

Or to ignore generated Excel files:

```bash
# .gitignore
*.xlsx
```

You may also want to rename the file `pickles .ipynb` (remove the space):

```bash
mv "pickles .ipynb" "pickles.ipynb"
```

---

## ✅ Future Plans

* Auto-scroll or pagination support
* Scheduled scraping (daily/weekly)
* Historical price tracking
* Export to CSV, database, or dashboard

---

## 👤 Author

Developed by **omar ahmed badr**
Feel free to contribute or suggest improvements.


