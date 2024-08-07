<h1 align="center">
	La Mer Product Selection and Price Analysis: Chicago O'Hare Airport
</h1>

<h3 align="center">
	<img src="https://github.com/DOCUVESTA/la-mer-skincare-chicago-duty-free-analysis/blob/a6747ef141dabd9d03f88a71cbc70df1146517bf/assets/header.png"/>
</h3>

## Overview
How much do we really save by shopping duty-free at the airport? These were my thoughts during a flight delay while travelling back home from the Chicago O'Hare International Airport. Skincare and cosmetics rank among the highest-selling categories in terms of volume at airport duty-free stores, especially sought after by travelers seeking in-demand products from luxury brands. La Mer stands out as one of the top high-end skincare brands, renowned for its beloved anti-aging cream: Crème de La Mer. To all skincare enthusiast and La Mer lovers, I will be comparing product selection, availability and pricing at three different purchase locations: Chicago O’Hare Terminal 3 duty-free store, Chicago O’Hare duty-free website and La Mer’s official USA website.

<br>

## Repository Contents
### Folder: data
#### Raw data
<table style="width:100%">
    <tr>
        <th>File Name</th>
        <th>Data Description</th>
    </tr>
    <tr>
        <td>lamer_bestsellers.json</td>
        <td>best-seller products on La Mer's website</td>
    </tr>
    <tr>
        <td>lamer_face_products.json</td>
        <td>all face products on La Mer's website</td>
    </tr>
    <tr>
        <td>lamer_official_website.xlsx</td>
        <td>best-seller and face products with multiple sizes available</td>
    </tr>
    <tr>
        <td>lamer_ord_data.xlsx</td>
        <td>La Mer product information collected from Chicago O'Hare International Airport duty-free store and website</td>
    </tr>
</table>

#### Final cleaned data
<table style="width:100%">
    <tr>
        <th>File Name</th>
        <th>Data Description</th>
    </tr>
    <tr>
        <td>df_dutyfree_ord.csv</td>
        <td>all products from Chicago O'Hare International Airport Terminal 3 duty-free store</td>
    </tr>
    <tr>
        <td>df_dutyfree_website.csv</td>
        <td>all products on the Chicago O'Hare International Airport duty-free website</td>
    </tr>
    <tr>
        <td>df_lamer_bestsellers.csv</td>
        <td>all best-seller products from La Mer's official USA website</td>
    </tr>
    <tr>
        <td>df_lamer_face_products.csv</td>
        <td>all face products from La Mer's official USA website</td>
    </tr>
</table>


<br>

### Python Script: lamer_data.py
- Web scraping program
- Key libraries: requests, BeautifulSoup, re and json

<br>

### Jupyter Notebook: la_mer_skincare_data_transformation.ipynb
- Jupyter notebook with annotations detailing each stage of preprocessing web scraped data
- Catalogue of La Mer products using HTML
- Seaborn + Plotly visualizations

<br>

### Notion: La Mer Products at the Chicago O’Hare Airport Duty Free public web page
A report with a brief history of the brand alongside a comprehensive comparison of product selection, availability, and pricing at three different purchase locations:
1. Chicago O'Hare International Airport Duty-Free Store (1 store - Terminal 3)
2. Chicago O'Hare International Airport Duty-Free Website (3 stores)
3. La Mer Official USA Website
<details closed>
<summary>Preview</summary>
<br>
	
![Report](https://github.com/DOCUVESTA/la-mer-skincare-chicago-duty-free-analysis/blob/921a8007b4461768ad3d625b2ca201ae5a319c2a/assets/preview_report.png)	
</details>

<p>
  <a href="https://docuvesta.notion.site/La-Mer-Products-at-the-Chicago-O-Hare-Airport-Duty-Free-12d6194be33b498db8f78a5741347721?pvs=4"><img src="https://img.shields.io/badge/Access-webpage-blue?style=for-the-badge&color=%23DAD2DF"></a>
</p>

<br>
