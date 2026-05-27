## 📈 Core Business Growth Timeline (Dataset Evolution)

Rather than generating completely random, disconnected tables, the synthetic data pipelines are synchronized to mimic a realistic, phased corporate timeline. This intentional architecture allows the final portfolio analysis to measure the direct business impact of operational expansions, product diversifications, and checkout optimizations.

---

## 🔮 Future Architecture & Excluded Domains

To keep the initial portfolio focus tightly bounded around marketing campaign attribution and acquisition funnels, certain backend operational domains have been intentionally omitted from this version of the dataset.

### 🚚 The Delivery & Fulfillment Module (Planned Future Version)
A dedicated **Delivery Entity** is not included in the current project phase. Future system versions will introduce an isolated logistics schema to track the full post-purchase lifecycle:
* **Fulfillment States:** Tracking transit phases via `Delivery_Status` (e.g., *Processing, Dispatched, In-Transit, Delivered*).
* **Reverse Logistics:** Dedicated pipelines to handle customer returns, exchanges, and dynamic refund processing statuses.
* **Carrier Performance:** Mapping third-party shipping provider efficiency, transit times, and regional delivery delays.