

# def binary_search(data, target):

# 	low = 0
# 	high = len(data)-1

# 	while low <= high:
# 		mid = (low + high)  // 2
# 		guess = data[mid]

# 		if guess == target:
# 			print(f"Number {data[mid]} found!")
# 			return f"Index : {mid}"
# 		if guess > target:
# 			high = mid - 1
# 		else:
# 			low = mid + 1
# 	return None


# x = [1,2,3,4,5,6,7,8,9,10]
# t = 9
# print(binary_search(x, t))


# Binary search practice 2

def binary_search(data, target):
	low = 0
	high = len(data)-1

	while low <= high:
		mid = (low + high) // 2
		guess = data[mid]

		if guess == target:
			print(f"Found {data[mid]}")
			print(f"at index : {mid}")
			return mid
		if guess < target:
			low = mid + 1
		else:
			high = mid - 1
	return None

l = [1,2,3,4,5,6,7,8,9,10]
t = 6
print(binary_search(l, t))


















