#Bitwise Operators
#$ | ~ ^
#to manupulate single bits of data, and return 0 or 1 based on the value of the bits that are used
#two 1 => 1&1
#at least 1 => 1|1   0|1    1|0
#exactly 1  => 0^1   1^0


print(15 & 22) #Conjunction Bitwise operator
#15 -> 0 0 0 0 1 1 1 1
#22 -> 0 0 0 1 0 1 1 0
#?  -> 0 0 0 0 0 1 1 0 => this bits corresponds as a result 6 => two 1 equals to 1

print(15 | 22) #Disjunction
#15 -> 0 0 0 0 1 1 1 1
#22 -> 0 0 0 1 0 1 1 0
#?  -> 0 0 0 1 1 1 1 1 => this bits corresponds as a result 31 => one of the bits 1 equals to 1 

print(15 ^ 22) #Exclusive - "OR" operator
#15 -> 0 0 0 0 1 1 1 1
#22 -> 0 0 0 1 0 1 1 0
#?  -> 0 0 0 1 1 0 0 1 => this bits corresponds as a result 31 => one of the bits 1 equals to 1,but if both of them 1 equals to 0 

print(~22) #Negation operator
#22 -> 0 0 0 1 0 1 1 0
#?  -> 1 1 1 0 1 0 0 1 => this bits corresponds as a result 31 => one of the bits 1 equals to 1, if 1 = 0, 0 = 1 (-)

#Bit Shifting
# >> (Bit Shifting Right) 
# << (Bit Shifting Left)
# to move bit from certain amount of places

print (22 >> 1)
#22 -> 0 0 0 1 0 1 1 0
#?  -> 0 0 0 0 1 0 1 1

print (22 >> 2)
#22 -> 0 0 0 1 0 1 1 0
#?  -> 0 0 0 0 0 1 0 1

print (22 << 1)
#22 -> 0 0 0 1 0 1 1 0
#?  -> 0 0 1 0 1 1 0 0

# Bit Shifting the same as a * and // operators
print(22//2) #print(22>>1)
print(22//4) #print(22>>2)
print(22*2) #print(22<<1)
print(22*4) #print(22<<2)


#quiz
print(5 ^ 11)


a = 20
b = 5
print("a & b =", a & b)


int(1001)


a = 20
b = 5
print("a | b =", a | b)

x = 2
print(x << 2)

print(~200)

print(22 << 1)
