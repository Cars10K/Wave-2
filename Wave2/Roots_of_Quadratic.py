print("This program calculates the real roots of a quadratic equation (if any).")
a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))

Discriminate = b**2 - 4*a*c

if Discriminate < 0:
	print("This quadratic function doesn't have any real roots.")
	
elif Discriminate == 0:
	print("This quadratic function has one real root.")
	
	Root = -b / 2*a 
	
	print("Real root = {}".format(Root))
	
elif Discriminate > 0:
	print("This quadratic function has two real roots.")
	
	Root1 = -b + Discriminate / 2*a
	Root2 = -b - Discriminate / 2*a 
	
	print("Real roots = {} or {}".format(Root1, Root2))