n = int(input("Nhập một số nguyên n: "))  
so_nguyen_to = []  
 
for num in range(2, n):  
    is_prime = True  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            is_prime = False
            break  
    if is_prime:  
        so_nguyen_to.append(num)  

print(f"Các số nguyên tố nhỏ hơn là: {so_nguyen_to}")