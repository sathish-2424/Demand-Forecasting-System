import pickle
import warnings
from pathlib import Path

import pandas as pd
import streamlit as st

warnings.filterwarnings("ignore")

MODEL_FILE = "demand_model.pkl"

st.set_page_config(page_title="Demand Forecasting", layout="wide")
st.title("Demand Forecasting System")


# ---------------- LOAD MODEL ----------------
def load_model():
    if Path(MODEL_FILE).exists():
        with open(MODEL_FILE, "rb") as f:
            return pickle.load(f)
    return None


# ---------------- UI ----------------
bundle = load_model()

# ---------------- PREDICTION ----------------
if bundle:
    st.subheader("Prediction")

    model = bundle["model"]
    columns = bundle["columns"]

    price = st.number_input("Price", 50.0)
    comp = st.number_input("Competitor Price", 55.0)
    inventory = st.number_input("Inventory", 100.0)
    units = st.number_input("Units Sold", 50.0)

    lag7 = st.number_input("Lag7", 100.0)
    lag14 = st.number_input("Lag14", 95.0)

    if st.button("Predict"):
        sample = pd.DataFrame([{
            "Store ID": 0,
            "Product ID": 0,
            "Category": 0,
            "Region": 0,
            "Inventory Level": inventory,
            "Units Sold": units,
            "Units Ordered": 100,
            "Price": price,
            "Discount": 0,
            "Weather Condition": 0,
            "Promotion": 0,
            "Competitor Pricing": comp,
            "Seasonality": 0,
            "Epidemic": 0,
            "Month": 1,
            "DayOfWeek": 1,
            "IsWeekend": 0,
            "PriceDiff": comp - price,
            "InventoryTurnover": units / inventory if inventory else 0,
            "Lag7": lag7,
            "Lag14": lag14
        }])

        sample = sample.reindex(columns=columns, fill_value=0)
        pred = model.predict(sample)[0]

        st.success(f"Predicted Demand: {pred:.2f}")
else:
    st.info("Ensure demand_model.pkl exists")
