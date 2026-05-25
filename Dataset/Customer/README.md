# Synthetic Customer Data Generator

This project generates realistic synthetic customer data for analytics practice, SQL testing, dashboard development, and portfolio projects.

The dataset is designed to simulate a real-world customer database with:
- Customer demographics
- Contact information
- Regional distributions
- Birth dates
- Customer status
- Registration dates

---

# Project Goal

The purpose of this project is to create a reusable synthetic customer dataset that can be used for:

- SQL practice
- Marketing analytics
- Dashboard development
- Exploratory Data Analysis (EDA)
- Data cleaning practice
- Future campaign simulation projects

---

# Features

- Thai-style fake customer profiles using Faker
- Unique customer identifiers with prefixes
- Realistic phone number generation
- Weighted regional distributions
- Age generation using Gaussian distribution
- Reproducible synthetic data using fixed random seeds
- Exportable CSV dataset

---

# Technologies Used

- Python
- Pandas
- Faker
- Random
- Datetime
- Jupyter Notebook

---

# Dataset Columns

| Column Name | Description |
|---|---|
| Customer_ID | Unique customer identifier |
| Customer_Name | Generated customer full name |
| Email | Fake email address |
| Phone | Simulated Thai mobile phone number |
| Address | Generated street address |
| Distinct | Generated district/city |
| City | Generated city |
| Postal | Postal code |
| Region | Customer region |
| Date_of_Birth | Customer birth date |
| Gender | Male / Female / Other |
| Status | Marital status |
| Created_At | Customer registration date |

---

# Synthetic Data Logic

## Customer IDs

Customer IDs use prefixes like `CUST_` so identifiers remain readable and organized.

Example:

```python
CUST_a3f9
```

---

## Reproducible Dataset Generation

The randomness is locked using seed `92` so the dataset always generates the exact same customer records every time the notebook runs.

This keeps the simulation stable and consistent for future projects.

For example:
- if the dataset grows from 1,000 to 1,200 rows
- the original 1,000 customers remain unchanged
- only 200 new customers are added

This allows future analytics projects to reuse the same customer base consistently.

---

## Realistic Gender-Based Names

Customer names are generated based on selected gender values to improve realism.

---

## Thai Mobile Number Simulation

Phone numbers are forced to start with:
- `06`
- `08`
- `09`

to better simulate real Thai mobile phone formats.

---

## Regional Distribution Weighting

Weighted probabilities are used instead of uniform random sampling to create more realistic regional concentration patterns.

Higher customer concentrations are assigned to:
- Central region
- Northern region

to reflect larger population and business activity areas.

---

## Realistic Age Distribution

A Gaussian distribution is used to center customer ages around 30 years old while restricting unrealistic values.

```python
random.gauss(30, 7)
```

This creates a more natural age spread for analytics simulations.

---

# Example Output

| Customer_ID | Customer_Name | Region | Gender |
|---|---|---|---|
| CUST_a1b2 | Somchai Prasert | Central | Male |
| CUST_f9k3 | Nisa Wongchai | Northern | Female |

---

# How to Run

## Install dependencies

```bash
pip install faker pandas
```

---

## Run notebook

Open the notebook:

```bash
jupyter notebook
```

Run all cells:

```text
Kernel → Restart & Run All
```

---

# File Structure

```text
marketing-campaign-analysis/
│
├── Dataset/
│   └── Customer/
│       ├── Cust_data_population.ipynb
│       ├── Data_Population.py
│       └── synthetic_customer_data.csv
│
├── README.md
└── requirements.txt
```

---

# Future Improvements

Planned future expansions:

- Customer transaction tables
- Marketing campaign simulations
- Customer segmentation
- RFM analysis
- Dashboard visualization
- SQL schema modeling
- Cohort analysis datasets

---

# Author

Built as part of a marketing and data analytics portfolio project.