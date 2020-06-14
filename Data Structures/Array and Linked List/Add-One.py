
def add_one(arr):
    num =''
    for digit in arr:
        num+=str(digit)
    num = str(int(num)+1)

    num2 = []
    for digit in num:
        num2.append(int(digit))
        
    return num2

# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")      

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)


# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)


# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

