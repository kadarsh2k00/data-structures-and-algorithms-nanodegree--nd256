names =  ['Roop','Shubh','Paaav']
assignments = [2,4,1]
grades = [78,60,85]

# message string to be used for each student
# HINT: use .format() with this string in your for loop
for i in range(len(names)):
    improved=grades[i]+(2*assignments[i])
    message = '''Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n'''.format(names[i],assignments[i],grades[i],improved)
    print(message)
