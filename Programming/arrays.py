arr = [1, 2, 3, 4, 6, 7, 3, 6, 3]


def add_integers(arr, num):
    arr += [num]
    return arr


print(f"The array with new element is {add_integers(arr, 5)}")


def arr_avr(arr):
    arr_len = len(arr)
    sum_arr = 0
    for i in arr:
        sum_arr += i
    return sum_arr/arr_len


print(f"The average of the Array is {arr_avr(arr)}")

index = arr.index(5)
print("Index of 5: ", index)

index = arr.index(4)
print("Index of 4: ", index)

identify = 3
if identify in arr:
    print("Number Exist")
else:
    print("Number does not Exist")

for num in arr:
    if num == identify:
        print("Value Exist")
        break
else:
    print("Value does not Exist")

arr.remove(5)
print(f"The arr after removing the value 5 {arr}")

copied_arr = arr
print(f"This is a Copied array {copied_arr}")

arr.insert(3, 10)
print(f"array after inserting the value 10 at index 3: {arr}")

min_value = min(arr)
max_value = max(arr)
print(f"The minimun value {min_value} is at the index: {arr.index(min_value)}")
print(f"The maximun value {max_value} is at the index: {arr.index(max_value)}")

print(f"The reverse of the array {arr} is {arr[::-1]}")

duplicates = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            duplicates.append(arr[j])
print(f"Duplicate elements in given array:{duplicates}")


print(f"Common values in given arrays: {set(arr).intersection(copied_arr)}")

duplicate_removed_arr = list(set(arr))
print(f"Duplicates removed array: {duplicate_removed_arr}")

arr.sort()
print(f"The second largest number of the array is {arr[-2]}")

no_even = 0
no_odd = 0
for num in arr:
    if num % 2 == 0:
        no_even += 1
    else:
        no_odd += 1
print(f"The Number of even number in the array is {no_even}")
print(f"The Number of odd numbers in the array is {no_odd}")

print(
    f"The difference between the largest number and the smallest number is {max_value-min_value}")
if 12 in arr:
    print(f"12 Exists in the array")
else:
    print(f"12 does not exist in the array")
if 23 in arr:
    print(f"23 Exists in the array")
else:
    print(f"23 does not exist in the array")
print(f"The array without duplicates: {list(set(arr))}")
