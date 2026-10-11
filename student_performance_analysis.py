# ============================================================
# STUDENT PERFORMANCE ANALYSIS AND VISUALIZATION
# ============================================================

# Install Plotly (run this cell in Google Colab)
!pip install plotly -q

# Import required libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------
# 1. CREATE STUDENT DATA
# ------------------------------------------------------------
data = {
    "Roll_No": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Vansh", "Riya", "Karan", "Pooja"],
    "Branch": ["CE", "CE", "IT", "CE", "IT", "CE", "IT", "CE"],
    "Python": [85, 72, 65, 90, 55, 78, 45, 88],
    "DBMS": [80, 75, 60, 92, 58, 70, 50, 85],
    "Maths": [78, 68, 72, 88, 52, 74, 48, 91],
    "Attendance": [92, 85, 78, 95, 65, 88, 70, 94]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# ------------------------------------------------------------
# 2. CALCULATE AVERAGE, PERCENTAGE, GRADE, AND STATUS
# ------------------------------------------------------------
df["Average"] = df[["Python", "DBMS", "Maths"]].mean(axis=1)

# Each subject is marked out of 100, so average equals percentage
df["Percentage"] = df["Average"]

# Function to assign grades
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Assign grades and pass/fail status
df["Grade"] = df["Percentage"].apply(get_grade)
df["Status"] = np.where(df["Percentage"] >= 40, "Pass", "Fail")

# Display the complete dataset
print("STUDENT PERFORMANCE DATA")
print(df.to_string(index=False))

# ------------------------------------------------------------
# 3. INTERACTIVE BAR CHART: AVERAGE MARKS BY SUBJECT
# ------------------------------------------------------------
subject_average = df[["Python", "DBMS", "Maths"]].mean().reset_index()
subject_average.columns = ["Subject", "Average_Marks"]

fig1 = px.bar(
    subject_average,
    x="Subject",
    y="Average_Marks",
    title="Average Marks by Subject",
    text="Average_Marks"
)
fig1.show()

# ------------------------------------------------------------
# 4. STUDENT PERFORMANCE BAR CHART
# ------------------------------------------------------------
fig2 = px.bar(
    df,
    x="Name",
    y="Percentage",
    color="Branch",
    text="Percentage",
    title="Student Percentage"
)
fig2.show()

# ------------------------------------------------------------
# 5. INTERACTIVE LINE CHART: SUBJECT-WISE PERFORMANCE
# ------------------------------------------------------------
fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=df["Name"],
    y=df["Python"],
    mode="lines+markers",
    name="Python"
))

fig3.add_trace(go.Scatter(
    x=df["Name"],
    y=df["DBMS"],
    mode="lines+markers",
    name="DBMS"
))

fig3.add_trace(go.Scatter(
    x=df["Name"],
    y=df["Maths"],
    mode="lines+markers",
    name="Maths"
))

fig3.update_layout(
    title="Student Subject-wise Performance",
    xaxis_title="Student",
    yaxis_title="Marks"
)
fig3.show()

# ------------------------------------------------------------
# 6. SCATTER PLOT: ATTENDANCE VS PERFORMANCE
# ------------------------------------------------------------
fig4 = px.scatter(
    df,
    x="Attendance",
    y="Percentage",
    color="Branch",
    size="Average",
    hover_name="Name",
    title="Attendance vs Student Performance"
)
fig4.show()

# ------------------------------------------------------------
# 7. HISTOGRAM: DISTRIBUTION OF AVERAGE MARKS
# ------------------------------------------------------------
fig5 = px.histogram(
    df,
    x="Average",
    nbins=5,
    title="Distribution of Average Marks",
    labels={"Average": "Average Marks"}
)
fig5.show()

# ------------------------------------------------------------
# 8. BOX PLOT: SUBJECT-WISE MARKS DISTRIBUTION
# ------------------------------------------------------------
marks_data = df.melt(
    id_vars=["Name"],
    value_vars=["Python", "DBMS", "Maths"],
    var_name="Subject",
    value_name="Marks"
)

fig6 = px.box(
    marks_data,
    x="Subject",
    y="Marks",
    color="Subject",
    points="all",
    title="Subject-wise Marks Distribution"
)
fig6.show()

# ------------------------------------------------------------
# 9. BRANCH-WISE AVERAGE PERFORMANCE
# ------------------------------------------------------------
branch_average = (
    df.groupby("Branch")["Percentage"]
    .mean()
    .reset_index()
)

fig7 = px.bar(
    branch_average,
    x="Branch",
    y="Percentage",
    color="Branch",
    text="Percentage",
    title="Branch-wise Average Performance"
)
fig7.show()

# ------------------------------------------------------------
# 10. STUDENT SEARCH
# ------------------------------------------------------------
student_name = input("\nEnter student name to search: ").strip()

result = df[df["Name"].str.lower() == student_name.lower()]

if not result.empty:
    print("\nSTUDENT FOUND")
    print(result.to_string(index=False))
else:
    print("\nStudent not found.")

# ------------------------------------------------------------
# 11. BASIC CLASS ANALYSIS
# ------------------------------------------------------------
highest_student = df.loc[df["Percentage"].idxmax()]
lowest_student = df.loc[df["Percentage"].idxmin()]
class_average = df["Percentage"].mean()
pass_percentage = df["Status"].eq("Pass").mean() * 100

print("\n========== CLASS ANALYSIS ==========")
print("Highest Performing Student:", highest_student["Name"])
print("Highest Percentage:", round(highest_student["Percentage"], 2))
print("Lowest Performing Student:", lowest_student["Name"])
print("Lowest Percentage:", round(lowest_student["Percentage"], 2))
print("Class Average:", round(class_average, 2))
print("Pass Percentage:", round(pass_percentage, 2), "%")
