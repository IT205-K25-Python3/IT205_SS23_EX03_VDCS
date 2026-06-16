from core import logistics, manager
from utils import time_helper, file_helper

flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
]

def main():
    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần\n2. Tiếp nhận chuyến bay mới\n"
              "3. Tính thời gian hạ cánh dự kiến (ETA)\n4. Khởi tạo thư mục lưu trữ log hệ thống\n5. Thoát chương trình")
        
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
            if choice == 1: logistics.display_flights(flights)
            elif choice == 2: manager.add_flight(flights)
            elif choice == 3: time_helper.calculate_eta(flights)
            elif choice == 4: file_helper.create_log_folder()
            elif choice == 5:
                print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
                break
            else: print("Vui lòng chọn từ 1-5.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên!")

if __name__ == "__main__":
    main()