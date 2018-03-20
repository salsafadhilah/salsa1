print ("            Operator Kondisi Pada Python \n")

print("\n 1. Arithmetic Operators\n")

#penjumlahan
a=10+4
#pengurangan
b=10-4
#perkalian
c=10*4
#pembagian
d=10/4
#floor(hasil bagi)
e=10//4
#modulus(sisa hasil bagi)
f=10%4
#exponent (pangkat)
g=10**4
print(a, b, c, d, e, f, g)
print("\n 2. Assighment Operators\n")

#sama dengan
a=3
print(a)
#tambah sama dengan
a+=2
print(a)
#ambil sama dengan
a-=2
print(a)
#kali sama dengan
a*=2
print(a)
#bagi sama dengan
a/=2
print(a)
#modulus sama dengan
a%=2
print(a)
#floor sama dengan
a//=2
print(a)
#pangkat sama dengan
a**=2
print(a)

print("\n 3. Comparison Operators\n")

#lebih dari
a=3>6
#kurang dari
b=3<6
#sama dengan
c=3==6
#faktorial sama dengan
d= 3!=6
#lebih dari sama dengan
e= 3>=6
#kurang dari sama dengan
f= 3<=6
print(a, b, c, d, f)
print("\n 4. Logical Operators\n")

#AND
a= True and True
b= True and False
c = False and False
print (a, b, c)
#OR
a= True or True 
b= True or False
c= False or False
print(a, b, c)
#NOT
a= not True
b= not False
print(a, b)
print("\n 5. Bitwise Operator\n")
a=input("masukkan nilai a : ")
b = input("masukkan nilai b : ")
#And/&
c= a & b
print "a & b =%s" %c
#or/|
print"a | b =%s" %c
#xor/^
print"a ^ b =%s"%c
#negasi/~
print"a ~ b =%s"%c
#left shift/<<
print "a << b =%s"%c
#right shift
print"a >> b =%s"%c

print("\n 6. Membership Operators\n")

#in
a = [1, 2, 3, 4, 5]
print 5 in a
print 6 in a
#not in
b = [1, 2, 3, 4, 5]
print 5 not in b
print 6 not in b

print("\n 7. Identify Operators")

#is
a, b = 10, 10
print a is b #hasil akam true karena nilai sama
#is not
a, b = 10, 5
print a is not b #hasil akan true karena nilai berbeda


