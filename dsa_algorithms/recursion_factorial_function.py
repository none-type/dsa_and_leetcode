# Recursion = function calling itself until it hits a stop condition.

# This function:
#     fact(3) asks: "What's 3 × fact(2)?"
#     fact(2) asks: "What's 2 × fact(1)?"
#     fact(1) says: "It's 1" (stop)

# Then answers flow backward: 2×1=2, then 3×2=6
# Like passing a note: Each call waits for the next one to finish. The last one gives the answer, then each passes it back, multiplying as it goes.
# Stop condition = x == 1 (prevents infinite loop).

# Each call is literally paused mid-calculation, frozen in time, waiting for the one below to hand back a number. 
# When it gets that number, it unpauses, does its multiplication, and hands its number back up.

def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x-1)

print(fact(3))