import math

def display_flights(flight_list):
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    for i, f in enumerate(flight_list, 1):
        # 10 khách/thùng -> math.ceil để làm tròn lên
        water_barrels = math.ceil(f['passengers'] / 10)
        print(f"{i}. Mã: {f['flight_id']} | Khởi hành: {f['depart_time']} | "
              f"Số khách: {f['passengers']:<3} | Dự phòng: {water_barrels} thùng nước.")