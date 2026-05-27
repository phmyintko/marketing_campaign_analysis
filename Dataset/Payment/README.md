# Synthetic Payment Data
This project simulates realistic synthetic product category data for analytics practice, SQL testing, and marketing portfolio projects.

## Long-Term Simulation
> 💡 The randomness is locked at **seed 92**, creating a permanent save point that keeps IDs and relationships consistent for ERDs, joins, and relational databases. This guarantees that the core product categorizations stay entirely deterministic during catalog expansions.

---

### Core Features
* **Payment Visual Prefixing:** Primary keys utilize a `PAY_` layout ruleset to cleanly distinguish transactional dimensional constraints from structural keys.
* **Timeline-Driven Feature Activation:** - **Phase 1 (Baseline - Jan 2025):** Core operations initialize exclusively with standard transactional channels (**Credit Card**, **PromptPay**, **COD**).
  - **Phase 2 (Expansion - April 2025):** To support the launch of the new product lines (Pillows, Bolsters, Blankets) manufactured out of the Nantong facility, the pipeline introduces **TrueMoney Wallet** capability.

---

### Limitations & Future Scope
* **Payment Method Expansion:** Future version may introduce installment payments, and other widely used Thai payment methods such as Line Pay and Shopee Pay.
