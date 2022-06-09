"""This is a Stock List Program"""
stock = {}


def _help():
    """This is Help Menu"""
    print("""
          H     : Show this Menu
          New   : Add New stuff
          Del   : Delete stuff
          Edt   : Edit stuff
          Info  : Info about one stuff
          Show  : Show all stuffs
          Exit  : Exit

          *** Notice! Sensitive to Lower or Upper Case Letters ***

          """)


def new_stuff():
    """Adding new stuff to list"""

    print("\n[Type \"Done\" to exit]\n")
    while (code := input("stuff's code : ")) != "Done":

        name = input("stuff's name : ")
        existence = input("stuff's existence : ")
        stock[code] = {"name": name, "exist": existence}
        print()


def show_all_stuffs():
    """Showing all Stuffs list"""

    print()
    if not stock:
        print("\nNothing in Stock")
    else:
        for code in stock:
            print(f"{code = }")
            for key, val in stock.get(code).items():
                print(f"{key} ... ... {val}")
            print("--------------------------")


def show_one_stuff():
    """Showing a specific stuff in list by its code """

    if not stock:
        print("Nothing in Stock")
    else:
        print()
        code = input("Stuff's code : ")
        show = stock.get(code, "it is not in list")
        print(f"\n{code = }")
        for key, val in show.items():
            print(f"{key} .... ... {val}")


def edit_stufff():
    pass


def main_program():
    """main program to interact with User"""
    user = "Command me according to Menu ? [H for Help] : "
    print()
    while (user_input := input(user)) != "Exit":

        if user_input == "New":
            new_stuff()
        elif user_input == "Show":
            show_all_stuffs()
        elif user_input == "Info":
            show_one_stuff()
        elif user_input == "H":
            _help()


if __name__ == "__main__":
    main_program()
    print("\nHave a good Day. Bye!\n")
