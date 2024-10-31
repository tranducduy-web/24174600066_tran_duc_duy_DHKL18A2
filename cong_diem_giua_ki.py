diem_giua_ki = float(input("nhap diem giua ki: "))
diem_cuoi_ki = float(input("nhap diem cuoi ki: "))
diem_chuyen_can = float(input("nhap diem chuyen can: "))

diem_trung_binh = (diem_giua_ki + diem_cuoi_ki +diem_chuyen_can) / 3

if diem_trung_binh >= 9:
    ket_qua = "A"
elif diem_trung_binh >=7:
    ket_qua = "B"
elif diem_trung_binh >=5:
    ket_qua = "C"
else:
    ket_qua = "D"

print("diem trung binh la: " + str(diem_trung_binh))
print("xep loai diem": + ket_qua)