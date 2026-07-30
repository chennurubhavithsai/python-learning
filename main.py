while True:

    score = 0

    questions = [
        {
            "question": "1. What is the output of print(5 + 3)?",
            "options": ["A. 53", "B. 8", "C. Error", "D. None"],
            "answer": "B"
        },
        {
            "question": "2. Which keyword is used to create a function?",
            "options": ["A. function", "B. define", "C. def", "D. func"],
            "answer": "C"
        },
        {
            "question": "3. Which data type stores True or False?",
            "options": ["A. int", "B. bool", "C. string", "D. list"],
            "answer": "B"
        },
        {
            "question": "4. Which symbol is used for comments?",
            "options": ["A. //", "B. <!--", "C. #", "D. **"],
            "answer": "C"
        },
        {
            "question": "5. Which loop repeats while a condition is True?",
            "options": ["A. for", "B. while", "C. repeat", "D. loop"],
            "answer": "B"
        },
        {
            "question": "6. Which function is used to get user input?",
            "options": ["A. print()", "B. input()", "C. scan()", "D. read()"],
            "answer": "B"
        },
        {
            "question": "7. Which symbol is used for assignment?",
            "options": ["A. =", "B. ==", "C. :", "D. +"],
            "answer": "A"
        },
        {
            "question": "8. Which keyword exits a loop?",
            "options": ["A. continue", "B. stop", "C. break", "D. exit"],
            "answer": "C"
        },
        {
            "question": "9. Which data type stores multiple values?",
            "options": ["A. list", "B. int", "C. float", "D. bool"],
            "answer": "A"
        },
        {
            "question": "10. Which keyword is used for conditions?",
            "options": ["A. for", "B. while", "C. if", "D. input"],
            "answer": "C"
        }
    ]

    print("\n===== PYTHON QUIZ =====")

    player = input("Enter your name: ")

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    percentage = (score / len(questions)) * 100

    print("\n===== RESULT =====")
    print("Player:", player)
    print("Score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")

    if percentage >= 50:
        print("🎉 PASS")
    else:
        print("📚 FAIL")

    # Save score
    with open("scores.txt", "a") as file:
        file.write(f"{player},{score}\n")

    # Find highest score
    highest_score = 0
    topper = ""

    with open("scores.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(",")

            if int(marks) > highest_score:
                highest_score = int(marks)
                topper = name

    print("\n🏆 Highest Score")
    print("Player :", topper)
    print("Score  :", highest_score)

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for playing!")
        break