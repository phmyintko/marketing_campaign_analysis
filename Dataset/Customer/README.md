# Synthetic Data
This project simulates realistic synthetic customer data for analytics practice, SQL testing, and marketing portfolio projects.

## Long-Term Simulation
> 💡 The randomness is locked at **seed 92**, creating a permanent save point that keeps IDs and relationships consistent for ERDs, joins, and relational databases. This ensures that the dataset to evolve consistently over time.

---

### Core Features
* **Customer Acquisition Logic:** customer acquisition momentum is simulated by Thailand's GDP path 2021 to 2026.
* **Thai Demographic Profiles:** Localized names, phone formats `06`, `08`, `09`, and standard free email domains (Gmail, Yahoo, etc.).
* **Regional Weights:** Favors major economic cities like `Central` (Bangkok) and `Northern` (Chiang Mai) regions.
* **Age Curves:** Centers customer profiles around a bell curve of <mark>30 years old</mark> with a <mark>standard deviation of 7 years</mark>, bounded between <mark>ages 18 and 70</mark>.
* **Prefixes:** Customer ID uses a short 4-character UUID with the `CUST_` prefix to keep records organized and easy to connect across tables.
* **Gender:** Names are conditionally checked against the generated gender profile `Faker.name_male()` vs `Faker.name_female()` to prevent unrealistic demographic mismatches.
* **SignUp Logic:** To simulate customer acquisition momentum, the `Created_At` dates are generated based on **Thailand's GDP path from 2021 to 2026** via `worldometers.info`.

---

### Limitations & Future Scope
* **Geographic:** For processing efficiency and scoping purposes, information like `Address`, `Distinct`, `City`, and `Postal` are currently generated independently. In future projects, I may integrate a relational Thai geography database or look-up table to ensure districts, cities, and postal codes map to each other with 100% real-world accuracy. 