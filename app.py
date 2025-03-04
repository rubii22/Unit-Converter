import streamlit as st

# ✅ PAGE CONFIGURATION (Must be first)
st.set_page_config(page_title="🌍Unit Converter", layout="wide")

# ✅ Custom CSS for a Sleek and Modern UI
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        color: #FFD700;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.3);
    }
    .stSidebar {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .stButton > button {
        background: #ffcc00;
        color: black;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 18px;
        transition: 0.3s;
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background: #ff9900;
        transform: scale(1.05);
    }
    .stInput input {
        border-radius: 8px;
        padding: 10px;
        font-size: 18px;
        text-align: center;
        font-weight: bold;
    }
    .stSelectbox select {
        border-radius: 8px;
        padding: 10px;
        font-size: 18px;
        text-align: center;
    }
    .stSuccess {
        font-size: 20px;
        font-weight: bold;
        color: #00FF7F;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='stTitle'>🌍Unit Converter</h1>", unsafe_allow_html=True)

# ✅ Sidebar for selecting conversion type
with st.sidebar:
    st.markdown("<div class='stSidebar'><h3>📌 Select Conversion Type</h3></div>", unsafe_allow_html=True)
    unit_type = st.selectbox("", ["Length", "Weight", "Temperature", "Currency"])

# ✅ Length Conversion Function
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Millimeters": 0.001, 
        "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048, "Inches": 0.0254
    }
    return value * (length_units[from_unit] / length_units[to_unit])

# ✅ Weight Conversion Function
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495
    }
    return value * (weight_units[from_unit] / weight_units[to_unit])

# ✅ Temperature Conversion Function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

# ✅ Static Currency Exchange Rates (Example: USD as base)
currency_rates = {
    "USD": 1.0, "EUR": 0.92, "PKR": 280.0, "GBP": 0.78, "INR": 83.0, "CAD": 1.34, "AUD": 1.5, "JPY": 150.0
}

# ✅ Input Field
value = st.number_input(f"🔢 Enter value to convert in {unit_type}:", min_value=0.0, format="%.2f", key="input_value")

# ✅ Dropdowns for unit selection
if unit_type == "Length":
    from_unit = st.selectbox("🔄 From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    to_unit = st.selectbox("🔄 To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    if st.button("🚀 Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.markdown(f"<div class='stSuccess'>✅ {value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Weight":
    from_unit = st.selectbox("🔄 From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("🔄 To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if st.button("🚀 Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.markdown(f"<div class='stSuccess'>✅ {value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Temperature":
    from_unit = st.selectbox("🔄 From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("🔄 To", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("🚀 Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.markdown(f"<div class='stSuccess'>✅ {value}° {from_unit} = {result:.2f}° {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Currency":
    from_currency = st.selectbox("💰 From Currency", list(currency_rates.keys()))
    to_currency = st.selectbox("💰 To Currency", list(currency_rates.keys()))
    if st.button("🚀 Convert"):
        if from_currency in currency_rates and to_currency in currency_rates:
            converted_amount = value * (currency_rates[to_currency] / currency_rates[from_currency])
            st.markdown(f"<div class='stSuccess'>✅ {value} {from_currency} = {converted_amount:.2f} {to_currency}</div>", unsafe_allow_html=True)
        else:
            st.error("⚠ Invalid Currency Code.")

# ✅ Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>👩‍💻 <b>Developed by Rubab Fatima</b></p>", unsafe_allow_html=True)
