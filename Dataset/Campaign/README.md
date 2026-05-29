# Synthetic Data
This project simulates realistic synthetic campaign data for analytics practice, SQL testing, and marketing portfolio projects.

## Long-Term Simulation
> 💡 The randomness is locked at **seed 92**, creating a permanent save point that keeps IDs and relationships consistent for ERDs, joins, and relational databases. This ensures that the dataset to evolve consistently over time.

---

### Core Features
* **Data Source:** Modeled in alignment with the **Thailand Consumer Spending Index** via `tradingeconomics.com`.
* **Seasonality:** Campaign Budget allocations are strictly weighted by `2025` quarterly data spikes ($Q2 > Q4 > Q3 > Q1).
* **Campaign Timeline:** Designed to cover Payday, local festivals and evnets. Moreover set a week gap between campaign to protect teams burn out.
* **Time Travel Bug Fix:** Handled by adding +2 for year which start in December. 



