
import streamlit as st

# Apply custom styles
st.markdown(
    """
    <style>
    /* Main Background */
    body, .stApp {
        background: rgb(2,0,36);
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,50,121,1) 35%, rgba(0,180,255,1) 100%);
        color: white;
    }
    
    /* Title Styling */
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #00FFFF, #007BFF);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
        border: none;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #00FFFF, #FF00FF);
        color: black;
    }
    
    label {
        font-size: 20px !important;
        font-weight: bold !important;
        color:rgb(255, 255, 255) !important;
    }
    
    /* Result Box */
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: #00d4ff;
        color: black;
        font-family: 'Arial', sans-serif;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Swift Unit Converter</h1>", unsafe_allow_html=True)

conversion_type = st.selectbox("**Choose Converter Type**", [
    "Length", "Weight", "Temperature", "Mass", "Time", "Speed", "Area", "Volume", "Energy", "Pressure", "Power"
])

value = st.number_input("**Enter Value**", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

unit_categories = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Mass": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Second", "Minute", "Hour", "Day", "Week"],
    "Speed": ["Meter/Second", "Kilometer/Hour", "Miles/Hour"],
    "Area": ["Square Meter", "Square Kilometer", "Acre", "Hectare"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon"],
    "Energy": ["Joule", "Kilojoule", "Calorie", "Kilowatt-hour"],
    "Pressure": ["Pascal", "Bar", "Atmosphere", "mmHg"],
    "Power": ["Watt", "Kilowatt", "Horsepower"]
}

with col1:
    from_unit = st.selectbox("**From**", unit_categories[conversion_type])
with col2:
    to_unit = st.selectbox("**To**", unit_categories[conversion_type])

def unit_converter(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274},
        "Mass": {"Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274},
        "Time": {"Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800},
        "Speed": {"Meter/Second": 1, "Kilometer/Hour": 3.6, "Miles/Hour": 2.23694},
        "Area": {"Square Meter": 1, "Square Kilometer": 1e-6, "Acre": 0.000247105, "Hectare": 0.0001},
        "Volume": {"Liter": 1, "Milliliter": 1000, "Cubic Meter": 0.001, "Gallon": 0.264172},
        "Energy": {"Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilowatt-hour": 2.77778e-7},
        "Pressure": {"Pascal": 1, "Bar": 1e-5, "Atmosphere": 9.86923e-6, "mmHg": 0.00750062},
        "Power": {"Watt": 1, "Kilowatt": 0.001, "Horsepower": 0.00134102}
    }
    if category in conversion_factors:
        return (value / conversion_factors[category][from_unit]) * conversion_factors[category][to_unit]
    return value

if st.button("Convert"):
    result = unit_converter(value, from_unit, to_unit, conversion_type)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Sidebar Enhancements
st.sidebar.header("🔹 Fun Facts & Extras")
st.sidebar.write("🎯 Did you know? The **second** is defined based on the vibrations of cesium atoms!")
st.sidebar.write("🏎️ **Speed Fact:** The fastest human-run speed is about 10.44 meters/second!")
st.sidebar.write("⚡ **Power Fact:** One horsepower is about 746 watts!")

# Sidebar Theme Selection
theme_choice = st.sidebar.radio("🌈 Choose Theme", ["Dark Mode", "Light Mode", "Colorful"])

if theme_choice == "Dark Mode":
    st.sidebar.write("🖤 **Dark Mode Activated!**")
elif theme_choice == "Light Mode":
    st.sidebar.write("☀️ **Light Mode Activated!**")
else:
    st.sidebar.write("🌈 **Colorful Mode Activated!** 🎨")