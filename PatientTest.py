test_result_value = (("RBC", (4.32, 5.72)), ("WBC", (3.5, 10.5)), ("HEMOGLOBIN", (13, 17)), ("PLATELET", (1.5, 4.0)), ("MCV", (90.4, 128)))
dict = {}

for i, values in test_result_value:
    dict[i] = values

print(dict)

# User input
patient_testNm = (input("Enter test name: ").strip()).upper()
patient_testResult = float(input("Enter test result: "))

if patient_testNm in dict: #use membershipp operator
    normal_range = dict[patient_testNm]
    if normal_range[0] <= patient_testResult <= normal_range[1]:
        print("Normal")
    else:
        print("Abnormal")
else:
    print("Test name not found.")