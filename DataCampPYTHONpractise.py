# x = [1,2,3]
# print(type(x))
# print(x)
# n = len(x)
# print(type(n))
# print(n)

# total = 0
# for i in range(len(x)):
#     total += x[i]
#     print(total)
#     print(type(total))

# avg = int(total/n)
# print(type(avg))
# print(avg)

# pi = 3.148241
# print(type(pi))
# print('I love to eat', pi ,'!')

# pi_str = str(3.148241)
# print(type(pi_str))
# print('I love to eat ' + pi_str +'!')

# cpi = [['R', 'O', 'H', 'I', 'L'], ['M', 'A', 'H', 'A', 'K']]
# print(cpi[0][1:])

# x = [123.45, 345.67, 9812.3, 98.8990, 1.1322334]
# # x.sort()
# print(sorted(x))

# import numpy as np
# array1 = np.array(['123.45', '345.67', '9812.3', '98.8990', '1.1322334'])
# np.set_printoptions(suppress=True, precision=6)
# print(sorted(array1))
# print(type(array1[1]))

# Import numpy as np
import numpy as np

# Lists
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# # NumPy arrays
# prices_array = np.array(prices)
# earnings_array = np.array(earnings)

# # Print the arrays
# print(prices_array)
# print(earnings_array)

# pe_list = []

# for i in range(len(prices_array)):
#     pe_list.append(prices_array[i]/earnings_array[i])

# pe_array = np.array(pe_list)
# print(pe_array)

# #  or u can just divide - property of an array

# pe_list1 = prices_array/earnings_array
# print(type(pe_list1))
# print(pe_list1)

list2d = np.array([prices, earnings])
print(list2d)
print(type(list2d))