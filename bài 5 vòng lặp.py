num = int(input("Nhập một số nguyên: "))  
tong_cac_uoc = 0   
for i in range(1, num // 2 + 1):  
    if num % i == 0:  
        tong_cac_uoc += i  

if tong_cac_uoc == num and num != 0:  
    print("là số hoàn hảo.")  
else:  
    print("không phải là số hoàn hảo.")