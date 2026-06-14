yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()

    new_prescription[0] = new_prescription[0].replace(
        "Panadol",
        "Paracetamol"
    )

    new_prescription.append("Oresol")

    return new_prescription

today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)