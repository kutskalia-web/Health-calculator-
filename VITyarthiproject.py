import tkinter as tk
from tkinter import ttk, messagebox
import math

# --- Constants for Health Metrics ---

# Standard BMI categories (WHO/CDC)
BMI_CATEGORIES = {
    'Underweight': (0.0, 18.5),
    'Normal weight': (18.5, 25.0),
    'Overweight': (25.0, 30.0),
    'Obesity': (30.0, float('inf'))
}

# General Sleep Recommendations by Age (National Sleep Foundation)
# Key: (min_hours, max_hours)
SLEEP_RECOMMENDATIONS = {
    '18-64': (7, 9),
    '65+': (7, 8)
}

# --- Core Calculation Functions (Copied from previous file) ---

def calculate_bmi(weight_kg, height_m):
    """
    Calculates the Body Mass Index (BMI).
    Formula: weight (kg) / [height (m)]^2
    """
    if height_m <= 0:
        return 0.0
    try:
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 2)
    except (TypeError, ValueError):
        return 0.0

def get_bmi_category(bmi):
    """
    Determines the BMI category based on the calculated BMI value.
    """
    for category, (min_val, max_val) in BMI_CATEGORIES.items():
        if min_val <= bmi < max_val:
            return category, min_val, max_val
    return "Unknown", 0.0, 0.0

def get_bmi_explanation(category):
    """
    Provides a simple explanation of what the BMI category means.
    """
    explanations = {
        'Underweight': "This range suggests you may not be consuming enough nutrients or calories. Consult a professional for healthy weight gain strategies.",
        'Normal weight': "Your weight is considered healthy relative to your height, indicating a lower risk of common obesity-related diseases.",
        'Overweight': "This range indicates carrying excess weight. A focus on diet and increased activity is recommended to reduce health risks.",
        'Obesity': "This range is associated with a significantly increased risk for serious health conditions. Professional consultation for a weight management plan is strongly advised.",
        'Unknown': "Could not determine a standard BMI meaning."
    }
    return explanations.get(category, explanations['Unknown'])


# --- Recommendation Functions (Copied from previous file) ---

def get_sleep_feedback(age, hours):
    """ Provides specific sleep recommendations based on age and hours slept. """
    if 18 <= age <= 64:
        age_group = '18-64'
    elif age >= 65:
        age_group = '65+'
    else:
        return "Note: Specific recommendations for minors/children are not included in this model."

    min_h, max_h = SLEEP_RECOMMENDATIONS[age_group]

    if hours < min_h:
        return (
            f"You slept {hours} hours, which is less than the recommended {min_h}-{max_h} hours for your age group ({age_group}). "
            "Recommendation: Try to prioritize an earlier bedtime and aim for a consistent sleep schedule to improve rest and focus."
        )
    elif hours > max_h:
        return (
            f"You slept {hours} hours, which is slightly more than the recommended {min_h}-{max_h} hours for your age group ({age_group}). "
            "Recommendation: Excessive sleep can sometimes indicate underlying issues. If this is unusual, review your daily routine for consistent sleep quality."
        )
    else:
        return (
            f"Excellent! Your sleep of {hours} hours falls perfectly within the recommended {min_h}-{max_h} hour range. "
            "Recommendation: Maintain this consistent sleep pattern for optimal health."
        )

def get_activity_feedback(activity_level_str):
    """ Provides feedback based on the user's reported activity level. """
    if activity_level_str == 'Sedentary':
        return (
            "Sedentary Lifestyle Detected. Recommendation: Aim to break up long periods of sitting (e.g., stand up every hour). "
            "Start with 30 minutes of light activity (like walking) daily and gradually increase intensity to moderate."
        )
    elif activity_level_str == 'Moderate':
        return (
            "Moderate Activity Level. Recommendation: You are meeting minimum guidelines! "
            "To maximize benefits, ensure you incorporate strength training (2-3 times per week) alongside your cardio for muscle and bone health."
        )
    elif activity_level_str == 'Active':
        return (
            "Active Lifestyle! Recommendation: Excellent work. To prevent injury and fatigue, ensure proper recovery time, nutrition, and hydration. "
            "Consider mixing up your routines to engage different muscle groups."
        )
    return "Activity Recommendation: Could not determine specific advice."

def get_smoking_advice(smoking_status):
    """ Provides advice related to smoking status. """
    if smoking_status == 'Yes':
        return (
            "Smoking Status: Tobacco use is extremely detrimental to cardiovascular and respiratory health. "
            "Health Priority: Seek support to quit smoking immediately. Resources like quit-lines or medical professionals can provide vital assistance."
        )
    elif smoking_status == 'No':
        return (
            "Smoking Status: Non-smoker. Excellent! "
            "Recommendation: Maintain this status and avoid exposure to second-hand smoke to protect your long-term health."
        )
    return "Smoking Status: Unknown. Please confirm your smoking status for relevant advice."

def generate_health_recommendations(category):
    """ Provides general health and activity advice based on BMI category. """
    recommendations = [
        "General Wellness Tip: Aim for 5 servings of fruits and vegetables daily and minimize processed foods.",
        "Hydration Tip: Drink at least 8 glasses (about 2 liters) of water per day."
    ]

    if category == 'Underweight':
        recommendations.append(
            "Nutritional Focus: Consider nutrient-dense foods (healthy fats, lean proteins) and consult a professional about healthy ways to gain muscle and fat mass."
        )
    elif category == 'Normal weight':
        recommendations.append(
            "Maintenance Goal: Focus on consistency. Continue balancing a healthy diet with regular, varied exercise."
        )
    elif category == 'Overweight':
        recommendations.append(
            "Dietary Change: Prioritize whole foods and increase high-fiber, low-calorie options like vegetables. Focus on sustainable portion control."
        )
    elif category == 'Obesity':
        recommendations.append(
            "Health Priority: It is highly recommended to consult a healthcare provider for a personalized, safe, and effective plan. Focus on achievable, small, consistent changes."
        )

    return recommendations

# --- Tkinter GUI Implementation ---

class HealthCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Personalized Health Guide")
        master.geometry("800x650")
        master.resizable(False, False)
        
        # Configure style for a modern look
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f7f7f7')
        self.style.configure('TLabel', background='#f7f7f7', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10, 'bold'), padding=5)
        self.style.map('TButton', background=[('active', '#e6e6e6')])

        # Input Frame
        self.input_frame = ttk.Frame(master, padding="20 20 20 10", relief='flat')
        self.input_frame.pack(fill='x')

        # Results Frame (for output)
        self.results_frame = ttk.Frame(master, padding="10 10 10 10", relief='groove')
        self.results_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.results_text = tk.Text(self.results_frame, height=20, wrap='word', 
                                    font=('Courier New', 10), bg='#ffffff', bd=1, relief='sunken')
        self.results_text.pack(fill='both', expand=True)

        self.create_widgets()

    def create_widgets(self):
        # Dictionary to hold input variables and entry widgets
        self.input_vars = {}
        
        # Define the input fields and their labels
        input_fields = [
            ("Age (years, 18+)", "age", "int"),
            ("Height (cm)", "height_cm", "float"),
            ("Weight (kg)", "weight_kg", "float"),
            ("Sleep Hours (avg)", "sleep_hours", "float"),
        ]

        # Use a grid for cleaner input layout
        input_grid = ttk.Frame(self.input_frame, padding="5")
        input_grid.pack(fill='x', padx=10, pady=5)

        for i, (label, var_name, data_type) in enumerate(input_fields):
            ttk.Label(input_grid, text=label + ":").grid(row=i, column=0, sticky='w', padx=5, pady=3)
            
            var = tk.StringVar()
            entry = ttk.Entry(input_grid, textvariable=var, width=15)
            entry.grid(row=i, column=1, sticky='ew', padx=5, pady=3)
            self.input_vars[var_name] = var

        # ComboBox for Activity Level
        ttk.Label(input_grid, text="Activity Level:").grid(row=4, column=0, sticky='w', padx=5, pady=3)
        self.activity_var = tk.StringVar(value='Sedentary')
        self.activity_combo = ttk.Combobox(input_grid, textvariable=self.activity_var, width=13,
                                           values=['Sedentary', 'Moderate', 'Active'], state='readonly')
        self.activity_combo.grid(row=4, column=1, sticky='ew', padx=5, pady=3)
        
        # ComboBox for Smoking Status
        ttk.Label(input_grid, text="Smoking Status:").grid(row=5, column=0, sticky='w', padx=5, pady=3)
        self.smoking_var = tk.StringVar(value='No')
        self.smoking_combo = ttk.Combobox(input_grid, textvariable=self.smoking_var, width=13,
                                          values=['No', 'Yes'], state='readonly')
        self.smoking_combo.grid(row=5, column=1, sticky='ew', padx=5, pady=3)

        # Configure grid column weights
        input_grid.columnconfigure(1, weight=1)

        # Calculate Button
        self.calculate_button = ttk.Button(self.input_frame, text="Generate Recommendations", 
                                           command=self.calculate_health, style='Accent.TButton')
        self.calculate_button.pack(pady=10)
        
    def calculate_health(self):
        """ Gathers input, performs calculations, and updates the results text area. """
        
        self.results_text.delete(1.0, tk.END) # Clear previous results
        
        try:
            # 1. Gather and Validate Input
            age = int(self.input_vars['age'].get())
            height_cm = float(self.input_vars['height_cm'].get())
            weight_kg = float(self.input_vars['weight_kg'].get())
            sleep_hours = float(self.input_vars['sleep_hours'].get())
            activity_level_str = self.activity_var.get()
            smoking_status = self.smoking_var.get()
            
            if age <= 0 or height_cm <= 0 or weight_kg <= 0 or sleep_hours < 0:
                raise ValueError("All numerical inputs must be positive.")

        except ValueError as e:
            messagebox.showerror("Input Error", f"Please check your input values: {e}. Ensure Age, Height, Weight, and Sleep are valid numbers.")
            return
        
        # 2. Process Input
        height_m = height_cm / 100

        # 3. Calculate BMI
        bmi = calculate_bmi(weight_kg, height_m)
        category, min_val, max_val = get_bmi_category(bmi)
        bmi_meaning = get_bmi_explanation(category)
        
        # 4. Format Output Report
        report = ""
        report += "="*50 + "\n"
        report += "          COMPREHENSIVE HEALTH METRICS REPORT\n"
        report += "="*50 + "\n"
        report += f"Age: {age} years\n"
        report += f"Height: {height_cm:.1f} cm | Weight: {weight_kg:.1f} kg\n"
        report += "-" * 50 + "\n"
        report += f"Calculated BMI: {bmi:.2f}\n"
        report += f"BMI Category: {category}\n"
        report += f"(Ideal BMI Range: {min_val:.1f} to {max_val:.1f})\n"
        
        # BMI Overall Meaning Block
        report += "\n[ BMI Overall Meaning ]\n"
        report += f"-> {bmi_meaning}\n"
        report += "="*50 + "\n"

        # 5. Generate and Display Recommendations

        # Sleep Recommendation
        report += "\n[ Sleep Recommendation ]\n"
        sleep_advice = get_sleep_feedback(age, sleep_hours)
        report += f"-> {sleep_advice}\n"
        
        # Activity Recommendation
        report += "\n[ Activity Recommendation ]\n"
        activity_advice = get_activity_feedback(activity_level_str)
        report += f"-> {activity_advice}\n"
        
        # Smoking Advice
        report += "\n[ Smoking Status Advice ]\n"
        smoking_advice = get_smoking_advice(smoking_status)
        report += f"-> {smoking_advice}\n"

        # General Health & Diet Recommendation
        report += "\n[ General Health & Diet Suggestions ]\n"
        health_suggestions = generate_health_recommendations(category)
        for suggestion in health_suggestions:
            report += f"-> {suggestion}\n"

        # Update the results text area
        self.results_text.insert(tk.END, report)


if __name__ == "__main__":
    root = tk.Tk()
    app = HealthCalculatorApp(root)
    root.mainloop()