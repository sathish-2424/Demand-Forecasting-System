# Demand Forecasting System

This project is a notebook-based demand forecasting workflow built on a retail-style transactional dataset. It covers data loading, feature engineering, exploratory analysis, stockout signal detection, and regression model benchmarking with Random Forest, XGBoost, and LightGBM.

## Project Files

- `demand_forecasting.ipynb`: main notebook containing the full analysis and model training workflow
- `demand_forecasting.csv`: source dataset used by the notebook

## Dataset Overview

The dataset contains `76,000` rows and `16` original columns:

- `Date`
- `Store ID`
- `Product ID`
- `Category`
- `Region`
- `Inventory Level`
- `Units Sold`
- `Units Ordered`
- `Price`
- `Discount`
- `Weather Condition`
- `Promotion`
- `Competitor Pricing`
- `Seasonality`
- `Epidemic`
- `Demand`

## What The Notebook Does

### 1. Data Inspection

The notebook:

- loads the CSV with pandas
- checks dataset info
- checks for missing values
- checks for duplicate rows

### 2. Feature Engineering

Additional features created in the notebook:

- `Month`
- `DayOfWeek`
- `IsWeekend`
- `PriceDiff`
- `InventoryTurnover`
- `PotentialStockout`

Feature logic includes:

- extracting calendar signals from `Date`
- comparing store price against competitor pricing
- estimating inventory turnover from units sold and inventory
- flagging potential stockouts when demand exceeds units sold and inventory is low

### 3. Exploratory Data Analysis

The notebook generates visual analysis for:

- correlation heatmap
- daily demand trend
- category-wise demand distribution
- promotion impact on demand
- weather impact on demand
- price vs demand relationship
- competitor pricing vs demand
- regional demand performance by promotion

### 4. Model Training

Categorical fields are label-encoded before training. The target is `Demand`, and the feature set excludes `Demand` and `Date`.

Models used:

- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

Train/test split:

- training set shape: `60,800 x 20`
- test size: `20%`
- random state: `42`

## Results

Saved notebook outputs show the following model performance:

| Model | MAE | R2 |
| --- | ---: | ---: |
| Random Forest | 12.6672 | 0.8723 |
| XGBoost | 11.6409 | 0.8939 |
| LightGBM | 11.6503 | 0.8955 |

Best observed `R2`: LightGBM (`0.8955`)

Best observed `MAE`: XGBoost (`11.6409`)

## Stockout Signal Snapshot

Potential stockout rate by category from the saved notebook output:

| Category | Potential Stockout Rate |
| --- | ---: |
| Groceries | 0.008289 |
| Toys | 0.006109 |
| Electronics | 0.006031 |
| Clothing | 0.005674 |
| Furniture | 0.004751 |

## Requirements

The notebook imports or installs the following Python packages:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `xgboost`
- `lightgbm`

Install them with:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost lightgbm
```

## How To Run

1. Create and activate a Python environment.
2. Install the required packages.
3. Open `demand_forecasting.ipynb` in Jupyter Notebook or JupyterLab.
4. Run the notebook cells from top to bottom.

## Summary

This repository demonstrates an end-to-end demand forecasting workflow for retail data, combining feature engineering, EDA, operational stockout insights, and model comparison in a single notebook.
