def ask_user():
    questions={"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
    while True:
        user_say = input('\n')
        if user_say == "Как дела":
           print(questions["Как дела"])
        elif user_say == "Что делаешь?":
           print(questions["Что делаешь?"])
    
print (ask_user())           