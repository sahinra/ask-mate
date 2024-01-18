import data_manager


def display_menu(menu_dict):
    for item in menu_dict.items():
        print(f"{item[0]}- {item[1]}")


if __name__ == "__main__":
    print("Welcome to Ask-Mate!")
    menu_dict = {
        "1": "List all questions",
        "2": "Display the questions that were answered",
        "3": "Provide an index to navigate the question and see answers",
        "0": "Exit"
    }
    display_menu(menu_dict)
    option = int(input("Choose a menu option - "))
    while not option == 0:
        try:
            if option == 1:
                data_manager.get_all_questions()
            elif option == 2:
                data_manager.get_all_questions_with_answers()
            elif option == 3:
                index = int(input("Choose an index - "))
                data_manager.get_question_with_answers(index)
            option = int(input("Choose a menu option - "))
        except ValueError as ex:
            print("Invalid input")
            continue
