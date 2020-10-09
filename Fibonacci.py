# Program that shows the first 10 numbers of the Fibonacci's sequence

n1=0
n2=1

print(n1)
print(n2)

for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3