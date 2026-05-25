print("---- BLOOD DONOR SCREENING SYSTEM ----")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    # Thông báo lý do không đủ điều kiện
    if donor_age < 18 and donor_weight < 50:
        print("Result: NOT ELIGIBLE. Reason: Under 18 and weight below 50kg.")
    elif donor_age < 18:
        print("Result: NOT ELIGIBLE. Reason: Age below 18.")
    elif donor_weight < 50:
        print("Result: NOT ELIGIBLE. Reason: Weight below 50kg.")
