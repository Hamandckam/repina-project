arr = input().split(" ")
n = int(arr[0])

arr.remove(arr[0])

suma = 0

for x in arr:
    y = int(x)

    if(y // 100 == 0 and y // 10 != 0):
        suma = suma + y

print(suma)