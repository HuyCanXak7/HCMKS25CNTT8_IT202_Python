import datetime

print("---- PATIENT QUICK ASSESSMENT SYSTEM ----")

patient_name = input("Enter patient name: ").strip()
if not patient_name:
    print("ERROR: Name cannot be empty!")
    exit()

try:
    birth_year = int(input("Enter birth year (e.g. 1985): "))
    days_sick = int(input("Enter number of sick days: "))
    temperature = float(input("Enter body temperature (°C): "))
    exam_fee = float(input("Enter exam fee (VND): "))
except ValueError:
    print("ERROR: Invalid input type!")
    exit()

current_year = datetime.datetime.now().year
if birth_year < 1900 or birth_year > current_year:
    print("ERROR: Birth year out of range!")
    exit()
if days_sick < 0:
    print("ERROR: Sick days must be >= 0!")
    exit()
if temperature < 30 or temperature > 45:
    print("ERROR: Temperature out of range!")
    exit()
if exam_fee <= 0:
    print("ERROR: Exam fee must be > 0!")
    exit()

age = current_year - birth_year
extra_fee = exam_fee * 0.1
total_fee = exam_fee + extra_fee

if temperature > 38 and days_sick > 3:
    health_status = "Nguy hiểm"
elif temperature > 38:
    health_status = "Sốt cao"
elif temperature > 37.5:
    health_status = "Sốt nhẹ"
else:
    health_status = "Bình thường"

# Priority (Nested If)
if health_status == "Nguy hiểm":
    if age > 60:
        priority = "Cấp cứu"
    else:
        priority = "Ưu tiên cao"
else:
    priority = "Bình thường"

fee_level = "Cao" if total_fee > 500000 else "Thấp"

print("\n===== PATIENT REPORT =====")
print(f"Name          : {patient_name}")
print(f"Age           : {age}")
print(f"Health Status : {health_status}")
print(f"Priority      : {priority}")
print(f"Exam Fee      : {exam_fee} VND")
print(f"Extra Fee     : {extra_fee} VND")
print(f"Total Fee     : {total_fee} VND")
print(f"Fee Level     : {fee_level}")
print("==========================")
