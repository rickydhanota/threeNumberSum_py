# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all the triplets in the array that sum up to the target sum and return a 2 dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplet themselves should be ordered in acsending order with respect to the numbers they hold.

# If no threee numbers sum up to the tagret sum, the function should return an empty array
# example array = [12,3,1,2,-6,5,-8,6], targetSum = 0
# sample output should be [[-8,2,6], [-8,3,5], [-6,1,5]]

def threeNumberSum(array, targetSum):
    array.sort() #sorts the array, built in python function
    triplets = []
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets

print(threeNumberSum([12,3,1,2,-6,5,-8,6], 0)) # sorted array would be [-8,-6, 1, 2, 3, 5, 6, 12]