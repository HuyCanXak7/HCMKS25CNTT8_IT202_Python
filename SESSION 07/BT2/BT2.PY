transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "
transaction = transaction.strip()
parts = transaction.split("|")

student_name = parts[0].strip().title()      
course_code  = parts[1].strip()              
amount = int(parts[2].strip())         
status = parts[3].strip().upper()      
amount_str = "{:,} VND".format(amount)        
print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", amount_str)
print("Trạng thái:", status)
