danh_sach_cau_thu = []

# Hàm hiển thị danh sách cầu thủ
def xem_danh_sach():
    print("\nDanh sách cầu thủ:")
    for cau_thu in danh_sach_cau_thu:
        print(cau_thu)
    if not danh_sach_cau_thu:
        print("Danh sách trống.")

def nhap_cau_thu():
    try:
        so_luong = int(input("Nhập số lượng cầu thủ cần thêm: "))
        for _ in range(so_luong):
            ma = input("Nhập mã cầu thủ: ")
            ten = input("Nhập tên cầu thủ: ")
            tuoi = int(input("Nhập tuổi cầu thủ: "))
            vi_tri = input("Nhập vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
            so_huy_chuong = int(input("Nhập số huy chương: "))
            cau_thu = {
                "ma": ma,
                "ten": ten,
                "tuoi": tuoi,
                "vi_tri": vi_tri,
                "so_huy_chuong": so_huy_chuong
            }
            danh_sach_cau_thu.append(cau_thu)
        print("Đã thêm cầu thủ thành công!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số cho tuổi và số huy chương!")

def tinh_thuong():
    try:
        for cau_thu in danh_sach_cau_thu:
            so_huy_chuong = cau_thu["so_huy_chuong"]
            if so_huy_chuong > 10:
                cau_thu["thuong"] = so_huy_chuong * 500000
            elif 5 <= so_huy_chuong <= 10:
                cau_thu["thuong"] = so_huy_chuong * 300000
            else:
                cau_thu["thuong"] = so_huy_chuong * 200000
        print("Đã tính thưởng cho tất cả cầu thủ.")
    except KeyError as e:
        print(f"Lỗi: Thiếu thông tin quan trọng - {e}")

def xoa_cau_thu():
    try:
        ma = input("Nhập mã cầu thủ cần xóa: ")
        for cau_thu in danh_sach_cau_thu:
            if cau_thu["ma"] == ma:
                danh_sach_cau_thu.remove(cau_thu)
                print(f"Đã xóa cầu thủ có mã {ma}.")
                return
        print("Không tìm thấy cầu thủ cần xóa.")
    except Exception as e:
        print(f"Lỗi xảy ra khi xóa cầu thủ: {e}")

def sua_cau_thu():
    try:
        ma = input("Nhập mã cầu thủ cần sửa: ")
        for cau_thu in danh_sach_cau_thu:
            if cau_thu["ma"] == ma:
                print("Nhập thông tin mới:")
                cau_thu["ten"] = input("Nhập tên mới: ")
                cau_thu["tuoi"] = int(input("Nhập tuổi mới: "))
                cau_thu["vi_tri"] = input("Nhập vị trí mới: ")
                cau_thu["so_huy_chuong"] = int(input("Nhập số huy chương mới: "))
                print(f"Đã sửa thông tin cầu thủ có mã {ma}.")
                return
        print("Không tìm thấy cầu thủ cần sửa.")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số cho tuổi hoặc số huy chương!")
    except Exception as e:
        print(f"Lỗi xảy ra khi sửa cầu thủ: {e}")

def sap_xep():
    try:
        danh_sach_cau_thu.sort(key=lambda x: x["so_huy_chuong"])
        print("Đã sắp xếp danh sách cầu thủ theo số huy chương.")
    except Exception as e:
        print(f"Lỗi xảy ra khi sắp xếp: {e}")

while True:
    try:
        print("\nChương trình quản lý cầu thủ:")
        print("1. Xem danh sách cầu thủ")
        print("2. Nhập thông tin cầu thủ")
        print("3. Tính thưởng")
        print("4. Tìm kiếm và xóa cầu thủ")
        print("5. Tìm kiếm và chỉnh sửa thông tin cầu thủ")
        print("6. Sắp xếp danh sách theo số huy chương")
        print("7. Thoát chương trình")
        chon = int(input("Nhập lựa chọn: "))
        
        if chon == 1:
            xem_danh_sach()
        elif chon == 2:
            nhap_cau_thu()
        elif chon == 3:
            tinh_thuong()
        elif chon == 4:
            xoa_cau_thu()
        elif chon == 5:
            sua_cau_thu()
        elif chon == 6:
            sap_xep()
        elif chon == 7:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên cho lựa chọn!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
