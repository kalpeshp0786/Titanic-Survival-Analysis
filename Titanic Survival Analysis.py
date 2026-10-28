import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TitanicAnalysis:
    def __init__(self, file_name="titanic_new.csv"):
        self.file_name = file_name
        self.data = None

    def load_data(self):
     try:
         folder_path = os.path.dirname(os.path.abspath(__file__))
         file_path = os.path.join(folder_path, "titanic_new.csv")

         self.data = pd.read_csv(file_path)

         print("\nDataset loaded successfully.")
         print("Total rows:", self.data.shape[0])
         print("Total columns:", self.data.shape[1])

     except FileNotFoundError:
        print("CSV file not found!")
        print("Please keep titanic_new.csv in the same folder as your Python file.")

     except Exception as error:
        print("Error:", error)

    def show_preview(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        print("\nFirst five records:")
        print(self.data.head())
        print("\nColumn names:")
        print(list(self.data.columns))

    def show_summary(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        print("\nDataset information:")
        print("Rows and columns:", self.data.shape)
        print("\nData types:")
        print(self.data.dtypes)
        print("\nStatistical summary:")
        print(self.data.describe(include="all").transpose())

    def check_missing_values(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        missing = self.data.isnull().sum()
        print("\nMissing values in each column:")
        print(missing[missing > 0] if missing.any() else "No missing values found.")

    def survival_report(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        if "Survived" not in self.data.columns:
            print("This dataset does not contain a 'Survived' column.")
            return

        counts = self.data["Survived"].value_counts().sort_index()
        print("\nSurvival count (0 = did not survive, 1 = survived):")
        print(counts)

        total = self.data["Survived"].notna().sum()
        survived = (self.data["Survived"] == 1).sum()
        if total:
            print(f"Survival percentage: {survived / total * 100:.2f}%")

    def compare_by_gender(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        if not {"Sex", "Survived"}.issubset(self.data.columns):
            print("Required columns 'Sex' and 'Survived' are not available.")
            return

        print("\nSurvival results by gender:")
        print(self.data.groupby("Sex")["Survived"].agg(["count", "sum", "mean"]))
        print("Mean is the survival rate (from 0 to 1).")

    def compare_by_class(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        if not {"Pclass", "Survived"}.issubset(self.data.columns):
            print("Required columns 'Pclass' and 'Survived' are not available.")
            return

        print("\nSurvival results by passenger class:")
        print(self.data.groupby("Pclass")["Survived"].agg(["count", "sum", "mean"]))

    def make_graph(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        print("\n1. Survival count")
        print("2. Passenger class count")
        print("3. Age distribution")
        print("4. Survival by gender")
        choice = input("Choose a graph: ").strip()

        if choice == "1":
            if "Survived" not in self.data.columns:
                print("Survived column is missing.")
                return
            sns.countplot(data=self.data, x="Survived")
            plt.title("Titanic Passenger Survival Count")
            plt.xlabel("Survived (0 = No, 1 = Yes)")
            plt.ylabel("Number of Passengers")

        elif choice == "2":
            if "Pclass" not in self.data.columns:
                print("Pclass column is missing.")
                return
            sns.countplot(data=self.data, x="Pclass")
            plt.title("Passengers by Ticket Class")
            plt.xlabel("Passenger Class")
            plt.ylabel("Number of Passengers")

        elif choice == "3":
            if "Age" not in self.data.columns:
                print("Age column is missing.")
                return
            sns.histplot(data=self.data, x="Age", bins=20, kde=True)
            plt.title("Age Distribution of Passengers")
            plt.xlabel("Age")
            plt.ylabel("Number of Passengers")

        elif choice == "4":
            if not {"Sex", "Survived"}.issubset(self.data.columns):
                print("Sex or Survived column is missing.")
                return
            sns.countplot(data=self.data, x="Sex", hue="Survived")
            plt.title("Survival Comparison by Gender")
            plt.xlabel("Gender")
            plt.ylabel("Number of Passengers")
            plt.legend(title="Survived", labels=["No", "Yes"])

        else:
            print("Invalid graph choice.")
            return

        plt.tight_layout()
        plt.show()

    def run(self):
        self.load_data()
        if self.data is None:
            return

        while True:
            print("\n========== TITANIC DATA ANALYSIS ==========")
            print("1. Show dataset preview")
            print("2. Show dataset summary")
            print("3. Check missing values")
            print("4. Show survival report")
            print("5. Compare survival by gender")
            print("6. Compare survival by passenger class")
            print("7. Display a graph")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.show_preview()
            elif choice == "2":
                self.show_summary()
            elif choice == "3":
                self.check_missing_values()
            elif choice == "4":
                self.survival_report()
            elif choice == "5":
                self.compare_by_gender()
            elif choice == "6":
                self.compare_by_class()
            elif choice == "7":
                self.make_graph()
            elif choice == "8":
                print("Thank you for using Titanic Data Analysis.")
                break
            else:
                print("Please enter a number from 1 to 8.")


if __name__ == "__main__":
    project = TitanicAnalysis("titanic_new.csv")
    project.run()
