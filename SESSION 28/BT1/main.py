from abc import ABC, abstractmethod

class BaseEmployee(ABC):
    company_name = "Rikkei Education"
    base_salary_rate = 3000000

    def __init__(self, employee_id, fullname):
        self.employee_id = self.validate_employee_code(employee_id)
        self.fullname = fullname.strip().upper()
        self.__working_hours = 0

    @property
    def working_hours(self):
        return self.__working_hours

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def update_kpi(self, progress):
        pass

    @staticmethod
    def validate_employee_code(emp_code: str):
        if not emp_code.startswith("RKE") or len(emp_code) != 10:
            raise ValueError("Mã nhân sự không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng RKE.")
        return emp_code

    @classmethod
    def update_base_salary_rate(cls, new_rate):
        cls.base_salary_rate = new_rate

    def _update_working_hours(self, hours=2):
        if hours <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        self.__working_hours += hours

    def __add__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.__working_hours + other.__working_hours

    def __lt__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.__working_hours < other.__working_hours


class Lecturer(BaseEmployee):
    def __init__(self, employee_id, fullname):
        super().__init__(employee_id, fullname)
        self.teaching_slots = 0

    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000)

    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        print(f"KPI giảng viên đạt {progress}%")

    def conduct_class(self):
        self.teaching_slots += 1
        super()._update_working_hours()


class AdmissionStaff(BaseEmployee):
    def __init__(self, employee_id, fullname, kpi_target=100000000):
        super().__init__(employee_id, fullname)
        self.kpi_target = kpi_target
        self.revenue_generated = 0

    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.revenue_generated * 0.05)

    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        self.revenue_generated += progress


class HybridManager(Lecturer, AdmissionStaff):
    def __init__(self, employee_id, fullname, kpi_target=100000000):
        super().__init__(employee_id, fullname)
        self.kpi_target = kpi_target
        self.revenue_generated = 0
        self.teaching_slots = 0

    def calculate_salary(self):
        salary_from_hours = self.working_hours * self.base_salary_rate
        salary_from_slots = self.teaching_slots * 500000
        salary_from_revenue = self.revenue_generated * 0.05
        return salary_from_hours + salary_from_slots + salary_from_revenue

    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        self.revenue_generated += progress


# Duck Typing cho cổng thanh toán
class VietcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print(f"[VCB] Đã giải ngân {amount:,} VND cho {employee.fullname} ({employee.employee_id})")


class TechcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print(f"[TCB] Đã giải ngân {amount:,} VND cho {employee.fullname} ({employee.employee_id})")


def execute_payroll(payment_service, employee, amount):
    try:
        payment_service.transfer_salary(employee, amount)
    except AttributeError:
        raise AttributeError("Cổng dịch vụ ngân hàng doanh nghiệp không hợp lệ hoặc chưa được liên kết.")


# ================= MENU CLI =================
def main():
    employees = []
    current_employee = None

    while True:
        print("\n===== RIKKEI EDUCATION HR SIMULATOR PRO =====")
        print("1. Tuyển dụng nhân sự mới")
        print("2. Xem thông tin & Kiểm tra MRO")
        print("3. Ghi nhận công nhật & Cập nhật KPI")
        print("4. Tổng hợp quỹ lương")
        print("5. Kiểm tra gộp giờ làm việc & So sánh hiệu suất")
        print("6. Giải ngân lương qua Cổng thanh toán")
        print("7. Thoát chương trình")
        choice = input("Chọn chức năng (1-7): ")

        try:
            if choice == "1":
                print("--- CHỌN LOẠI NHÂN SỰ ---")
                print("1. Lecturer")
                print("2. Admission Staff")
                print("3. Hybrid Manager")
                emp_type = input("Chọn loại nhân sự (1-3): ")
                emp_id = input("Nhập mã nhân sự 10 ký tự: ")
                fullname = input("Nhập họ và tên: ")

                if emp_type == "1":
                    emp = Lecturer(emp_id, fullname)
                elif emp_type == "2":
                    emp = AdmissionStaff(emp_id, fullname)
                elif emp_type == "3":
                    emp = HybridManager(emp_id, fullname)
                else:
                    print("Loại nhân sự không hợp lệ!")
                    continue

                employees.append(emp)
                current_employee = emp
                print(f"Tuyển dụng thành công: {emp.fullname}")

            elif choice == "2":
                if not current_employee:
                    print("Chưa có nhân sự được chọn!")
                else:
                    print("--- THÔNG TIN NHÂN SỰ ---")
                    print(f"Loại: {current_employee.__class__.__name__}")
                    print(f"Tổ chức: {current_employee.company_name}")
                    print(f"Mã: {current_employee.employee_id}")
                    print(f"Tên: {current_employee.fullname}")
                    print(f"Số giờ làm việc: {current_employee.working_hours}")
                    if isinstance(current_employee, Lecturer):
                        print(f"Số ca dạy: {current_employee.teaching_slots}")
                    if isinstance(current_employee, AdmissionStaff):
                        print(f"Doanh số: {current_employee.revenue_generated}")
                    print("MRO:", current_employee.__class__.mro())

            elif choice == "3":
                if not current_employee:
                    print("Chưa có nhân sự được chọn!")
                else:
                    print("1. Ghi nhận ca dạy (Lecturer/Hybrid)")
                    print("2. Cập nhật doanh số (Admission/Hybrid)")
                    task = input("Chọn tác vụ (1-2): ")
                    if task == "1" and isinstance(current_employee, Lecturer):
                        current_employee.conduct_class()
                        print("Ghi nhận ca dạy thành công!")
                    elif task == "2" and isinstance(current_employee, AdmissionStaff):
                        revenue = int(input("Nhập doanh số mới: "))
                        current_employee.update_kpi(revenue)
                        print("Cập nhật doanh số thành công!")
                    else:
                        print("Tác vụ không hợp lệ!")

            elif choice == "4":
                if not current_employee:
                    print("Chưa có nhân sự được chọn!")
                else:
                    salary = current_employee.calculate_salary()
                    print(f"Tổng lương thực nhận: {salary:,} VND")

            elif choice == "5":
                if not current_employee or len(employees) < 2:
                    print("Cần ít nhất 2 nhân sự để so sánh!")
                else:
                    for i, emp in enumerate(employees):
                        print(f"{i+1}. {emp.fullname} ({emp.employee_id}) - {emp.working_hours} giờ")
                    idx = int(input("Chọn nhân sự đối ứng: ")) - 1
                    other = employees[idx]
                    print("So sánh giờ công:", current_employee < other)
                    print("Tổng giờ công:", current_employee + other)

            elif choice == "6":
                if not current_employee:
                    print("Chưa có nhân sự được chọn!")
                else:
                    print("1. Vietcombank")
                    print("2. Techcombank")
                    bank_choice = input("Chọn ngân hàng (1-2): ")
                    amount = current_employee.calculate_salary()
                    if bank_choice == "1":
                        bank = VietcombankCorporateService()
                    else:
                        bank = TechcombankCorporateService()
                    execute_payroll(bank, current_employee, amount)

            elif choice == "7":
                print("Cảm ơn đã sử dụng hệ thống!")
                break

            else:
                print("Lựa chọn không hợp lệ!")

        except Exception as e:
            print("Lỗi:", e)


if __name__ == "__main__":
    main()
