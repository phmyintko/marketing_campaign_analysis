## Purpose

This entity acts as a bridge between Orders and Products. It enables customers to purchase multiple products under a single order while recording product-level details such as quantity, unit price, and total amount. The dataset supports sales analysis, product performance reporting, customer purchasing behavior analysis, and revenue tracking.

---

## Core Features

* Weighted category, subcategory, and size selection based on realistic purchase patterns.
* Product, Product Sub Category, and Product Category entities are joined to filter matching products.
* Products are randomly selected from eligible filtered results.
* Quantity generation varies by customer type.
* Total amount is calculated using unit price and quantity.
* All records maintain valid Order and Product relationships.

---

## Business Rules

* Product categories follow weighted purchase distributions:
  * Mattress — 46%
  * Bedsheet — 24%
  * Pillow — 16%
  * Bolster — 10%
  * Blanket — 4%

* Each category applies its own subcategory and size distribution.

* Quantities vary based on customer type:
  * One-Time Customers
  * Repeat Customers
  * Commercial Customers

* Only products matching the generated category, subcategory, and size are eligible for selection.

---

## Output

Generated dataset fields:

* Order_Items_ID
* Order_ID
* Product_ID
* Quantity
* Unit_Price
* Total_Amount