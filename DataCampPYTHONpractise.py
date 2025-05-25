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

# # Lists
# prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
# earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

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

# list2d = np.array([prices, earnings])
# print(list2d)
# print(type(list2d))
# print(list2d.shape)
# print(list2d.size)
# print(list2d.sum(axis=1))
# print(list2d.mean(axis=1))
# print(np.mean(list2d, axis=1)) # better and more preffered works with all arays - list/ndarray and etc
# print(list2d.std(axis=1))
# print(np.sort(list2d[0]))
# print(np.arange(1,13))
# list2d_trans = np.transpose(list2d)
# print(list2d_trans)
# print(list2d_trans[:,1])
# print(list2d[1,6])

# months = np.array(['Jan','Feb','Mar','Apr','May','June','July'])
# index1 = np.array([-1,-2,5,0])
# bool_index = np.array([True, False, False, True, True, True, True])
# months_sub = months[index1]
# print(months_sub)
# print(type(months_sub))
# months_sub1 = months[bool_index]
# print(months_sub1)
# print(type(months_sub1))

# test1 = np.array([-1, 3, 5, 6, 0, -6, -8, 4])
# index2 = (test1>=0)
# print(index2)
# print(type(index2))
# print(test1[index2])

###############################   MODULE 4 - Visualization   #############################
import matplotlib.pyplot as plt

prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
prices_sorted = np.sort(prices)
months = np.arange(1,8)
# plt.plot(months,prices_sorted,color='red',linestyle='-.')
plt.scatter(x=months,y=prices_sorted,color='red')

# add labels
plt.xlabel("Months")
plt.ylabel("Stock Prices")
plt.title("PLOT")

plt.show()
