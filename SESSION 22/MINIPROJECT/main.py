import logging

# Cấu hình logging hệ thống
logging.basicConfig(
    level=logging.DEBUG,  # Hiển thị đầy đủ DEBUG → ERROR
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def get_discount_rate(tier: str, quantity: int) -> float:
    """Trả về tỷ lệ chiết khấu dựa trên hạng thành viên và số lượng"""
    logger.debug(f"Đang tính toán chiết khấu cho hạng {tier} với số lượng {quantity}")
    
    if quantity <= 0:
        raise ValueError("Quantity must be positive")  # Clean Code: chặn dữ liệu sai
    
    # Xác định tỷ lệ chiết khấu cơ bản
    if tier == "silver":
        rate = 0.05
    elif tier == "gold":
        rate = 0.10
    elif tier == "diamond":
        rate = 0.15
    else:
        rate = 0.0
        
    # Thưởng thêm nếu mua số lượng lớn (>= 50 sản phẩm)
    if quantity >= 50:
        rate += 0.05  # Fix lỗi logic: cộng thêm
    
    return rate

def calculate_agency_total(price: float, quantity: int, tier: str) -> float:
    """Tính tổng tiền sau chiết khấu cho đại lý"""
    if price < 0:
        raise ValueError("Đơn giá không được âm")
        
    rate = get_discount_rate(tier, quantity)
    final_price = price * (1 - rate) * quantity
    
    logger.info(f"Kết quả: Tổng tiền = {final_price}")
    return final_price

# Test cases
if __name__ == "__main__":
    calculate_agency_total(100, 50, "gold")   # Case biên: gold + số lượng lớn
    calculate_agency_total(100, 10, "silver") # Case thường
    # calculate_agency_total(100, -5, "silver") # Case lỗi dữ liệu đầu vào
