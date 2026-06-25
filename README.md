# 🧾 Vending Machine Management System

A desktop-based billing and transaction management application built using Python and Tkinter. The system provides an easy-to-use graphical interface for generating customer bills, calculating totals, managing transactions, and storing billing records.

---

## 📌 Overview

The Vending Machine Management System automates the billing process for vending machine operations. It allows users to enter customer and product details, calculate costs instantly, generate bills, and save transaction records for future reference.

This project demonstrates GUI development, event-driven programming, file handling, and automation using Python.

---

## ✨ Features

### 🔐 Secure Login System

The application includes a login screen to prevent unauthorized access.

Default Credentials:

- Username: `user`
- Password: `123`

---

### 🧾 Automated Billing

Generate bills automatically with:

- Unique bill numbers
- Customer details
- Product information
- Quantity tracking
- Cost calculations
- Transaction timestamps

---

### 💰 Automatic Cost Calculation

The application instantly calculates:

```text
Total Cost = Quantity × Cost per Item
```

This reduces manual work and billing errors.

---

### 📅 Date & Time Tracking

Displays:

- Current Date
- Current Time
- Current Day

Every transaction is recorded with timestamp information.

---

### 💾 Data Storage

All bills are automatically stored inside:

```text
data.txt
```

This creates a simple transaction history system.

---

### 🔄 Reset Functionality

Clear all entered information instantly using the Reset button.

---

## 🖥️ Application Workflow

### Step 1

Launch the application.

### Step 2

Login using valid credentials.

### Step 3

Enter:

- Customer Name
- Item Name
- Quantity
- Cost Per Item

### Step 4

Click **Total** to calculate the final amount.

### Step 5

Click **Bill** to generate and save the transaction.

### Step 6

The generated bill is stored in `data.txt`.

---

## 🏗️ Project Structure

```text
Vending-Machine-Management-System/
│
├── main.py
├── data.txt
├── README.md
│
└── screenshots/
    ├── login.png
    └── dashboard.png
```

---

## ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Tkinter | GUI Development |
| Random | Bill Number Generation |
| Datetime | Date & Time Management |
| File Handling | Data Storage |

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/vending-machine-management-system.git
```

### Move into Project Directory

```bash
cd vending-machine-management-system
```

### Run the Application

```bash
python main.py
```

---

## 🧠 Concepts Demonstrated

### Python Fundamentals

- Variables
- Functions
- Conditional Statements
- Event Handling

### GUI Development

- Labels
- Buttons
- Entry Widgets
- Window Management

### File Handling

- Reading Files
- Writing Files
- Appending Data

### Automation

- Bill Generation
- Cost Calculation
- Date and Time Tracking

---

## 🔮 Future Improvements

Potential upgrades include:

- SQLite Database Integration
- Inventory Management
- PDF Bill Generation
- Sales Analytics Dashboard
- User Management System
- Password Encryption
- Search Functionality
- Excel Export Support
- Print Bill Feature

---

## 🎯 Learning Outcomes

This project helped me gain experience in:

- Python Programming
- Desktop Application Development
- GUI Design
- Data Management
- Software Automation
- User Experience Design

---

## 👨‍💻 Author

**Bhagyam Pathak**

Aspiring Full-Stack Developer | Python Developer | Machine Learning Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

⭐ Star the repository to support the project!
