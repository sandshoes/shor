from random import randint

s = 0
n = int(input('Insert number here: '))
p = n - 1

if p%2 != 0:
	print('Number is not odd')
	quit()

while p % 2 == 0:
	p = p/2
	s += 1
print(s)

d = (n-1)/(2**s)
t = 0
for i in range(4):
	a = randint(2, n-1)
	x = pow(a,d,n)
	for r in range(s):
		d = (n-1)/(2**r)
		x = pow(a,d,n)
		if x == 1 or x == n-1:
			t=1
			continue
if t==0:
	print('The number is not prime')
if t==1:
	print('The number is prime')

