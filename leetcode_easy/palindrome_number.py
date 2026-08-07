
# DECOMPOSITION


# get left digit
# get right digit
# compare left and right
# chop off left and right digits
# remove two digits from divisor because x has two less digits


# ====================================================
# How do you get the right value? 
	# mod the number by 10 to get the ones place.

# How do we get the left value? 
	# divide it by the amount in it's biggest place value. 

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

    	while x // divisor >= 10:
    		divisor *= 10

    	while x:
    		right = x % 10
    		left = x // divisor

    		if left != right:
    			return False

    		x = (x % divisor) // 10
    		divisor = divisor // 100

    	return True 


    	

