questions = [
   ["who is shah rukh khan?", "WWE wrestler", "Actor", "Astronaut","Plumber",3],
   [" what is the capital of India ?", "Mumbai", "Delhi", "New York", " Punjab", 2],
   ["Which planet is known as red planet?", "Earth", "Mars", "Venus", "Jupitar", 2],
   ["What is the largest mammal?", "Elephant", "Blue whale", "Giraffe", "Shark", 2]
]

prizes = ["1000$,  2000$,  3000$,  4000$"]
# sum = 0
i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")    
    print(f"d. {question[4]}")    

    # check whweter the ans is correct or not

    a = int(input("Enter your answer. 1 for a , 2 for b, 3 for c, 4 for d "))
    if (question[5]== a):
        print("correct answer")
    else :
        print(f"incorrect, the correct answer was {question[5]}")
        print("Better luck next time !")
        break    
    # sum += prizes[i]         # this was for 1 , 2, 3, 4,  prize if i diidnt want i remove it
    print("You won {[i]}")
    i += 1