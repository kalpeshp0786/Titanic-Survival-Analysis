## Project Description

The Titanic Data Analysis project is a Python-based application that analyzes passenger data from the Titanic dataset. It uses Pandas for data analysis, Matplotlib and Seaborn for creating graphs, and Python classes and functions to organize the program.

This project helps users understand passenger survival, gender-wise survival rates, passenger classes, missing values, and age distribution through a simple menu-driven interface.

## Objectives

- Load and analyze the Titanic dataset.
- Display the first five records and column names.
- Show dataset information and statistical summaries.
- Identify missing values in each column.
- Calculate passenger survival counts and percentages.
- Compare survival rates by gender and passenger class.
- Visualize data using different graphs.

## Technologies Used

- **Python** – Main programming language
- **Pandas** – Data loading and analysis
- **Matplotlib** – Graph creation and visualization
- **Seaborn** – Statistical data visualization
- **CSV** – Dataset file format

## Project Files

```text
Titanic Survival Analysis/
│
├── Titanic Survival Analysis.py
├── titanic_new.csv
└── README.md
```

Keep the `titanic_new.csv` dataset in the same folder as the Python file.

## Requirements

Install Python 3 and the required libraries before running the project.

```bash
python -m pip install pandas matplotlib seaborn
```

## How to Run the Project

1. Download or prepare the Titanic dataset named `titanic_new.csv`.
2. Place the CSV file in the same folder as the Python program.
3. Open the project folder in Visual Studio Code or a terminal.
4. Run the Python file:

```bash
python "Titanic Survival Analysis.py"
```

5. After the dataset loads successfully, the main menu will appear.
6. Enter the number corresponding to the operation you want to perform.

## Features

### 1. Show Dataset Preview
Displays the first five records and all available column names.

### 2. Show Dataset Summary
Displays the dataset dimensions, column data types, and statistical information.

### 3. Check Missing Values
Identifies columns containing missing values.

### 4. Show Survival Report
Displays the number of passengers who survived and did not survive, along with the survival percentage.

### 5. Compare Survival by Gender
Shows passenger counts, survival counts, and average survival rates for each gender.

### 6. Compare Survival by Passenger Class
Analyzes survival information for different passenger ticket classes.

### 7. Display a Graph
Provides four visualization options:

- Survival count
- Passenger class count
- Age distribution
- Survival comparison by gender

### 8. Exit
Closes the application.

## Dataset Information

The project uses `titanic_new.csv`. Depending on the dataset version, it may contain columns such as:

- `Survived` – Survival status (0 = No, 1 = Yes)
- `Sex` – Passenger gender
- `Pclass` – Passenger ticket class
- `Age` – Passenger age

The program checks whether the required columns are available before performing specific analyses.

## Expected Output

When the program runs successfully, it displays a menu similar to this:

```text
========== TITANIC DATA ANALYSIS ==========

1. Show dataset preview
2. Show dataset summary
3. Check missing values
4. Show survival report
5. Compare survival by gender
6. Compare survival by passenger class
7. Display a graph
8. Exit

Enter your choice:
```

The output depends on the dataset and the option selected by the user. Graphs are displayed in a separate window.

## Error Handling

- Displays a message if the CSV file is missing.
- Prevents analysis before the dataset is loaded.
- Checks whether required columns exist.
- Handles errors encountered while loading the dataset.
- Displays a message when an invalid menu option is entered.

## Conclusion

The Titanic Data Analysis project demonstrates how Python can be used to explore and understand real-world data. It provides practical experience with Pandas, data cleaning checks, statistical summaries, survival analysis, and graphical visualization. The project also demonstrates the use of classes, methods, conditional statements, loops, and exception handling in Python.

