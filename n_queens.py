def can_be_extended(perm):
	i = len(perm) - 1
	for j in range(i):
		if i-j == abs(perm[i] - perm[j]):
			return False
	return True

def n_queens(perm, n):
	if len(perm) == n:
		#print the current sequence of placements if all the queens have been placed.
		print(perm)
		return 1
	else:
		count = 0
		for i in range(n):
			if i not in perm:
				perm.append(i)
				if can_be_extended(perm):
					count += n_queens(perm, n)
				perm.pop()
	return count

if __name__ == "__main__":
	n = int(input("Enter n:"))
	print(n_queens([], n))
