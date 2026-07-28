"""
Feature metadata, feature ranges, medical tooltips, and sample patient presets for Multi Disease Prediction.
"""

# ==============================================================================
# DIABETES FEATURE METADATA
# ==============================================================================
DIABETES_METADATA = {
    "Pregnancies": {
        "label": "Number of Pregnancies",
        "min": 0, "max": 20, "default": 1, "step": 1,
        "unit": "count",
        "tooltip": "Number of times pregnant (Pima Indian Diabetes dataset metric)."
    },
    "Glucose": {
        "label": "Plasma Glucose Concentration",
        "min": 0, "max": 300, "default": 120, "step": 1,
        "unit": "mg/dL",
        "tooltip": "Plasma glucose concentration after a 2 hours oral glucose tolerance test. Normal fasting level is <100 mg/dL."
    },
    "BloodPressure": {
        "label": "Diastolic Blood Pressure",
        "min": 0, "max": 180, "default": 70, "step": 1,
        "unit": "mm Hg",
        "tooltip": "Diastolic blood pressure. Normal range is typically 60-80 mm Hg."
    },
    "SkinThickness": {
        "label": "Triceps Skin Fold Thickness",
        "min": 0, "max": 99, "default": 20, "step": 1,
        "unit": "mm",
        "tooltip": "Triceps skin fold thickness used to estimate body fat percentage."
    },
    "Insulin": {
        "label": "2-Hour Serum Insulin",
        "min": 0, "max": 900, "default": 80, "step": 1,
        "unit": "mu U/ml",
        "tooltip": "2-Hour serum insulin level. Elevated levels indicate insulin resistance."
    },
    "BMI": {
        "label": "Body Mass Index (BMI)",
        "min": 0.0, "max": 70.0, "default": 25.0, "step": 0.1,
        "unit": "kg/m²",
        "tooltip": "Weight in kg divided by height in meters squared. Normal BMI range is 18.5 - 24.9."
    },
    "DiabetesPedigreeFunction": {
        "label": "Diabetes Pedigree Function",
        "min": 0.078, "max": 2.5, "default": 0.47, "step": 0.01,
        "unit": "score",
        "tooltip": "Genetic score estimating diabetes likelihood based on family history."
    },
    "Age": {
        "label": "Age",
        "min": 1, "max": 120, "default": 33, "step": 1,
        "unit": "years",
        "tooltip": "Patient age in years."
    }
}

DIABETES_PRESETS = {
    "Healthy Female Patient": {
        "Pregnancies": 1, "Glucose": 85, "BloodPressure": 66, "SkinThickness": 29,
        "Insulin": 0, "BMI": 26.6, "DiabetesPedigreeFunction": 0.351, "Age": 31
    },
    "Diabetic Female Patient": {
        "Pregnancies": 5, "Glucose": 166, "BloodPressure": 72, "SkinThickness": 19,
        "Insulin": 175, "BMI": 25.8, "DiabetesPedigreeFunction": 0.587, "Age": 51
    }
}

# ==============================================================================
# HEART DISEASE FEATURE METADATA
# ==============================================================================
HEART_METADATA = {
    "age": {
        "label": "Patient Age",
        "min": 1, "max": 120, "default": 54, "step": 1,
        "unit": "years",
        "tooltip": "Age of the patient in years."
    },
    "sex": {
        "label": "Sex",
        "options": {1: "Male", 0: "Female"},
        "default": 1,
        "tooltip": "Biological sex of the patient."
    },
    "cp": {
        "label": "Chest Pain Type (CP)",
        "options": {
            0: "Typical Angina (0)",
            1: "Atypical Angina (1)",
            2: "Non-anginal Pain (2)",
            3: "Asymptomatic (3)"
        },
        "default": 0,
        "tooltip": "Type of chest pain reported by the patient."
    },
    "trestbps": {
        "label": "Resting Blood Pressure",
        "min": 80, "max": 220, "default": 130, "step": 1,
        "unit": "mm Hg",
        "tooltip": "Resting blood pressure upon hospital admission."
    },
    "chol": {
        "label": "Serum Cholesterol",
        "min": 100, "max": 600, "default": 240, "step": 1,
        "unit": "mg/dL",
        "tooltip": "Serum cholesterol in mg/dL. Desirable levels are below 200 mg/dL."
    },
    "fbs": {
        "label": "Fasting Blood Sugar > 120 mg/dL",
        "options": {1: "True (> 120 mg/dL)", 0: "False (<= 120 mg/dL)"},
        "default": 0,
        "tooltip": "Fasting blood sugar level relative to 120 mg/dL threshold."
    },
    "restecg": {
        "label": "Resting Electrocardiographic Results",
        "options": {
            0: "Normal (0)",
            1: "ST-T Wave Abnormality (1)",
            2: "Left Ventricular Hypertrophy (2)"
        },
        "default": 0,
        "tooltip": "Resting ECG evaluation results."
    },
    "thalach": {
        "label": "Maximum Heart Rate Achieved",
        "min": 60, "max": 220, "default": 150, "step": 1,
        "unit": "bpm",
        "tooltip": "Maximum heart rate achieved during exercise stress testing."
    },
    "exang": {
        "label": "Exercise Induced Angina",
        "options": {1: "Yes (1)", 0: "No (0)"},
        "default": 0,
        "tooltip": "Occurrence of angina induced by exercise."
    },
    "oldpeak": {
        "label": "ST Depression (Oldpeak)",
        "min": 0.0, "max": 10.0, "default": 1.0, "step": 0.1,
        "unit": "mm",
        "tooltip": "ST depression induced by exercise relative to rest."
    },
    "slope": {
        "label": "Slope of Peak Exercise ST Segment",
        "options": {
            0: "Upsloping (0)",
            1: "Flat (1)",
            2: "Downsloping (2)"
        },
        "default": 1,
        "tooltip": "The slope of the peak exercise ST segment."
    },
    "ca": {
        "label": "Major Vessels Colored by Flourosopy",
        "options": {0: "0", 1: "1", 2: "2", 3: "3", 4: "4"},
        "default": 0,
        "tooltip": "Number of major vessels (0-4) colored by fluoroscopy."
    },
    "thal": {
        "label": "Thalassemia Status",
        "options": {
            0: "Null / Unknown (0)",
            1: "Normal (1)",
            2: "Fixed Defect (2)",
            3: "Reversable Defect (3)"
        },
        "default": 2,
        "tooltip": "Thalassemia blood disorder evaluation."
    }
}

HEART_PRESETS = {
    "Healthy Patient Profile": {
        "age": 62, "sex": 0, "cp": 0, "trestbps": 140, "chol": 268, "fbs": 0,
        "restecg": 0, "thalach": 160, "exang": 0, "oldpeak": 3.6, "slope": 0, "ca": 2, "thal": 2
    },
    "High Risk Patient Profile": {
        "age": 63, "sex": 1, "cp": 3, "trestbps": 145, "chol": 233, "fbs": 1,
        "restecg": 0, "thalach": 150, "exang": 0, "oldpeak": 2.3, "slope": 0, "ca": 0, "thal": 1
    }
}

# ==============================================================================
# PARKINSON'S DISEASE FEATURE METADATA
# ==============================================================================
PARKINSONS_METADATA = {
    "MDVP:Fo(Hz)": {"label": "MDVP:Fo(Hz)", "min": 80.0, "max": 260.0, "default": 154.0, "step": 0.1, "unit": "Hz", "tooltip": "Average vocal fundamental frequency."},
    "MDVP:Fhi(Hz)": {"label": "MDVP:Fhi(Hz)", "min": 100.0, "max": 600.0, "default": 197.0, "step": 0.1, "unit": "Hz", "tooltip": "Maximum vocal fundamental frequency."},
    "MDVP:Flo(Hz)": {"label": "MDVP:Flo(Hz)", "min": 65.0, "max": 240.0, "default": 116.0, "step": 0.1, "unit": "Hz", "tooltip": "Minimum vocal fundamental frequency."},
    "MDVP:Jitter(%)": {"label": "MDVP:Jitter(%)", "min": 0.000, "max": 0.050, "default": 0.006, "step": 0.0005, "unit": "%", "tooltip": "Percentage variation in fundamental frequency."},
    "MDVP:Jitter(Abs)": {"label": "MDVP:Jitter(Abs)", "min": 0.00000, "max": 0.00100, "default": 0.00004, "step": 0.00001, "unit": "sec", "tooltip": "Absolute cycle-to-cycle jitter in seconds."},
    "MDVP:RAP": {"label": "MDVP:RAP", "min": 0.000, "max": 0.030, "default": 0.003, "step": 0.0005, "unit": "ratio", "tooltip": "Relative Amplitude Perturbation."},
    "MDVP:PPQ": {"label": "MDVP:PPQ", "min": 0.000, "max": 0.030, "default": 0.003, "step": 0.0005, "unit": "ratio", "tooltip": "Five-point Period Perturbation Quotient."},
    "Jitter:DDP": {"label": "Jitter:DDP", "min": 0.000, "max": 0.090, "default": 0.009, "step": 0.001, "unit": "ratio", "tooltip": "Average absolute difference of differences between jitter cycles."},
    "MDVP:Shimmer": {"label": "MDVP:Shimmer", "min": 0.000, "max": 0.150, "default": 0.030, "step": 0.001, "unit": "ratio", "tooltip": "Variation in voice amplitude."},
    "MDVP:Shimmer(dB)": {"label": "MDVP:Shimmer(dB)", "min": 0.000, "max": 1.500, "default": 0.280, "step": 0.01, "unit": "dB", "tooltip": "Amplitude variation in decibels."},
    "Shimmer:APQ3": {"label": "Shimmer:APQ3", "min": 0.000, "max": 0.080, "default": 0.015, "step": 0.001, "unit": "ratio", "tooltip": "Three-point Amplitude Perturbation Quotient."},
    "Shimmer:APQ5": {"label": "Shimmer:APQ5", "min": 0.000, "max": 0.100, "default": 0.018, "step": 0.001, "unit": "ratio", "tooltip": "Five-point Amplitude Perturbation Quotient."},
    "MDVP:APQ": {"label": "MDVP:APQ", "min": 0.000, "max": 0.150, "default": 0.024, "step": 0.001, "unit": "ratio", "tooltip": "11-point Amplitude Perturbation Quotient."},
    "Shimmer:DDA": {"label": "Shimmer:DDA", "min": 0.000, "max": 0.240, "default": 0.045, "step": 0.001, "unit": "ratio", "tooltip": "Average absolute difference between consecutive shimmer amplitudes."},
    "NHR": {"label": "NHR", "min": 0.000, "max": 0.400, "default": 0.024, "step": 0.001, "unit": "ratio", "tooltip": "Noise-to-Harmonic Ratio in voice signal."},
    "HNR": {"label": "HNR", "min": 8.0, "max": 40.0, "default": 21.8, "step": 0.1, "unit": "dB", "tooltip": "Harmonics-to-Noise Ratio. Higher is cleaner vocal tone."},
    "RPDE": {"label": "RPDE", "min": 0.0, "max": 1.0, "default": 0.49, "step": 0.01, "unit": "score", "tooltip": "Recurrence Period Density Entropy measure of non-linear complexity."},
    "DFA": {"label": "DFA", "min": 0.50, "max": 0.90, "default": 0.71, "step": 0.01, "unit": "exponent", "tooltip": "Detrended Fluctuation Analysis signal exponent."},
    "spread1": {"label": "spread1", "min": -8.0, "max": -2.0, "default": -5.68, "step": 0.05, "unit": "log scale", "tooltip": "Non-linear measure of fundamental frequency variation."},
    "spread2": {"label": "spread2", "min": 0.0, "max": 0.50, "default": 0.22, "step": 0.01, "unit": "scale", "tooltip": "Non-linear measure of fundamental frequency variation."},
    "D2": {"label": "D2", "min": 1.0, "max": 3.7, "default": 2.38, "step": 0.01, "unit": "dimension", "tooltip": "Correlation dimension measure of vocal signal complexity."},
    "PPE": {"label": "PPE", "min": 0.0, "max": 0.60, "default": 0.20, "step": 0.01, "unit": "entropy", "tooltip": "Pitch Period Entropy measure."}
}

PARKINSONS_PRESETS = {
    "Healthy Subject Sample": {
        "MDVP:Fo(Hz)": 197.076, "MDVP:Fhi(Hz)": 206.896, "MDVP:Flo(Hz)": 192.055,
        "MDVP:Jitter(%)": 0.00289, "MDVP:Jitter(Abs)": 0.00001, "MDVP:RAP": 0.00166,
        "MDVP:PPQ": 0.00168, "Jitter:DDP": 0.00498, "MDVP:Shimmer": 0.01098,
        "MDVP:Shimmer(dB)": 0.09700, "Shimmer:APQ3": 0.00563, "Shimmer:APQ5": 0.00680,
        "MDVP:APQ": 0.00802, "Shimmer:DDA": 0.01689, "NHR": 0.00339, "HNR": 26.775,
        "RPDE": 0.422229, "DFA": 0.741367, "spread1": -7.348300, "spread2": 0.177551,
        "D2": 1.743867, "PPE": 0.085569
    },
    "Parkinson's Subject Sample": {
        "MDVP:Fo(Hz)": 119.992, "MDVP:Fhi(Hz)": 157.302, "MDVP:Flo(Hz)": 74.997,
        "MDVP:Jitter(%)": 0.00784, "MDVP:Jitter(Abs)": 0.00007, "MDVP:RAP": 0.00370,
        "MDVP:PPQ": 0.00554, "Jitter:DDP": 0.01109, "MDVP:Shimmer": 0.04374,
        "MDVP:Shimmer(dB)": 0.42600, "Shimmer:APQ3": 0.02182, "Shimmer:APQ5": 0.03130,
        "MDVP:APQ": 0.02971, "Shimmer:DDA": 0.06545, "NHR": 0.02211, "HNR": 21.033,
        "RPDE": 0.414783, "DFA": 0.815285, "spread1": -4.813031, "spread2": 0.266482,
        "D2": 2.301442, "PPE": 0.284654
    }
}
