import streamlit as st



# Custom CSS for background color and text styling
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    .stApp {
        background-color: #f0f8ff;
    }
    h1 {
        color: #4a4a4a;
        text-align: center;
    }
    div[data-baseweb="select"] > div {
        background-color: #e6f7ff;
    }
    button {
        background-color: #007acc;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)



# Conversion function
def Convertunits(value, unit_from, unit_to):
    conversions = {
   # Length
    "meter_kilometer": 0.001,
    "kilometer_meter": 1000,
    "centimeter_meter": 0.01,
    "meter_centimeter": 100,
    "millimeter_meter": 0.001,
    "meter_millimeter": 1000,
    "kilometer_millimeter": 1_000_000,
    "millimeter_kilometer": 1 / 1_000_000,
    "kilometer_centimeter": 100_000,
    "centimeter_kilometer": 1 / 100_000,
    "mile_kilometer": 1.60934,
    "kilometer_mile": 0.621371,
    "mile_meter": 1609.34,
    "meter_mile": 1 / 1609.34,
    "foot_meter": 0.3048,
    "meter_foot": 3.28084,
    "foot_centimeter": 30.48,
    "centimeter_foot": 1 / 30.48,
    "inch_centimeter": 2.54,
    "centimeter_inch": 0.393701,
    "inch_millimeter": 25.4,
    "millimeter_inch": 1 / 25.4,

    # Mass
    "gram_kilogram": 0.001,
    "kilogram_gram": 1000,
    "pound_kilogram": 0.453592,
    "kilogram_pound": 2.20462,
    "ounce_gram": 28.3495,
    "gram_ounce": 0.035274,
    "pound_gram": 453.592,
    "gram_pound": 1 / 453.592,

    # Time
    "second_minute": 1 / 60,
    "minute_second": 60,
    "minute_hour": 1 / 60,
    "hour_minute": 60,
    "hour_second": 3600,
    "second_hour": 1 / 3600,
    "hour_day": 1 / 24,
    "day_hour": 24,
    "day_minute": 1440,
    "minute_day": 1 / 1440,
     }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    else:
        return None


# App title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟Universal Unit Converter 🌟</h1>", unsafe_allow_html=True)
st.write("---")

# Input section
col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("🔢 Enter the value:", min_value=1.0, step=1.0)

units = [
    "meter", "kilometer", "centimeter", "millimeter", "mile", "foot", "inch",
    "gram", "kilogram", "pound", "ounce",
    "second", "minute", "hour", "day"
]

with col2:
    unit_from = st.selectbox("📤 Convert from:", units)

with col3:
    unit_to = st.selectbox("📥 Convert to:", units)

st.write("---")

# Convert button
if st.button("🚀 Convert"):
    result = Convertunits(value, unit_from, unit_to)

    if result is None:
        st.error("❌ Conversion not supported between these units.")
    else:
        if unit_from == "second" and unit_to == "minute":
            minutes = int(result)
            seconds = int((result - minutes) * 60)
            st.success(f"✅ Converted value: {minutes} min {seconds} sec")
        else:
            st.success(f"✅ Converted value: {round(result, 2)} {unit_to}")
# .