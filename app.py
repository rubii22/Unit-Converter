
import streamlit as st

# ✅ PAGE CONFIGURATION
st.set_page_config(page_title="🌍 Unit Converter", layout="wide")

# ✅ Dark Mode Toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

# ✅ Custom CSS for Light/Dark Theme
if dark_mode:
    background_color = "#121212"
    text_color = "white"
else:
    background_color = "linear-gradient(to right, #1e3c72, #2a5298)"
    text_color = "black"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {background_color};
        color: {text_color};
        font-family: 'Arial', sans-serif;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>🌍 Unit Converter</h1>", unsafe_allow_html=True)

# ✅ Sidebar for selecting conversion type
st.sidebar.markdown("### 📌 Select Conversion Type")
unit_type = st.sidebar.selectbox("", ["Length", "Weight", "Temperature", "Currency", "Volume", "Speed", "Data Storage"])

# ✅ Conversion Functions
def convert_length(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048, "Inches": 0.0254}
    return value * (length_units[from_unit] / length_units[to_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592}
    return value * (weight_units[from_unit] / weight_units[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

currency_rates = {"USD": 1.0, "EUR": 0.92, "PKR": 280.0, "GBP": 0.78}

def convert_volume(value, from_unit, to_unit):
    volume_units = {"Liters": 1, "Milliliters": 0.001, "Gallons": 3.785, "Cups": 0.24}
    return value * (volume_units[from_unit] / volume_units[to_unit])

def convert_speed(value, from_unit, to_unit):
    speed_units = {"Km/h": 1, "Mph": 1.609, "m/s": 3.6}
    return value * (speed_units[from_unit] / speed_units[to_unit])

def convert_data(value, from_unit, to_unit):
    data_units = {"Bytes": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3}
    return value * (data_units[from_unit] / data_units[to_unit])

# ✅ Conversion History
if "history" not in st.session_state:
    st.session_state.history = []

# ✅ Input and Conversion
value = st.number_input(f"🔢 Enter value to convert in {unit_type}:", min_value=0.0, format="%.2f")

unit_options = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "Weight": ["Kilograms", "Grams", "Pounds"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Currency": list(currency_rates.keys()),
    "Volume": ["Liters", "Milliliters", "Gallons", "Cups"],
    "Speed": ["Km/h", "Mph", "m/s"],
    "Data Storage": ["Bytes", "KB", "MB", "GB"],
}

from_unit = st.selectbox("🔄 From", unit_options[unit_type])
to_unit = st.selectbox("🔄 To", unit_options[unit_type])

if st.button("🚀 Convert"):
    if unit_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif unit_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif unit_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif unit_type == "Currency":
        result = value * (currency_rates[to_unit] / currency_rates[from_unit])
    elif unit_type == "Volume":
        result = convert_volume(value, from_unit, to_unit)
    elif unit_type == "Speed":
        result = convert_speed(value, from_unit, to_unit)
    elif unit_type == "Data Storage":
        result = convert_data(value, from_unit, to_unit)

    # ✅ Store history
    st.session_state.history.append(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# ✅ Show History
st.sidebar.markdown("### 🕘 Conversion History")
for item in reversed(st.session_state.history[-5:]):  # Show last 5 conversions
    st.sidebar.write(item)

st.sidebar.markdown("ℹ️ Only last 5 conversions shown.")
