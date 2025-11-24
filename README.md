# Unit-Test-Result-Analyzer
This project is a complete result analysis tool designed to process student grade data from an Excel sheet and generate detailed subject-wise performance reports. It helps institutions, teachers, and administrators to quickly evaluate academic results with clear insights, including toppers, arrears, pass percentage, and grade distribution charts.


# Student Result Analysis using Python (Pandas + Matplotlib)

This project analyzes student examination results from an Excel file and generates:

- *Subject-wise toppers*
- *Arrear and absentee details*
- *Pass percentage*
- *Grade-wise bar charts*

The script reads an Excel sheet containing student details and grade columns, processes each subject, and outputs visual and textual analysis.

---

## 📂 Features

### ✔ *1. Read Excel File*
- Reads file name and sheet name from user input.
- Converts registration number column to integer.

### ✔ *2. Subject-wise Toppers*
- Identifies the highest grade (priority order: O → A+ → A → B+ → B).
- Lists all students earning the top grade.

### ✔ *3. Arrear Analysis*
- Lists:
  - Arrear students (U)
  - Arrear absentees (UA)
  - Withdrawn (W)
  - Withheld (WH)
- Calculates *pass percentage* excluding withdrawn students.

### ✔ *4. Grade Distribution Graph*
- Creates bar charts showing the frequency of each grade:
  - O, A+, A, B+, B, U, UA, WH, W

---

## 📄 Input Format (Excel Sheet)

Expected columns (example):

| RegNumber | Name | MA101 | PH101 | CS101 | ... |
|-----------|------|--------|--------|--------|-----|

Where each subject column contains grades like:
O, A+, A, B+, B, U, UA, WH, W.

---


##CODE:


<img width="629" height="751" alt="Screenshot 2025-11-24 232004" src="https://github.com/user-attachments/assets/fe749d38-42a3-4a47-870f-8a98925a1c52" />
<img width="621" height="732" alt="Screenshot 2025-11-24 232030" src="https://github.com/user-attachments/assets/2fe22665-f930-4145-b9d3-06b2594843dc" />
<img width="660" height="799" alt="Screenshot 2025-11-24 232048" src="https://github.com/user-attachments/assets/f1b5aedb-4e1a-4777-a03f-30e023ce30a9" />




##OUTPUT:

<img width="855" height="900" alt="Screenshot 2025-11-24 122221" src="https://github.com/user-attachments/assets/edd2d588-698d-42a4-b9a5-9130be6b030c" />
<img width="659" height="818" alt="Screenshot 2025-11-24 122254" src="https://github.com/user-attachments/assets/c9ab357b-e870-432d-8977-04c08131d99a" />
<img width="600" height="362" alt="Screenshot 2025-11-24 122329" src="https://github.com/user-attachments/assets/0cf994bf-9ec9-431e-91a8-7b195b5ff7bc" />


--bargraph output--


<img width="795" height="633" alt="Screenshot 2025-11-24 115914" src="https://github.com/user-attachments/assets/8c7483bb-bbf1-48bc-ac14-beb26e387c75" />
<img width="777" height="636" alt="Screenshot 2025-11-24 120003" src="https://github.com/user-attachments/assets/00fb2a4e-1bf3-4979-a86f-a587cd191cca" />
<img width="802" height="645" alt="Screenshot 2025-11-24 120024" src="https://github.com/user-attachments/assets/f8fdbcd4-7020-42ff-b3fb-8ab47a33616f" />
<img width="762" height="634" alt="Screenshot 2025-11-24 120102" src="https://github.com/user-attachments/assets/19030757-1747-41cb-adae-f3b660db2b8d" />
<img width="784" height="643" alt="Screenshot 2025-11-24 120122" src="https://github.com/user-attachments/assets/bac09e21-94c1-470e-ac94-3a73c263b685" />




✅ Algorithm

Function: read_file()

1. Prompt the user to enter the Excel file name.


2. Prompt the user to enter the sheet name.


3. Read the Excel file into a pandas DataFrame.


4. Convert the RegNumber column into integer type.


5. Return the DataFrame.




---

Function: subjectwise_topper(df, j)

1. Print the subject code corresponding to column j.


2. Initialize variable highest_grade as an empty string.


3. Loop through each row:

Check grades in order of priority: O → A+ → A → B+ → B.

Update highest_grade with the highest one found.



4. Print the highest grade.


5. Loop again to list students who obtained highest_grade.




---

Function: subjectwise_arrear(df, j)

1. Initialize counters:

count → number of arrears and absentees

w → number of withdrawn and withheld students



2. Print arrear students (U).


3. Print arrear absentees (UA).


4. Print withdrawn students (W).


5. Print withheld students (WH).


6. Compute pass percentage:


Pass Percentage=[(Total Student-Studentwith Grade U,UA,W,WH)/(Total Student - Student with Grades w or wh)] * 100


---



Function: graph(df, j)

1. Initialize an array to count occurrences of grades: ["O","A+","A","B+","B","U","UA","WH","W"]


2. Loop through each row and increment corresponding grade count.


3. Plot a bar chart:

x-axis → grades

y-axis → counts

title → subject code



4. Display the graph.




---

Main Program

1. Call read_file() to import DataFrame.


2. Ask user for:

Starting column number of grades.

Ending column number of grades.



3. Loop through each subject column:

Print toppers.

Print arrear details.

Display graph.



##FLOWCHART:

<img width="615" height="740" alt="Screenshot 2025-11-25 000214" src="https://github.com/user-attachments/assets/28b35b06-e5a6-4d98-978f-19bf92701ea7" />
<img width="605" height="839" alt="Screenshot 2025-11-25 000243" src="https://github.com/user-attachments/assets/59df31d8-8c30-4c2b-a1f5-7bdbd707c041" />

* Created By: Hafizur Rahman
* Reg. No.: 25BAI11372
* Subject: Itroduction To Problem Solving and Programing
* Faculty: Dr. Manimaran
