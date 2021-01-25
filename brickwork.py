import fileinput
import sys

# read numbers N and M the dimensions of each layer
n, m = map(int, input().split())

# reading the rest of the input into a two dimensional array
a = [list(map(int, line.split())) for line in fileinput.input()]

# dimensions validation
if m % 2 != 0 or n % 2 != 0:
	print("N and M must be even numbers")
	sys.exit(0)

# input size validation
if len(a) != n:
	print("Input size does not match given dimensions")
	sys.exit(0)
for l in a:
	if len(l) != m:
		print("Input size does not match given dimensions")
		sys.exit(0)

# verifying that there are no bricks in the input spanning 3 rows or 3 columns
for i in range(n):
	for j in range(m - 2):
		if a[i][j] == a[i][j + 1] == a[i][j + 2]:
			print("Invalid bricks found")
			sys.exit(0)
for j in range(m):
	for i in range(n - 2):
		if a[i][j] == a[i + 1][j] == a[i + 2][j]:
			print("Invalid bricks found")
			sys.exit(0)
			
# initialize the second layer array with the first two empty lines to be filled in the next step
b = [[], []]

# fill the bottom two lines of the second layer, we fill them by blocks of 2 x 2
for i in range(0, m, 2):
	if a[0][i] == a[0][i + 1]:
		b[0].extend((i + 1, i + 2))
		b[1].extend((i + 1, i + 2))
	else:
		b[0].extend((i + 1, i + 1))
		b[1].extend((i + 2, i + 2))

# fill the rest of the second layer (no constraints)
for i in range(2, n):
	b.append([])
	for j in range(m // 2):
		b[i].extend((i * m // 2 + j + 1, i * m // 2 + j + 1))

# reverse the list to display it
b.reverse()

for i in range(n):
	for j in range(m):
		print("%d "%b[i][j], end="")
	print()