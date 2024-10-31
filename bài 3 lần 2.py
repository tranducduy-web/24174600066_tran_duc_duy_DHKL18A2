number1 = float (input("Số thứ nhất: "))
number2 = float (input("Sô th hai: "))
number3 = float (input("Số thứ ba: "))

if number >= number2 and number1 >= number3:
    max_number = number1
elif number2 >= number and number2 >= number3:
    max_number = number2
else:
    max_number = number3
    
print(f"Số lớn nhất trong 3 số là: {max_number)")
