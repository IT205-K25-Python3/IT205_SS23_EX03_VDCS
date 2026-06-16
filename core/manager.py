def check_duplicate_id(flight_id, flight_list):
    new_id = flight_id.strip().upper()
    for f in flight_list:
        if f['flight_id'] == new_id:
            return True
    return False

def add_flight(flight_list):
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    try:
        fid = input("Nhập mã chuyến bay: ").strip().upper()
        if check_duplicate_id(fid, flight_list):
            print(">> Lỗi: Mã chuyến bay đã tồn tại!")
            return

        passengers = int(input("Nhập số lượng hành khách: "))
        time_str = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ")
        # Kiểm tra format ngày tháng
        from datetime import datetime
        datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        
        duration = int(input("Nhập số phút bay: "))
        
        flight_list.append({
            "flight_id": fid, "passengers": passengers,
            "depart_time": time_str, "duration_min": duration
        })
        print(f">> Thêm chuyến bay {fid} thành công!")
    except ValueError:
        print(">> Lỗi: Dữ liệu không hợp lệ (Sai định dạng thời gian hoặc kiểu số)!")