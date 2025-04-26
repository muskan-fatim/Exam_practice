import random

personalityQuestions = [
    {
        "question": "Do you like to hang out with friends?",
        "yes_means": "extrovert"
    },
    {
        "question": "Do you enjoy spending time alone?",
        "yes_means": "introvert"
    },
    {
        "question": "Do you like to read books quietly?",
        "yes_means": "introvert"
    },
    {
        "question": "Do you enjoy loud social events?",
        "yes_means": "extrovert"
    },
    {
        "question": "Do you prefer watching movies at home over going to a cinema?",
        "yes_means": "introvert"
    },
    {
        "question": "Do you have a large group of friends?",
        "yes_means": "extrovert"
    },
    {
        "question": "Are you usually the first to speak in group discussions?",
        "yes_means": "extrovert"
    },
    {
        "question": "Do you often need time alone to recharge?",
        "yes_means": "introvert"
    },
    {
        "question": "Do you feel energized after spending time with people?",
        "yes_means": "extrovert"
    },
    {
        "question": "Do you feel drained after social interactions?",
        "yes_means": "introvert"
    }
]

def ask_question():
    print("🎯 Welcome to the Personality Analyzer 🎯")
    introvert_score = 0
    extrovert_score = 0

    # Shuffle and ask 7 random questions
    questions = random.sample(personalityQuestions, 7)

    for q in questions:
        print("\n" + q["question"])
        answer = input("Answer (Yes/No): ").strip().lower()

        if answer == "yes":
            if q["yes_means"] == "introvert":
                introvert_score += 1
            else:
                extrovert_score += 1
        elif answer == "no":
            # Optional: reverse score (for more depth), or ignore
            pass

    print("\n📊 Test Completed!")
    print(f"Introvert Score: {introvert_score}")
    print(f"Extrovert Score: {extrovert_score}")

    if abs(introvert_score - extrovert_score) <= 1:
        print("🌀 You seem to be an **Ambivert** (a balance of both).")
    elif introvert_score > extrovert_score:
        print("🌙 You show more **Introverted** traits.")
    else:
        print("🌞 You show more **Extroverted** traits.")

ask_question()
