# Ham isqrt tra ve so nguyen <= isqrt(n)
def isqrt(n):
	x=n
	y=(x+n//x)//2
	while(y<x):
		x=y
		y=(x+n//x)//2
	return int(x)
# Ham fermat thuc hien giai thuat fermat de phan tich n thanh 2 uoc
def fermat(n):
	t0=isqrt(n)+1 	# Bat dau tu so sqrt(n)
	counter=0
	t=t0+counter
	temp=isqrt((t*t)-n)	# temp = t^2 -n
	while((temp*temp)!=((t*t)-n)):	# lap cho toi khi temp la binh phuong cua mot so nguyen
		counter+=1
		t=t0+counter
		temp=isqrt((t*t)-n)
	s=temp
	p=t+s
	q=t-s
	return p,q 	# Tra ve hai uoc cua n
def isprime(n):
	for i in range(2, isqrt(n)+1):
		if n%i == 0:
			return False
	return True
# Ham kiem tra so co phai so ban nguyen to hay khong
def checksemi(i):
	# Voi so chan
	if (i%2 == 0):
		x = i/2
		if isprime(x):
			return 1,2,x
		else:
			return 0,0,0
	# Voi so nguyen
	if isprime(i):
		return 0,0,0
	# Phan tich so le bang fermat
	a,b = fermat(i)
	if (isprime(a) and isprime(b)):
		return 1,a,b
	else:
		return 0,0,0

def euclid(a, b):
	r1 = a 
	r2 = b
	s1 = 1
	s2 = 0
	t1 = 0
	t2 = 1
	while(r2>0):
		q = r1//r2
		r = r1 - q*r2
		r1 = r2
		r2 = r 

		s = s1 - q*s2
		s1 = s2
		s2 = s 

		t = t1 - q*t2
		t1 = t2
		t2 = t 
	return r1, s1, t1

def listed(p,q):
	n=p*q
	phi = (p-1)*(q-1)
	result = []
	for i in range(2,isqrt(phi)+1):
		a,b,c=euclid(phi,i)
		if a != 1:
			continue
		else:
			if c<0:
				c+=phi
			result.append(str((i,c)))

	with open ("boso.txt", "w") as f:
		f.write("N = %s\np = %s,q = %s, phi = %s\n" %(n, p, q, phi))
		count = 0
		for i in result:
			f.write(i+"\t")
			count+=1
			if count ==10:
				f.write("\n")
				count =0

# Bat dau chuong trinh
print("Thuc hien tim so nua nguyen to gan so n nhat va lon hon n.")
n = int(input("Nhap gia tri n: "))
if n%2 ==0:
	n+=1
check,p,q =checksemi(n)
while(check != 1):
	n+=2
	check,p,q =checksemi(n)

listed(p,q)