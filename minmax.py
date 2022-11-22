
# Importing Libraries
import math

# Defining minmax algorithm1
def minmax (current_depth, index,
			maximum, values,
			target_depth):

	# condition to check if current depth reached the desired target depth,
	# If yes then it will return the value.
	if (current_depth == target_depth):
		return values[index]
	
        # IF the function is of extracting MAX then run it,
        # ELSE run for extracting MIN
	if (maximum):
		return max(minmax(current_depth + 1, index * 2,
					False, values, target_depth),
				minmax(current_depth + 1, index * 2 + 1,
					False, values, target_depth))
	
	else:
		return min(minmax(current_depth + 1, index * 2,
					True, values, target_depth),
				minmax(current_depth + 1, index * 2 + 1,
					True, values, target_depth))
	
# Values given in fig 6.2
values = [3, 12, 8,2,4,6,14,5,2]

# Tree Depth intialises as 3 
treeDepth = math.log(len(values), 3)
print("Terminal Nodes: ", values)
print("\nRESULT:\nOPTIMAL VALUE: ", end = "")
print(minmax(0, 0, True, values, treeDepth))

