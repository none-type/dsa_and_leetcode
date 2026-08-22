# work in progress divide and conquer recursion problem

def divide_and_conquer(x):
	total = 0
	if not x:
		return total
	else:
		a = x.pop()
		total = a + sum(x)
		divide_and_conquer(x)
x = [1,2,3,4]
print(divide_and_conquer(x))