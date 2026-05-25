# Synthetic Customer Data

This project simulates realistic synthetic customer data for analytics practice, SQL testing, and marketing portfolio projects.


## Long-Term Simulation

> 💡 The randomness is locked at **seed 92** like a permanent save point. If I later increase the dataset from 1,000 customers to 1,200 for a future project, the original 1,000 customers stay completely identical, and the simulation simply adds 200 brand-new customers to the end of the list. So the dataset stays consistent over time and evolves realistically in future projects.

---

### Core Features
* **Thai Demographic Profiles:** Localized names, phone formats `06`, `08`, `09`, and standard free email domains (Gmail, Yahoo, etc.).
* **Regional Weights:** Favors major economic cities like `Central` (Bangkok) and `Northern` (Chiang Mai) regions.
* **Age Curves:** Centers customer profiles around a bell curve of <mark>30 years old</mark> with a <mark>standard deviation of 7 years</mark>, bounded between <mark>ages 18 and 70</mark>.
* **Prefixes:** Customer IDs are generated with distinct string prefixes like `CUST_` or `ORD_` so fields never get mixed up when building database schemas. 
* **Gender:** Names are conditionally checked against the generated gender profile `Faker.name_male()` vs `Faker.name_female()` to prevent unrealistic demographic mismatches.

---

### Limitations & Future Scope

* **Geographic:** For processing efficiency and scoping purposes, information like `Address`, `Distinct`, `City`, and `Postal` are currently generated independently. In future projects, I may integrate a relational Thai geography database or look-up table to ensure districts, cities, and postal codes map to each other with 100% real-world accuracy. 