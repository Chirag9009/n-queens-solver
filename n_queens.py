def can_be_extended(perm):
	"""
	Function: Checks whether a given premutation can be extended further or not.
	input arguments: perm=current permutation that is to be extended, as a list of integer values
	returns: Boolean true if permutation can be extended, false otherwise
	"""
	i = len(perm) - 1
	for j in range(i):
		if i-j == abs(perm[i] - perm[j]): #checks the diagonal of the last added queen in the permutation
			return False
	return True

def n_queens(perm, n):
	"""
	Function: Prints the solutions found for n-queens problem as soon as it is found.
		  The solution is a list with columns where a queen is placed.
	input arguments: perms=current permutation, as a list of integer values 
			 n = number of queens to be placed, integer value
	returns: total number of solutions possible for the given problem
	"""
	if len(perm) == n:
		#print the current sequence of placements if all the queens have been placed.
		print(perm)
		return 1
	else:
		count = 0
		for i in range(n):
			if i not in perm: #if column is not present in current solution then check if it can be extended without conflicts.
				perm.append(i)
				if can_be_extended(perm):
					count += n_queens(perm, n)
				perm.pop()
	return count

if __name__ == "__main__":
	n = int(input("Enter n:"))
	print(n_queens([], n))
