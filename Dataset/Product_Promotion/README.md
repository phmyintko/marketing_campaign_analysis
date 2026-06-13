# Synthetic Data
This project simulates realistic synthetic Product Promotion bridge table for analytics practice, SQL testing, and marketing portfolio projects.

---

## Long-Term Simulation
> 💡 The randomness is locked at **seed 92**, creating a permanent save point that keeps IDs and relationships consistent for ERDs, joins, and relational databases. This ensures that the dataset to evolve consistently over time.

---

### Core Features
* **Field Matching:** Promotions are automatically linked to relevant products by matching keywords in promotion names. 
* **Promotion Rules:** Discount values are generated according to promotion type: Percentage Discount, Fixed Discount, Voucher Code, Flash Sale, Bundle Offer, and Free Shipping. Major campaigns such as Mid-Year Discount and 11.11 receive higher discount rates than regular promotions.
* **Fixed Discount Rule:** Fixed discount amounts are calculated dynamically from product prices.
* **One to Many:** Duplicate Product–Promotion relationships are removed to maintain unique Product_ID and Promotion_ID pairs.

