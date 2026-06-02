delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
delivery_orders.append("GE004")
delivery_orders.insert(0, "GE000")
delivery_orders[2] = "GE002-UPDATED"
delivery_orders.remove("GE003-CANCEL")
transferred_order = delivery_orders.pop()
print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)