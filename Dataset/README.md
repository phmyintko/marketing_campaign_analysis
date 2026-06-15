## Core Business Growth Timeline (Dataset Evolution)

Rather than generating completely random, disconnected tables, the synthetic data pipelines are synchronized to mimic a realistic, phased corporate timeline. This intentional architecture allows the final portfolio analysis to measure the direct business impact of operational expansions, product diversifications, and checkout optimizations.

---

## Business Evolution Timeline

The synthetic dataset simulates the growth lifecycle of a Thai home goods retailer between 2021 - 2026.

| Year | Business Stage | Major Changes | Strategic Focus |
|---|---|---|---|
| 2021 | Launch Stage | Spring mattresses & bedsheets introduced | grow customer base  |
| 2022 | Early Growth | Customer base reaches 1,000+ | increase revenue |
| 2023 | Product Expansion | Pocket spring mattresses & linen bedsheets added | improve customer retention |
| 2024 | Category Expansion | Pillows, bolsters & blankets introduced | cross-category adoption & category penetration |
| 2025 | Customer Engagement Stage | Loyalty campaigns introduced | cross-category adoption & repeat purchases growth |
| 2026 | Marketing Optimization Stage | Multi-channel attribution analysis & targeting refinement expanded | Improve campaign effectiveness & increase revenue |



Customer acquisition trends were assigned by using Thailand’s GDP growth. Higher growth years generally reflect stronger consumer demand and business confidence, allowing companies to invest more in marketing and customer acquisition. Lower growth years were assigned lower signup probabilities to simulate a more challenging business environment.



---

## Future Architecture & Excluded Domains

To keep the initial portfolio focus tightly bounded around marketing campaign attribution and acquisition funnels, certain backend operational domains have been intentionally omitted from this version of the dataset.

### The Delivery & Fulfillment Module (Planned Future Version)
A dedicated **Delivery Entity** is not included in the current project phase. Future system versions will introduce an isolated logistics schema to track the full post-purchase lifecycle:
* **Fulfillment States:** Tracking transit phases via `Delivery_Status` (e.g., *Processing, Dispatched, In-Transit, Delivered*).
* **Reverse Logistics:** Dedicated pipelines to handle customer returns, exchanges, and dynamic refund processing statuses.
* **Carrier Performance:** Mapping third-party shipping provider efficiency, transit times, and regional delivery delays.

### Future Improvement
Future versions of the dataset may introduce additional digital marketing entities such as web analytics sessions, ad impression logs, social engagement metrics, and traffic attribution systems to support full-funnel brand awareness analysis and upper-funnel campaign performance measurement.