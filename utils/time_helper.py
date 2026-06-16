from datetime import datetime, timedelta

def calculate_eta(flight_list):
    fid = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    for f in flight_list:
        if f['flight_id'] == fid:
            start_time = datetime.strptime(f['depart_time'], "%Y-%m-%d %H:%M:%S")
            eta = start_time + timedelta(minutes=f['duration_min'])
            print(f"-> Chuyến bay {fid} cất cánh lúc: {f['depart_time']}")
            print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
            return
    print(">> Không tìm thấy chuyến bay!")