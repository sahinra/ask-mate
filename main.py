import data_manager


def display_menu(menu_dict):
    for item in menu_dict.items():
        print(f"{item[0]}- {item[1]}")


def register_or_login():
    start_menu_dict = {
        "1": "Register user",
        "2": "Login user",
        "0": "Exit"
    }
    display_menu(start_menu_dict)
    first_option = int(input("Choose a menu option - "))
    try:
        if first_option == 1:
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            data_manager.register_user(username, email, password)
            return 1
        elif first_option == 2:
            username = input("Username: ")
            password = input("Password: ")
            data_manager.login_user(username, password)
            return 1
    except ValueError as ex:
        print("Invalid input")
        return 0


def logged_in_user_activities():
    option = int(input("Choose a menu option - "))

    user_logged_out = False

    while not user_logged_out:
        try:
            if option == 1:
                data_manager.get_all_questions()
            elif option == 2:
                data_manager.get_all_questions_with_answers()
            elif option == 3:
                index = int(input("Choose an index - "))
                data_manager.get_question_with_answers(index)
            elif option == 0:
                print("You logged out")
                user_logged_out = True
                break
            option = int(input("Choose a menu option - "))
        except ValueError as ex:
            print("Invalid input")
            continue


if __name__ == "__main__":
    print("Welcome to Ask-Mate!")

    logged_menu_dict = {
        "1": "List all questions",
        "2": "Display the questions that were answered",
        "3": "Provide an index to navigate the question and see answers",
        "0": "Log out"
    }

    if register_or_login():
        display_menu(logged_menu_dict)
        logged_in_user_activities()




