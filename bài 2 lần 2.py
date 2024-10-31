x = float (input( "Nhập hoành độ x của điểm M: "))
y = float(input( "Nhập tung độ y của điểm M: "))
a = float (input( "Nhập hoành độ a của tâm I: "))
b = float(input( "Nhập tung độ b của tâm I: "))
R = float(input( "Nhập bán kính R của hình tròn: "))

cac _diem = f"M({x}, {y}), I({a}, {b}), R={R}"
tinh_khoang_cach = (x - a) * 2 + (y - b) * 2
tinh_khoang_cach <= R ** 2

if cac_diem:
    print( "True: Điểm M nằm trong hoặc trên hình tròn.")
else :
    print ("False: Điểm M nằm ngoài hình tròn.")