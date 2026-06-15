# Synthetic Data
This project simulates realistic synthetic order data for analytics practice, SQL testing, and marketing portfolio projects.

## Long-Term Simulation
> 💡 The randomness is locked at **seed 92**, creating a permanent save point that keeps IDs and relationships consistent for ERDs, joins, and relational databases. This guarantees that the core product categorizations stay entirely deterministic during catalog expansions.

---

### Core Features
* **Customer Segmentation:** Customers are assigned to realistic purchasing behaviors like 75% One Time Customer, 20% Repeat Customer (2 to 6 times) and 5% Commercial Customer (8 to 20 times).
* **Order Distribution Rule:** Order years are weighted according to Thailand consumer spending trend. ref: tradingeconomics.com
* **Timeline Validation:** Orders cannot occur before customer registration, and payments cannot be assigned to orders that predate the payment creation date.


