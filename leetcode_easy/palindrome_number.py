
# DECOMPOSITION


# get left digit
# get right digit
# compare left and right
# chop off left and right digits
# everytime we remove two digits from the num, also remove two digits from divisor 


# ====================================================
# How do you get the right value? 
	# mod the number by 10 to get the ones place.

		# Since every digit to the left is a multiple of 10, it divides evenly with 0 remainder.
		# The only digit that isn't a multiple of 10 is the ones digit itself.
		# Therefore, the remainder has to be the ones digit.

# How do we get the left value? 
	# divide it by the amount in it's biggest place value. 
	# if 121, divide it by 100 to get the left digit.

# How do we remove the ones place digit?
	# floor divide the num by 10 (floor division rounds down)

# How do we remove the left digit?
	# mod it by the number in it's biggest place value (eg: 100, 1000), the remainder will be all the remaining digits.

# "Keep increasing divisor by factor of 10 until dividing x by it gives us a single digit (the leftmost digit)."?
	# get the most significant divisor we can that is still less than or equal to the x
	# while x // divisor >= 10:
# ====================================================

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
    	if x < 0:
    		return False

    	divisor = 1

    	# Is x at least 10 times the current divisor?
    	while x >= 10 * divisor:
    		divisor *= 10 # increase divisor by next power of 10

    	while x:
    		right = x % 10
    		left = x // divisor

    		if left != right:
    			return False

    		x = (x % divisor) // 10 # chop off two digits from num
    		divisor = divisor // 100 # chop off two digits from divisor

    	return True 


    	

