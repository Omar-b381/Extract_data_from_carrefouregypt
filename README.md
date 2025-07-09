# 🛒 Carrefouregypt Olive Oil Scraper

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Extract all data about  https://www.carrefouregypt.com/mafegy/ar/c/FEGY1760404?currentPage=1

This project is a simple web scraper built using **Selenium** and **Pandas**. It extracts information about **olive oil products** from [Carrefour Egypt](https://www.carrefouregypt.com/mafegy/ar/c/FEGY1760404), including:

* ✅ Product name
* ✅ Price
* ✅ Product link
* ✅ Image URL

The data is saved to an Excel file: `Carfoor_oil.xlsx`

---

## 📂 Output Example

| Product                      | Price | Link        | Image         |
| ---------------------------- | ----- | ----------- | ------------- |
| زيت زيتون بكر بورجيس - 500مل | 570   | [Link](...) | ![Image](...) |

---

## 🛠 Requirements

Make sure you have the following installed:

* Python 3.7+
* Firefox + geckodriver (or Chrome + chromedriver if you change the browser)
* The following Python packages:

```bash
pip install selenium pandas openpyxl
```

---

## 🚀 How to Run

```bash
python scraper.py
```

This will generate an Excel file named `Carfoor_oil.xlsx` in the same directory.

---

## 📌 Notes

* The scraper uses **Firefox WebDriver** by default. You can switch to Chrome by editing the line:

  ```python
  driver = webdriver.Chrome()
  ```
* Make sure your WebDriver (e.g., `geckodriver` for Firefox) is installed and added to your system PATH.

---

## 📈 Future Ideas

* Support for multiple pages
* Track price changes over time
* Export to CSV or database

---

## 🧑‍💻 Author

Developed by \ omar ahmed badr
Feel free to modify, extend, or share.


