
# Initialising values of Alpha and Beta
MAX, MIN = 1000, -1000

# Returns optimal value for current player
#(Initially called for root and maximizer)
def minmax(current_depth, index, maximium,
			values, alpha, beta):

	# Terminating condition. i.e
	# leaf node is reached
	if current_depth == 3:
		return values[index]

	if maximium:
	
		best = MIN

		# Check for left and right child
		for i in range(0, 2):
			
			val = minmax(current_depth + 1, index * 2 + i,
						False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
		return best
	
	else:
		best = MAX

		# Recur for left and
		# right children
		for i in range(0, 2):
		
			val = minmax(current_depth + 1, index * 2 + i,
							True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
		return best
	

values = [3, 12, 8,2,4,6,14,5,2]
print("Two Ply game")
print("Terminal Nodes", values)
print("The optimal value is :", minmax(0, 0, True, values, MIN, MAX))

values2 = [1, 5, 9,2,4,6,23,13,21,8,7,18,14,3,16,14,15,12]
print("\nFour Ply game")
print("Terminal Nodes", values2)
print("The optimal value is :", minmax(0, 0, True, values2, MIN, MAX))
        

        

	
	

