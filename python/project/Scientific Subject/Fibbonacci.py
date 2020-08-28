n = 2
Fb = [0,1]

S = int(input("Limit: ")) 
while n > 1:
	L = (n-1) + (n-2)
	Fb.append(L)	
	n = n + 1
	
	if n == S:
		break
		
print(Fb)

