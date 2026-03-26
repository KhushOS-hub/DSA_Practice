arr = [4,5,6,7,8,9,10]

x = 5
i = 0
j = len(arr) - 1

while i <= j:
    mid = i + (j -i)//2
    if arr[mid] == x:
        print(f"Found {x} at index {mid}")
        break
    elif arr[mid] < x:
        i = mid + 1
        print(i)
    else:
        j = mid - 1
        print(j)
