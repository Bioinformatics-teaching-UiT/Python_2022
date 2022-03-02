"""
Script to calculate the mean
Takes in a list of numbers
Returns the mean
"""

def get_mean(listofnumbers, totalval):
    for num in listofnumbers:
        totalval += num
        meanval = totalval / len(listofnumbers)
    return totalval, meanval

num_list = [1, 5.6, 8, 101]
sum1, mean1 = get_mean(num_list, 0)
print(f'Your sum is {sum1}, mean is {mean1}!')
sum2, mean2 = get_mean([10, 2.333, -1], 0)
print(f'Your sum is {sum2}, mean is {mean2}!')
sum3, mean3 = get_mean([1,2,3,4,5], 0)
print(f'Your sum is {sum3}, mean is {mean3}!')


