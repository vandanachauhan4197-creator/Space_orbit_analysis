# 🛰️ Space Trash Tracker: Orbital Traffic & Risk Analytics
 (**Project Status:** *Under Active Development* 🏗️
> **Note:** The Python backend and data engineering pipeline are 100% complete. I am currently building the interactive Power BI / Tableau dashboard, which will be deployed here in the next 1-2 days).

## 🌍 The Big Problem:
Imagine driving on a highway full of speeding cars, but there are no traffic lights, and the road is littered with broken car parts flying around at 10 times the speed of a bullet. That is exactly what is happening in space right now!

When old satellites collide or break down, they leave behind thousands of pieces of dangerous space trash (debris). This trash spins around the Earth at incredible speeds and can crush multi-million dollar active satellites (like the ones providing our GPS, weather reports, and internet). 

This project is a **Smart Tracking System** built to identify where this trash is, how high it is flying, and which pieces pose the biggest danger to our space systems.

---

## ⚡ What Does This Project Do?
This project automatically builds a complete data pipeline that works in 3 simple stages:

1. **Live Data Fetching (`fetch_data.py`)**: It connects directly to live space databases (CelesTrak API) and pulls the latest real-time tracking records of the Iridium-33 debris cloud.
2. **Space Math Calculations (`enrich_data.py`)**: Raw space data doesn't tell you how high the trash is. This script uses fundamental laws of space physics (Kepler's Third Law) to calculate the exact **Altitude (Height in Kilometers)** of each piece of junk from Earth.
3. **Smart Danger Scoring**: It calculates a **Collision Risk Score (1 to 100)** for every single object. If a piece of trash is flying very fast in a highly crowded area, its score goes up, marking it as a "Critical Threat."

---

## 📱 Built on a Mobile Phone! (The Innovation)
The most unique part of this project? **The entire backend data engineering, physics calculations, and logic setup were coded entirely on a smartphone** using Pydroid 3 (Python). 

This demonstrates high resourcefulness and advanced problem-solving skills—proving that you don't need heavy corporate machines to build advanced data infrastructure.

---

## 📂 Project Structure
* `fetch_data.py` 📥 -> The automatic data gatherer (Downloads live data).
* `enrich_data.py` 🧠 -> The brain of the project (Cleans data & calculates risk scores).
* `space_debris_enriched.csv` 💾 -> The final, clean Excel-style sheet ready to be used for business dashboards.

---

## 🔮 What's Next? (The Final Dashboard)
The clean data produced by this Python pipeline is 100% ready to be loaded into modern business intelligence tools like **Power BI** or **Tableau** to create interactive dashboards with:
* **Red Alert Filters**: To instantly see only the most dangerous pieces of trash.
