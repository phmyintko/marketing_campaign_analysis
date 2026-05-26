# Synthetic Manufacturer Data

This project simulates realistic synthetic manufacturer data for analytics practice, SQL testing, and marketing portfolio projects.

## Long-Term Simulation

> 💡 The randomness is locked at **seed 92**, creating a permanent save point that keeps IDs and relationships consistent for ERDs, joins, and relational databases. This ensures that the dataset to evolve consistently over time.

---

### Core Features
* **Geographic Mapping:** Manufacturers are assigned to realistic production regions, with mattress factory based in **Foshan** and bedding factory based in **Nantong**.
* **Timeline Logic:** Manufacturer creation dates follow a structured timeline, with mattress manufacturers starting in January 2025 and bedding manufacturers starting in April 2025.
* **Prefixes:** Manufacturer ID uses a short 4-character UUID with the `MFG_` prefix to keep records organized and easy to connect across tables.

---

### Limitations & Future Scope

* **Localization:** Future expansions could incorporate Thailand-based manufacturers to simulate both imported supply chains and localized domestic production.