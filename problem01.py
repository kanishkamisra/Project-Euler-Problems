s = 0
for n in range(0,1000):
	if n % 3 == 0 or n % 5 == 0:
		s += n

print s

# or

print sum(n for n in range(1000) if n % 5 == 0 or n % 3 == 0)