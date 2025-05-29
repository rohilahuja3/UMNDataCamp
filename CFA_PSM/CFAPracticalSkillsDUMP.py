import numpy as np

arr1 = ['A', 'B', 'C', 'D']
for i in range(len(arr1)):
    print("Company name is {}".format(arr1[i]))

arr2 = ['A2', 'B2', 'C2', 'D2']
for i in arr2:
    print("Company name is {}".format(i))

arr3 = ['A3', 'B3', 'C3', 'D3']
for i in arr3:
    print(f"Company name is {i}")

print("#############################################")

arr_new = np.array(['A', 'B', 'C', 'D'])
for i in range(len(arr_new)):
    print("Name {}".format(arr_new[i]))

arr_new = np.array(['A', 'B', 'C', 'D'])
for i in arr_new:
    print("Name {}".format(i))

arr_new = np.array(['A', 'B', 'C', 'D'])
for i in arr_new:
    print(f"Name {i}")