inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]
def show_inventory(inventory_list):
    print(f"--- DANH SÁCH HÀNG TỒN KHO ---")
    if len(inventory_list) == 0:
        print("Kho hàng đang rỗng")
        return
    print(f"{'ID':<5} |" f"{'Tên':<12}  |" f"{'Số lượng':<8}|")
    for inventory in inventory_list:
         print(
            f"{inventory['id']:<5} | "
            f"{inventory['name']:<12} | "
            f"{inventory['quantity']:<6} | "
        )
def add_item(inventory_list):
    inventory_id = input("Nhập mã hàng hóa(ID): ")
    inventory_name = input("Nhập tên hàng hóa: ")
    inventory_quantity = input("Nhập số lượng của hàng hóa")
    
    New_inventory = {
    "id": inventory_id,
    "name": inventory_name,
    "quantity": inventory_id
}
    inventory.append(New_inventory)
    print("Tạo đơn hàng thành công")
    
    if inventory_id == 0:
        print("Không được để trống vui lòng nhập lại!")
        return
    

menu = True
while menu:
    print(f"="*65)
    print(f"QUẢN LÝ KHO HÀNG - GROCERY STORE")
    print(f"1. Xem danh sách hàng tồn kho")
    print(f"2. Nhập thêm hàng hóa mới")
    print(f"4. Thoát chương trình")
    print(f"="*65)
    user_choice = input("Mời bạn lựa chọn tính năng: ")
    if user_choice == '4':
        print("Bạn đã chọn tính năng số 4")
        print("Đang thoát chương trình ...")
        break
    elif user_choice == '1':
        print("Bạn đã chọn tính năng số 1")
        show_inventory(inventory)
    elif user_choice == '2':
        print("Bạn đã chọn tính năng số 2")
        add_item(inventory)
    else:
        print("Lựa chọn sai vui lòng nhập lại!")
        
        
        
        