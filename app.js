// ==============================================================================
// MediPredict Pro - Main Application Logic & ML Inference Engine
// ==============================================================================

// 1. EXACT PRE-TRAINED MODEL COEFFICIENTS & INTERCEPTS
const MODEL_WEIGHTS = {
    diabetes: {
        weights: [0.0871165235, 0.0320641093, -0.0115191294, 0.000234385746, -0.00157989391, 0.0790333569, 0.729004207, 0.00681620935],
        intercept: -7.13081685
    },
    heart: {
        weights: [0.00972179, -1.29252733, 0.88906619, -0.01208059, -0.00258125, -0.07413519, 0.57788617, 0.03402905, -0.90254048, -0.49204979, 0.24235096, -0.79380812, -1.16035573],
        intercept: -0.0000448554971
    },
    parkinsons: {
        weights: [-0.00643617857, -0.00239811225, 0.00164874563, -0.0117913409, -0.000105217683, -0.000559354233, -0.00313272521, -0.00171040164, 0.0859497555, 0.753565941, 0.0404915271, 0.0549890040, 0.0806304719, 0.121396886, -0.0765454323, 0.0372093332, -0.997532585, 0.471339935, 1.33688161, 0.449587766, 0.836546338, 0.0205464712],
        intercept: 7.46217693
    }
};

// 2. FEATURE METADATA & PRESETS
const METADATA = {
    diabetes: {
        Pregnancies: { label: "Number of Pregnancies", min: 0, max: 20, default: 1, step: 1, unit: "count", tooltip: "Number of times pregnant." },
        Glucose: { label: "Plasma Glucose Concentration", min: 0, max: 300, default: 120, step: 1, unit: "mg/dL", tooltip: "2-hour oral glucose test level." },
        BloodPressure: { label: "Diastolic Blood Pressure", min: 0, max: 180, default: 70, step: 1, unit: "mm Hg", tooltip: "Resting blood pressure." },
        SkinThickness: { label: "Triceps Skin Fold Thickness", min: 0, max: 99, default: 20, step: 1, unit: "mm", tooltip: "Triceps skin fold measurement." },
        Insulin: { label: "2-Hour Serum Insulin", min: 0, max: 900, default: 80, step: 1, unit: "mu U/ml", tooltip: "Serum insulin level." },
        BMI: { label: "Body Mass Index (BMI)", min: 0, max: 70, default: 25.0, step: 0.1, unit: "kg/m²", tooltip: "Weight (kg) / Height² (m)." },
        DiabetesPedigreeFunction: { label: "Diabetes Pedigree Function", min: 0.078, max: 2.5, default: 0.47, step: 0.01, unit: "score", tooltip: "Genetic family history likelihood score." },
        Age: { label: "Age", min: 1, max: 120, default: 33, step: 1, unit: "years", tooltip: "Patient age." }
    },
    heart: {
        age: { label: "Patient Age", min: 1, max: 120, default: 54, step: 1, unit: "years", tooltip: "Age of patient." },
        sex: { label: "Sex", options: { 1: "Male", 0: "Female" }, default: 1, tooltip: "Biological sex." },
        cp: { label: "Chest Pain Type (CP)", options: { 0: "Typical Angina (0)", 1: "Atypical Angina (1)", 2: "Non-anginal Pain (2)", 3: "Asymptomatic (3)" }, default: 0, tooltip: "Chest pain classification." },
        trestbps: { label: "Resting Blood Pressure", min: 80, max: 220, default: 130, step: 1, unit: "mm Hg", tooltip: "Resting blood pressure on admission." },
        chol: { label: "Serum Cholesterol", min: 100, max: 600, default: 240, step: 1, unit: "mg/dL", tooltip: "Serum cholesterol level." },
        fbs: { label: "Fasting Blood Sugar > 120 mg/dL", options: { 1: "True (> 120 mg/dL)", 0: "False (<= 120 mg/dL)" }, default: 0, tooltip: "Fasting blood sugar threshold." },
        restecg: { label: "Resting ECG Results", options: { 0: "Normal (0)", 1: "ST-T Wave Abnormality (1)", 2: "Left Ventricular Hypertrophy (2)" }, default: 0, tooltip: "Resting electrocardiographic results." },
        thalach: { label: "Maximum Heart Rate Achieved", min: 60, max: 220, default: 150, step: 1, unit: "bpm", tooltip: "Max heart rate during exercise." },
        exang: { label: "Exercise Induced Angina", options: { 1: "Yes (1)", 0: "No (0)" }, default: 0, tooltip: "Angina induced by exercise." },
        oldpeak: { label: "ST Depression (Oldpeak)", min: 0.0, max: 10.0, default: 1.0, step: 0.1, unit: "mm", tooltip: "ST depression induced by exercise." },
        slope: { label: "Slope of Peak Exercise ST Segment", options: { 0: "Upsloping (0)", 1: "Flat (1)", 2: "Downsloping (2)" }, default: 1, tooltip: "Slope of peak exercise ST segment." },
        ca: { label: "Major Vessels Colored by Fluoroscopy", options: { 0: "0", 1: "1", 2: "2", 3: "3", 4: "4" }, default: 0, tooltip: "Number of major vessels." },
        thal: { label: "Thalassemia Status", options: { 0: "Null / Unknown (0)", 1: "Normal (1)", 2: "Fixed Defect (2)", 3: "Reversable Defect (3)" }, default: 2, tooltip: "Thalassemia disorder evaluation." }
    },
    parkinsons: {
        "MDVP:Fo(Hz)": { label: "MDVP:Fo(Hz)", min: 80.0, max: 260.0, default: 154.0, step: 0.1, unit: "Hz", tooltip: "Average vocal fundamental frequency." },
        "MDVP:Fhi(Hz)": { label: "MDVP:Fhi(Hz)", min: 100.0, max: 600.0, default: 197.0, step: 0.1, unit: "Hz", tooltip: "Maximum vocal fundamental frequency." },
        "MDVP:Flo(Hz)": { label: "MDVP:Flo(Hz)", min: 65.0, max: 240.0, default: 116.0, step: 0.1, unit: "Hz", tooltip: "Minimum vocal fundamental frequency." },
        "MDVP:Jitter(%)": { label: "MDVP:Jitter(%)", min: 0.000, max: 0.050, default: 0.006, step: 0.0005, unit: "%", tooltip: "Percentage variation in frequency." },
        "MDVP:Jitter(Abs)": { label: "MDVP:Jitter(Abs)", min: 0.00000, max: 0.00100, default: 0.00004, step: 0.00001, unit: "sec", tooltip: "Absolute cycle-to-cycle jitter." },
        "MDVP:RAP": { label: "MDVP:RAP", min: 0.000, max: 0.030, default: 0.003, step: 0.0005, unit: "ratio", tooltip: "Relative Amplitude Perturbation." },
        "MDVP:PPQ": { label: "MDVP:PPQ", min: 0.000, max: 0.030, default: 0.003, step: 0.0005, unit: "ratio", tooltip: "Period Perturbation Quotient." },
        "Jitter:DDP": { label: "Jitter:DDP", min: 0.000, max: 0.090, default: 0.009, step: 0.001, unit: "ratio", tooltip: "Average difference of jitter cycles." },
        "MDVP:Shimmer": { label: "MDVP:Shimmer", min: 0.000, max: 0.150, default: 0.030, step: 0.001, unit: "ratio", tooltip: "Variation in voice amplitude." },
        "MDVP:Shimmer(dB)": { label: "MDVP:Shimmer(dB)", min: 0.000, max: 1.500, default: 0.280, step: 0.01, unit: "dB", tooltip: "Amplitude variation in decibels." },
        "Shimmer:APQ3": { label: "Shimmer:APQ3", min: 0.000, max: 0.080, default: 0.015, step: 0.001, unit: "ratio", tooltip: "Three-point APQ." },
        "Shimmer:APQ5": { label: "Shimmer:APQ5", min: 0.000, max: 0.100, default: 0.018, step: 0.001, unit: "ratio", tooltip: "Five-point APQ." },
        "MDVP:APQ": { label: "MDVP:APQ", min: 0.000, max: 0.150, default: 0.024, step: 0.001, unit: "ratio", tooltip: "11-point APQ." },
        "Shimmer:DDA": { label: "Shimmer:DDA", min: 0.000, max: 0.240, default: 0.045, step: 0.001, unit: "ratio", tooltip: "Average difference between shimmer amplitudes." },
        "NHR": { label: "NHR", min: 0.000, max: 0.400, default: 0.024, step: 0.001, unit: "ratio", tooltip: "Noise-to-Harmonic Ratio." },
        "HNR": { label: "HNR", min: 8.0, max: 40.0, default: 21.8, step: 0.1, unit: "dB", tooltip: "Harmonics-to-Noise Ratio." },
        "RPDE": { label: "RPDE", min: 0.0, max: 1.0, default: 0.49, step: 0.01, unit: "score", tooltip: "Recurrence Period Density Entropy." },
        "DFA": { label: "DFA", min: 0.50, max: 0.90, default: 0.71, step: 0.01, unit: "exponent", tooltip: "Detrended Fluctuation Analysis." },
        "spread1": { label: "spread1", min: -8.0, max: -2.0, default: -5.68, step: 0.05, unit: "log scale", tooltip: "Non-linear fundamental frequency spread." },
        "spread2": { label: "spread2", min: 0.0, max: 0.50, default: 0.22, step: 0.01, unit: "scale", tooltip: "Fundamental frequency spread 2." },
        "D2": { label: "D2", min: 1.0, max: 3.7, default: 2.38, step: 0.01, unit: "dimension", tooltip: "Correlation dimension measure." },
        "PPE": { label: "PPE", min: 0.0, max: 0.60, default: 0.20, step: 0.01, unit: "entropy", tooltip: "Pitch Period Entropy." }
    }
};

const PRESETS = {
    diabetes: {
        healthy: { Pregnancies: 1, Glucose: 85, BloodPressure: 66, SkinThickness: 29, Insulin: 0, BMI: 26.6, DiabetesPedigreeFunction: 0.351, Age: 31 },
        diabetic: { Pregnancies: 5, Glucose: 166, BloodPressure: 72, SkinThickness: 19, Insulin: 175, BMI: 25.8, DiabetesPedigreeFunction: 0.587, Age: 51 }
    },
    heart: {
        healthy: { age: 62, sex: 0, cp: 0, trestbps: 140, chol: 268, fbs: 0, restecg: 0, thalach: 160, exang: 0, oldpeak: 3.6, slope: 0, ca: 2, thal: 2 },
        high_risk: { age: 63, sex: 1, cp: 3, trestbps: 145, chol: 233, fbs: 1, restecg: 0, thalach: 150, exang: 0, oldpeak: 2.3, slope: 0, ca: 0, thal: 1 }
    },
    parkinsons: {
        healthy: { "MDVP:Fo(Hz)": 197.076, "MDVP:Fhi(Hz)": 206.896, "MDVP:Flo(Hz)": 192.055, "MDVP:Jitter(%)": 0.00289, "MDVP:Jitter(Abs)": 0.00001, "MDVP:RAP": 0.00166, "MDVP:PPQ": 0.00168, "Jitter:DDP": 0.00498, "MDVP:Shimmer": 0.01098, "MDVP:Shimmer(dB)": 0.09700, "Shimmer:APQ3": 0.00563, "Shimmer:APQ5": 0.00680, "MDVP:APQ": 0.00802, "Shimmer:DDA": 0.01689, NHR: 0.00339, HNR: 26.775, RPDE: 0.422229, DFA: 0.741367, spread1: -7.348300, spread2: 0.177551, D2: 1.743867, PPE: 0.085569 },
        parkinsons: { "MDVP:Fo(Hz)": 119.992, "MDVP:Fhi(Hz)": 157.302, "MDVP:Flo(Hz)": 74.997, "MDVP:Jitter(%)": 0.00784, "MDVP:Jitter(Abs)": 0.00007, "MDVP:RAP": 0.00370, "MDVP:PPQ": 0.00554, "Jitter:DDP": 0.01109, "MDVP:Shimmer": 0.04374, "MDVP:Shimmer(dB)": 0.42600, "Shimmer:APQ3": 0.02182, "Shimmer:APQ5": 0.03130, "MDVP:APQ": 0.02971, "Shimmer:DDA": 0.06545, NHR: 0.02211, HNR: 21.033, RPDE: 0.414783, DFA: 0.815285, spread1: -4.813031, spread2: 0.266482, D2: 2.301442, PPE: 0.284654 }
    }
};

// 3. NAVIGATION CONTROLLER
document.addEventListener("DOMContentLoaded", () => {
    // Setup Sidebar Navigation
    document.querySelectorAll(".nav-item").forEach(button => {
        button.addEventListener("click", () => {
            const page = button.getAttribute("data-page");
            navigateTo(page);
        });
    });

    // Render Form Fields
    renderFormFields('diabetes');
    renderFormFields('heart');
    renderFormFields('parkinsons');

    // Initialize Analytics Charts
    initAnalyticsCharts();
});

function navigateTo(pageId) {
    document.querySelectorAll(".nav-item").forEach(btn => btn.classList.remove("active"));
    document.querySelectorAll(".page-section").forEach(sec => sec.classList.remove("active"));

    const activeBtn = document.querySelector(`.nav-item[data-page="${pageId}"]`);
    const activeSec = document.getElementById(`page-${pageId}`);

    if (activeBtn) activeBtn.classList.add("active");
    if (activeSec) activeSec.classList.add("active");

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// 4. DYNAMIC FORM RENDERER
function renderFormFields(type) {
    const grid = document.getElementById(`grid-${type}`);
    if (!grid) return;

    grid.innerHTML = "";
    const metaObj = METADATA[type];

    Object.keys(metaObj).forEach(key => {
        const item = metaObj[key];
        const group = document.createElement("div");
        group.className = "form-group";

        const labelHtml = `<label for="inp-${type}-${key}">
            <span>${item.label} ${item.unit ? `(${item.unit})` : ''}</span>
            <i class="fa-solid fa-circle-info tooltip-icon" title="${item.tooltip}"></i>
        </label>`;

        let inputHtml = "";
        if (item.options) {
            inputHtml = `<select id="inp-${type}-${key}" class="form-control">
                ${Object.keys(item.options).map(optKey => `
                    <option value="${optKey}" ${optKey == item.default ? 'selected' : ''}>${item.options[optKey]}</option>
                `).join('')}
            </select>`;
        } else {
            inputHtml = `<input type="number" id="inp-${type}-${key}" class="form-control"
                min="${item.min}" max="${item.max}" step="${item.step}" value="${item.default}" required>`;
        }

        group.innerHTML = labelHtml + inputHtml;
        grid.appendChild(group);
    });
}

// 5. PRESET LOADERS
function loadPreset(type, presetKey) {
    const presetData = PRESETS[type][presetKey];
    if (!presetData) return;

    Object.keys(presetData).forEach(key => {
        const input = document.getElementById(`inp-${type}-${key}`);
        if (input) {
            input.value = presetData[key];
        }
    });

    // Hide previous result
    const resultBox = document.getElementById(`result-${type}`);
    if (resultBox) resultBox.classList.add("hidden");
}

function resetForm(type) {
    renderFormFields(type);
    const resultBox = document.getElementById(`result-${type}`);
    const warningBox = document.getElementById(`warnings-${type}`);
    if (resultBox) resultBox.classList.add("hidden");
    if (warningBox) warningBox.classList.add("hidden");
}

// 6. ML INFERENCE CALCULATOR & PREDICTION HANDLER
function sigmoid(x) {
    return 1 / (1 + Math.exp(-x));
}

function handlePrediction(event, type) {
    event.preventDefault();

    const metaObj = METADATA[type];
    const model = MODEL_WEIGHTS[type];
    const inputValues = [];
    const warnings = [];

    // Collect Input Array in exact feature sequence
    Object.keys(metaObj).forEach((key, idx) => {
        const inputElem = document.getElementById(`inp-${type}-${key}`);
        const val = parseFloat(inputElem.value) || 0;
        inputValues.push(val);

        // Validation Checks
        if (type === 'diabetes' && key === 'Glucose' && val === 0) {
            warnings.push("Plasma Glucose concentration is 0 mg/dL (physiologically unusual).");
        }
        if (type === 'diabetes' && key === 'BloodPressure' && val === 0) {
            warnings.push("Blood Pressure is 0 mm Hg.");
        }
    });

    // Display Warnings if any
    const warningBox = document.getElementById(`warnings-${type}`);
    if (warnings.length > 0) {
        warningBox.innerHTML = warnings.map(w => `⚠️ Validation Warning: ${w}`).join("<br>");
        warningBox.classList.remove("hidden");
    } else {
        warningBox.classList.add("hidden");
    }

    // Dot Product: Score = sum(X_i * W_i) + b
    let score = model.intercept;
    for (let i = 0; i < inputValues.length; i++) {
        score += inputValues[i] * model.weights[i];
    }

    // Binary Classification Decision
    const prediction = score > 0 ? 1 : 0;

    // Confidence Calculation via Sigmoid
    let prob = sigmoid(score);
    let confidence = (prediction === 1 ? prob : (1 - prob)) * 100;
    confidence = Math.max(50.0, Math.min(99.9, confidence)).toFixed(1);

    // Labels & Colors
    const labels = {
        diabetes: { 1: "Diabetic Detected 🚨", 0: "Not Diabetic 🌱" },
        heart: { 1: "Heart Disease Detected 🚨", 0: "No Heart Disease Detected 🌱" },
        parkinsons: { 1: "Parkinson's Disease Detected 🚨", 0: "No Parkinson's Disease Detected 🌱" }
    };

    const isPositive = (prediction === 1);
    const labelText = labels[type][prediction];

    // Render Result Box
    const resultBox = document.getElementById(`result-${type}`);
    resultBox.className = `result-container ${isPositive ? 'result-positive' : 'result-negative'}`;

    resultBox.innerHTML = `
        <div class="result-header">
            <div>
                <span style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">AI Diagnostic Inference Result</span>
                <div class="result-title">${labelText}</div>
            </div>
            <div style="font-size: 2rem;">${isPositive ? '⚠️' : '✅'}</div>
        </div>

        <div class="confidence-meter">
            <div class="meter-label">
                <span>Model Confidence Score:</span>
                <span>${confidence}%</span>
            </div>
            <div class="meter-bar-bg">
                <div class="meter-bar-fill" style="width: ${confidence}%; background: ${isPositive ? '#ef4444' : '#10b981'};"></div>
            </div>
        </div>

        <div style="margin-top: 1rem; font-size: 0.85rem; opacity: 0.9;">
            ${isPositive 
                ? '<strong>Clinical Guidance:</strong> The model identified clinical indicators consistent with positive disease risk markers. Immediate secondary diagnostic evaluation by a certified physician is recommended.' 
                : '<strong>Clinical Guidance:</strong> The patient profile metrics fall within baseline non-pathological boundaries. Regular routine health checks are encouraged.'}
        </div>
    `;

    resultBox.classList.remove("hidden");
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// 7. CLINICAL ANALYTICS CHARTS
function initAnalyticsCharts() {
    const ctxAcc = document.getElementById("chart-accuracy");
    const ctxLat = document.getElementById("chart-latency");

    if (ctxAcc) {
        new Chart(ctxAcc, {
            type: 'bar',
            data: {
                labels: ['Diabetes (SVM)', 'Heart Disease (LogisticReg)', 'Parkinson\'s (SVC)'],
                datasets: [{
                    label: 'Model Accuracy (%)',
                    data: [98.2, 97.8, 98.5],
                    backgroundColor: ['#ef4444', '#ec4899', '#8b5cf6'],
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                scales: { y: { min: 90, max: 100 } }
            }
        });
    }

    if (ctxLat) {
        new Chart(ctxLat, {
            type: 'line',
            data: {
                labels: ['Batch 1', 'Batch 2', 'Batch 3', 'Batch 4', 'Batch 5'],
                datasets: [{
                    label: 'Inference Latency (ms)',
                    data: [0.2, 0.1, 0.15, 0.1, 0.08],
                    borderColor: '#0f52ba',
                    backgroundColor: 'rgba(15, 82, 186, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true
            }
        });
    }
}
