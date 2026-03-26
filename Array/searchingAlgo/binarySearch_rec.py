arrSort = [3,5,6,7,10,13,15,24]

x = int(input("Enter the number you want to search: "))
i = 0
j = len(arrSort) - 1

def binarySearch(arrSort, i, j, x):
    if i <= j:
        mid = i + (j - i)//2

        if arrSort[mid] == x:
            return mid
        elif arrSort[mid] < x:
            return binarySearch(arrSort, mid + 1, j, x)
        else:
            return binarySearch(arrSort, i, mid - 1, x)
        
    return -1

result = binarySearch(arrSort, i, j, x)

if result == -1:
    print("No such number Found")
else:
    print(f"Found at index {result}")