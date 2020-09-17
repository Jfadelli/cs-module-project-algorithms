'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #create a character map to count the number of times a character appears in the array
    char_map = {}
    for num in arr:
        if num in char_map:
            char_map[num] += 1
        else:
            char_map[num] = 1
    for key in char_map:
        if char_map[key] == 1:
            return key
single_number([1,2,3,4,4,3,2])

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")