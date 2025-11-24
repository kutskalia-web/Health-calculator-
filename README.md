# Health-calculator-
# 🧑‍⚕️ Personalized Health Guide (BMI & Wellness Tracker)

A simple, user-friendly desktop application built with **Tkinter** in Python to calculate Body Mass Index (BMI) and provide personalized wellness recommendations based on the user's health metrics and lifestyle inputs (age, sleep habits, activity level, and smoking status).

## ✨ Features

* **BMI Calculation:** Accurately calculates BMI using the standard formula.
* **BMI Categorization:** Classifies BMI into standard WHO/CDC categories (Underweight, Normal, Overweight, Obesity).
* **Personalized Feedback:** Provides specific recommendations for:
    * **Sleep:** Feedback based on age-appropriate sleep hour recommendations.
    * **Activity:** Advice tailored to sedentary, moderate, or active lifestyles.
    * **Smoking Status:** Critical health advice based on smoking status.
    * **General Health:** Diet and wellness tips based on the calculated BMI category.
* **GUI Interface:** A straightforward graphical interface for easy data input and report viewing.

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** installed on your system. This application relies on the standard `tkinter` library, which is included with most Python installations.

### Installation

1.  **Clone the repository** (or download the code file):

    ```bash
    git clone [https://github.com/YourUsername/health-guide-app.git](https://github.com/YourUsername/health-guide-app.git)
    cd health-guide-app
    ```

2.  **Run the application:**

    ```bash
    python your_script_name.py
    ```

    *(Replace `your_script_name.py` with the actual name of your Python file, e.g., `health_calculator.py`)*

## 🛠️ Usage

1.  **Launch the Application:** Run the script as shown in the installation steps.
2.  **Input Data:** Enter your personal metrics:
    * **Age** (must be 18 or older for specific sleep advice)
    * **Height** (in centimeters)
    * **Weight** (in kilograms)
    * **Sleep Hours** (average hours slept per night)
3.  **Select Options:** Choose your **Activity Level** and **Smoking Status** from the dropdown menus.
4.  **Generate Report:** Click the **"Generate Recommendations"** button.
5.  **View Results:** The report area will display your calculated BMI, category, and a detailed set of personalized health and lifestyle recommendations.

## 📐 BMI Formula

The Body Mass Index is calculated using the formula:

$$BMI = \frac{weight\,(kg)}{height^2\,(m^2)}$$

The application automatically converts the height input from centimeters (cm) to meters (m) before calculation.

## 🛑 Disclaimer

**This application is for informational and educational purposes only.** The health metrics and recommendations provided are based on general public health guidelines (WHO, National Sleep Foundation, etc.). It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a physician or other qualified health provider with any questions you may have regarding a medical condition or before making any major changes to your diet or exercise routine.
