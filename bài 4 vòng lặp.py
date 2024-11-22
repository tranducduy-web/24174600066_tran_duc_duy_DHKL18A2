num = int(input("Nhập một số nguyên: "))  

if num < 2:  
    print("không phải là số nguyên tố.")  
else:  
    is_prime = True  
    for i in range(2, num):  
        if num % i == 0:  
            is_prime = False  
            break  

    if is_prime:  
        print("là số nguyên tố.")  
    else:  
        print("không phải là số nguyên tố.")
