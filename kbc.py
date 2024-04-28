
questions=[
    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],
    
    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],
    
    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],
        [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],
    
    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],
    
    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],

    [
        "Question HERE","Option1","Option2","Option3","Option4","int value of correct number of option hwere"
    ],


    
]



levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]


m=0
for i in range(0,len(questions)):
    print(f"Question for Rs.{levels[i]}: {questions[i][0]}\n")

    print(f"Option A.{questions[i][1]}         Option B.{questions[i][2]}")
    print(f"Option c.{questions[i][3]}         Option D.{questions[i][4]}") 

    ans=int(input("Enter your answer(1-4) or 69 to quit the game"))

    if ans==69:
        m=levels[i-1]
        break

    if ans==questions[i][5]:
        print("Correct answer")


        if i==4:
            m=10000
        elif i==9:
            m=320000

    else:
        print("Wrong answer")
        break


print("FINAL TAKE HOME MONEY IS: ",m)

