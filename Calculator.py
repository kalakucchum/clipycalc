print("Welcome to the Command Line Interface Calculator! The calculator can do some basic operations.")
print("For Addition, Press 1.")
print("For Subtraction, Press 2.")
print("For Multiplication, Press 3.")
print("For Divison, Press 4.")
print("For Power, Press 5.")
print("For Root Power, Press6")
x = int(input("What do you want to do ? "))
if x == 1:
	y = float(input("Enter the first number , Please ! : "))
	z = float(input("Enter the second number , Please ! : "))
	r = y + z
	print("The Sumession is",r,".")
elif x == 2:
	y = float(input("Enter the first number , Please ! : "))
	z = float(input("Enter the second number , Please ! : "))
	r = y - z	
	print("The result is",r,".")
elif x == 3:
	y = float(input("Enter the first number , Please ! : "))
	z = float(input("Enter the second number , Please ! : "))
	r = y * z	
	print("The result is",r,".")
elif x == 3:
	y = float(input("Enter the dividend , Please ! : "))
	z = float(input("Enter the divisor , Please ! : "))
	r = y / z
	d = y % z	
	print("The quotient is",r,".")
	print("The remainder is",d,".")
elif x == 4:
	y = float(input("Enter the base , Please ! : "))
	z = float(input("Enter the power , Please ! : "))
	r = y ** z
	print(y,"to the power",z,"is",r)
elif x == 5:
	y = float(input("Enter the base , Please ! : "))
	z = float(input("Enter the root power , Please ! : "))
	m = 1 / z
	r = y ** m
	print(y,"to the power",z,"is",r)






