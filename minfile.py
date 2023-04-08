import pandas as pd

# Define a sample DataFrame with student data and marks
data2 = {
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "Dave", "Eve"],
    "email": ["alice@example.com", "bob@example.com", "charlie@example.com", "dave@example.com", "eve@example.com"],
    "computer": [60, 70, 80, 90, 65],
    "mechanics": [80, 75, 70, 60, 85],
    "maths": [90, 80, 70, 60, 50],
    "English": [70, 75, 80, 85, 90],
    "electrical": [65, 60, 55, 70, 75],
    "physics": [85, 90, 95, 80, 75],
    "chemistry": [75, 80, 85, 90, 95]
}
data=pd.read_csv("Book1.csv")
df = pd.DataFrame(data)

# Find the subject with the minimum marks for each student
subjects = ["computer", "mechanics", "maths", "English", "electrical", "physics", "chemistry"]


print(df[subjects].idxmin(axis=1))
