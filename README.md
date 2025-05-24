# 🏠 Streamlit Mortgage Calculator

This is a simple Streamlit web app that demonstrates the **basics of interactive UI development** with Python. The app calculates **monthly mortgage repayments** based on user inputs such as home value, deposit, interest rate, and loan term. It also displays a **repayment schedule** and a **line chart** showing the reduction of remaining balance over the years.

## 🚀 Features

- Real-time mortgage calculation
- Monthly, total repayment and total interest summary
- Dynamic amortisation schedule
- Visualisation of remaining balance over time using a line chart

---

## 📷 Screenshots

### 📌 Initial Input Section
This is where users enter the key details: home value, deposit, interest rate, and loan term. These inputs are used to calculate the loan amount and monthly repayments.

<img width="760" alt="Image" src="https://github.com/user-attachments/assets/2245e5f3-3d04-41e5-9f36-1f575c0a75c4" />

### 📌 Loan Balance Over Time Chart
This line chart visually represents how the remaining loan balance decreases each year, helping users understand how the mortgage is paid down over time.

<img width="754" alt="Image" src="https://github.com/user-attachments/assets/cb12cccd-370f-465b-bba1-1ee39141d955" />

### 📌 Detailed Repayment Table
An expandable table provides a detailed breakdown of monthly payments, showing how much goes towards principal and interest, along with the remaining balance.

<img width="749" alt="Image" src="https://github.com/user-attachments/assets/84f8a3ff-e9fe-4cfe-b3f5-7d187a006db0" />

---

## 🧮 How the App Works

1. User provides:
   - Home Value
   - Deposit
   - Interest Rate (% annual)
   - Loan Term (in years)

2. The app computes:
   - Loan Amount = Home Value - Deposit
   - Monthly Interest Rate
   - Number of Payments = Loan Term × 12
   - Monthly Repayments using standard amortisation formula

3. It shows:
   - Monthly Repayment Amount
   - Total Repayment Over the Loan Period
   - Total Interest Paid
   - Line chart of Remaining Loan Balance per Year

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – for building the UI
- [Pandas](https://pandas.pydata.org/) – for building and displaying the amortisation table
- [Matplotlib](https://matplotlib.org/) – (optional) for future custom visualisations
- Python’s built-in `math` library – for basic calculations

---

## ▶️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/AlbertoGhub/mortgage_calculator_Steamlit.git
```

### 2. Install dependencies
#### Option 1: Install manually

```bash
pip install streamlit pandas matplotlib
```
#### Option 2: Install from requirements.txt

```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

---

## 🌍 Deploying the App

📌 Recommended: Streamlit Community Cloud (free)

- Go to: https://streamlit.io/cloud
- Sign in with GitHub
- Click "New App"
- Connect your GitHub repository
- Select the branch and file (app.py) to deploy
- Click "Deploy"

## 📁 Project Structure
```bash
Project
│
├── app                
│    └── app.py             # Main Streamlit application
├── images                  # Screenshots
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

---

📌 Notes
- This app is meant for educational purposes, and for me, as a way of getting started with the Streamlit library
- All values are indicative and not financial advice.
---
👨‍💻 Author
Developed with ❤️ by Alberto AJ - AI/ML Engineer out of an endless curiosity and a passion for learning new things.
