import pandas as pd
import matplotlib.pyplot as plt


# Load the hospital dataset from the 'data/' folder
df = pd.read_csv("data/diabetic_data.csv")

# 1. Check for null values in each column

print("Null values before cleaning:")
print(df.isnull().sum())

# 2. Drop rows with too many missing values
df.dropna(thresh=len(df.columns) - 2, inplace=True)

# 3. Fill remaining missing values (customize based on column types)
df.fillna({
    "race": "Unknown",
    "medical_specialty": "General",
    "diag_1": "Other",
    "diag_2": "Other",
    "diag_3": "Other"
}, inplace = True)

# 4. Rename some confusing columns (example)
df.rename(columns={
    "encounter_id": "visit_id",
    "patient_nbr": "patient_id",
    "readmitted": "was_readmitted"
}, inplace = True)

# 5. Remove exact duplicate rows, if any
df.drop_duplicates(inplace = True)

# 6. Quick check after cleaning
print("\nShape after cleaning:", df.shape)
print("First dew rows:\n", df.head())

# 7. Save cleaned data for next steps (e.g. SQL or Tableau)
df.to_csv("output/cleaned_data.csv", index = False)

#Check unique values in readmission column
print(df["was_readmitted"].value_counts())

# Percentage of readmitted vs not
print(df["was_readmitted"].value_counts(normalize=True) * 100)

# Count readmissions by age
readmit_by_age = df[df["was_readmitted"] != "NO"].groupby("age")["was_readmitted"].count()

# Visualize it
readmit_by_age.plot(kind="bar", title="Readmissions by Age Group", figsize=(10,4))


# Show the plot explicitly (optional but helpful)
plt.ylabel("Number of Readmissions")
plt.xlabel("Age Group")
plt.tight_layout()
plt.show()