rikkei_aviation/
│
├── main.py # File chạy chính, điều hướng menu
├── core/ # Package xử lý nghiệp vụ chính
│ ├── **init**.py
│ ├── logistics.py # Chức năng 1: Thống kê hậu cần
│ └── manager.py # Chức năng 2: Quản lý chuyến bay
└── utils/ # Package chứa các hàm hỗ trợ
├── **init**.py
├── time_helper.py # Chức năng 3: Tính ETA
└── file_helper.py # Chức năng 4: Khởi tạo logs
