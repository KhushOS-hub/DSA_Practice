array = [24,65,1,56,3,7,9]

inp = int(input("Enter the number for searching: "))

def linearSearch(array, inp):
    for i in range(len(array)):
        if (inp == array[i]):
            print(f"Found {inp} at {i}th index")
            return True
    return False

result = linearSearch(array, inp)
if(result == False):
    print("No such element present in the array")

        
