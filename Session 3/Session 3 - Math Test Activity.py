# ----- Program Setup -----
student_number = 1          # This makes sure that the test can check to see which student to assign the current name and score to.

student_1_score = 0         #
student_2_score = 0         # This stores the different students' scores.
student_3_score = 0         #

# ----- The Maths Test -----
def test(score):
    score = 0
    global student_1_score          #
    global student_2_score          # This imports the three student score global variables.
    global student_3_score          #

    # ----- Question 1 -----
    print ("Question 1: ")
    q1 = input ("What is 32 + 45?: ")

    if q1 == "77":
        score += 1                  #
    else:                           # When a question is correct, it adds 1 to the overall score. If incorrect, it's adds nothing.
        score += 0                  #

    # ----- Question 2 -----
    print ("Question 2: ")
    q2 = input ("What is 3²?: ")

    if q2 == "9":
        score += 1
    else:
        score += 0

    # ----- Question 3 -----
    print ("Question 3: ")
    q3 = input ("What is 110 ÷ 11?: ")

    if q3 == "10":
        score += 1
    else:
        score += 0
    
    # ----- Question 4 -----
    print ("Question 4: ")
    q4 = input ("What is 320 - 130?: ")

    if q4 == "190":
        score += 1
    else:
        score += 0

    # ----- Question 5 -----
    print ("Question 5: ")
    q5 = input ("What is 31 x 5?: ")

    if q5 == "155":
        score += 1
    else:
        score += 0

    # ----- Student Number Control -----
    if student_number == 1:                             #
        student_1_score = score                         # 
    elif student_number == 2:                           # When the test is ran whilst Student Number is 1, it will assign the score to student 1.
        student_2_score = score                         # The process repeats with Students 2 and 3 on the second and third times running respectively.
    else:                                               #
        student_3_score = score                         #

# ----- Below is what's printed in the terminal outside the tests -----

print ()
print ("Welcome to your maths tests.")
print ()

# ----- Quiz for Student 1 -----
print ("Student 1: ")                                   #
student_1_name = input ("Please enter your name: ")     #
test(0)                                                 # This calls the first student, runs the test, prints the individual's score. 
print (f"Your score is: {student_1_score}")             # It then sets the student number to 2 before moving on.
student_number = 2                                      #
print ()                                                #

# ----- Quiz for Student 2 -----
print ("Student 2: ")                                   #
student_2_name = input ("Please enter your name: ")     #
test(0)                                                 # This calls the second student, runs the test, prints the individual's score.
print (f"Your score is: {student_2_score}")             # It then sets the student number to 3 before moving on.
student_number = 3                                      #
print ()                                                #

# ----- Quiz for Student 3 -----
print ("Student 3: ")                                   #
student_3_name = input ("Please enter your name: ")     #
test(0)                                                 # This calls the third student, runs the test, prints the individual's score. It then moves on to the results.
print (f"Your score is: {student_3_score}")             # 
print ()                                                #

# ----- Results -----
student_1_results = (student_1_name, student_1_score)   #
student_2_results = (student_2_name, student_2_score)   # This compiles the students' names and scores into variables that correspond with each student.
student_3_results = (student_3_name, student_3_score)   #

student_list    = [student_1_results, student_2_results, student_3_results]     # This compiles the results into a list. 
sorted_list     = sorted(student_list)                                          # Then, another list is made by sorting them in ascending order.

print ("Results: ")
print ("1st", *sorted_list[0], sep=", ")                # This prints off the three places and displays the values from "sorted_list".
print ("2nd", *sorted_list[1], sep=", ")                # The asterisk before it changes the formatting to be more readable.
print ("3rd", *sorted_list[2], sep=", ")                # The 'sep=", " ' means that each parameter that is printed off will be separated by a comma, followed by a space.

print ()
print ("Thank you for participating in this test.")