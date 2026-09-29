# Vit-Project

# VIT Counselling Simulator

A command-line Python application that simulates the VITEEE counselling seat allotment process. It takes a candidate's rank along with campus and branch preferences, validates every input, and allots the best available seat based on simulated closing-rank cutoffs across VIT campuses.

**Repository:** https://github.com/Anshu-Raj45/Vit-Project

---

## Features

- **Strict input validation:** re-prompts automatically for invalid, negative, out-of-range or non-integer values.
- **Rank range enforcement:** accepts ranks only from 1 to 150,000 (total candidates).
- **Duplicate prevention:** the same campus or branch cannot be entered twice.
- **Optimal allotment logic:** evaluates all entered preferences and allots the seat with the lowest closing-rank cutoff (strictest/best college) among all eligible options.
- **Terminal only:** runs in any standard terminal with no GUI and no external libraries.

---

## Project Structure

```
Vit-Project/
├── main.py
└── README.md      
```

---

## Prerequisites

- **Python 3.6 or higher**
- Any terminal: Command Prompt, PowerShell, macOS Terminal or a Linux shell

Check your Python installation:

```bash
python --version
# or
python3 --version
```

---

## Step-by-Step Setup

### 1. Clone the repository

```bash
https://github.com/Anshu-Raj45/Vit-Project
cd Vit-Project
```

### 2. Dependency installation

This project uses **only the Python standard library**, so there is nothing to install. No `pip install` step and no `requirements.txt` is needed.

### 3. Configuration

No configuration files, environment variables or API keys are required. The campus list, branch list and simulated closing-rank cutoffs are defined inside `main.py`.

---

## Running the Project

From inside the `Vit-Project` folder, run:

```bash
python main.py
```

## How It Works

1. **Enter your rank:** a VITEEE rank between 1 and 150,000.
2. **Set the number of preferences:** how many campuses and how many branches you want to evaluate.
3. **Select options:** enter the option numbers from the tables below.
4. **Result:** the program checks every selected campus/branch combination against the simulated closing-rank cutoffs and automatically allots the best eligible seat.

---

## Input Reference

**Campuses**

| Option | Campus       |
|--------|--------------|
| 1      | VIT Vellore  |
| 2      | VIT Chennai  |
| 3      | VIT AP       |
| 4      | VIT Bhopal   |

**Branches**

| Option | Branch             |
|--------|--------------------|
| 1      | CSE                |
| 2      | CSE AI & ML        |
| 3      | CSE Data Science   |
| 4      | ECE                |
| 5      | EEE                |
| 6      | Mechanical         |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `python` is not recognised | Use `python3`, or reinstall Python and tick "Add Python to PATH". |
| `can't open file 'main.py'` | Make sure you are inside the `Vit-Project` folder (`cd Vit-Project`). |
| Old Python version error | Check `python --version`; Python 3.6 or higher is required. |
| Program keeps re-asking for input | Enter a whole number within the range shown in the prompt, without duplicates. |

---

## Conclusion

The VIT Counselling Simulator gives a simple, dependency-free way to understand how VITEEE seat allotment works. By validating every input, preventing duplicate preferences and comparing a candidate's rank against closing-rank cutoffs across campuses and branches, it shows which seat a given rank is likely to secure. It is useful for aspirants exploring their options and for learners studying input validation and preference-based selection logic in Python.

Possible future improvements include using real historical cutoff data, category-wise and slot-wise allotment, and a web-based interface.
