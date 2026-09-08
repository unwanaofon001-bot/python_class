# def eligibility_checker(age, has_ticket):
#     # age = 18
#     # has_ticket = True

#     if age >= 18 and has_ticket == True:
#         return True
#     else:
#         return False

        
def student_grade():
    print("Enter student name: ")
    student_name = input()

    print("how many score do you want to enter?")
    num_scores = int(input())

    scores = []

    for i in range(num_scores):
        print(f"Enter score number {i + 1}:")
        score = int(input())
        scores.append(score) 


    total_score = sum(scores)
    average = total_score / len(scores)
        
    if average >= 50:
        result = "PASS"
    else:
        result = "FAIL"
    print("-----SUMMARRY------")
    print(f"Name: {student_name}") 
    print(f"Total Score: {total_score}")
    print(f"Average: {average}")
    print(f"Reult: {result}")

 
   
student_grade()   


