# Synthetic Data

This project simulates realistic synthetic Product Sub Category data for analytics practice, SQL testing, and retail product portfolio projects.

---

### Core Features

* **One to Many Relationship:** Builds a realistic product hierarchy by linking each sub-category directly to its parent product category, supporting one-to-many category relationships commonly found in retail and e-commerce databases.

* **Product Mapping:** Assigns sub-categories using predefined merchandising logic (e.g., Foam, Spring, and Pocket Spring belong to Mattress) instead of generating random product classifications.

* **Timeline Consistency:** Preserves historical accuracy by ensuring a sub-category cannot exist before its parent category is introduced, preventing timeline inconsistencies within the product catalog.

* **Deterministic Identifier Generation:** Uses a fixed seed to guarantee stable and reproducible sub-category identifiers across dataset regenerations, ensuring reliable database joins and ERD relationships.

* **Data Modeling:** Stores category relationships through foreign keys

---

### Entity Relationship

```text
Campaign

    │
    |
    └───< Campaign_Objective >───┐
                                 │
                                 ▼

                             Objective
```