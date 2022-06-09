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
        stock[code] = {"Name": name, "Exist": existence}
        print()


def show_all_stuffs():
    """Showing all Stuffs list"""

    if not stock:
        print("There is not anything in stock")
    else:
        print("--------------------------")
        for code in stock:
            print(f"Code ... ...{code}")
            for key, val in stock.get(code).items():
                print(f"{key} ... ... {val}")
            print("--------------------------")


def show_one_stuff():
    """Showing a specific stuff in list by its code """

    if not stock:
        print("There is not anything in stock")
    else:
        print()
        code = input("Stuff's code ?  :  ")
        show = stock.get(code, "it is not in list")
        print(f"\nCode .... ...{code}")
        for key, val in show.items():
            print(f"{key} .... ... {val}")


def edit_stufff():
    pass


def del_stuff():
    """delete stuff from list"""

    code = input(
        """which stuff you want to delete ?\n[type "Show" for what is in list]\ncode: """)
    if code == "Show":
        show_all_stuffs()
    else:
        if not stock:
            print("There is not anything in stock")
        else:
            if code in stock:
                del stock[code]
                print(f"\nstuff with {code = } deleted Successfully! \n")
            else:
                print(f"\nstuff with {code = } is not in list\n")


def _main():
    """main program to interact with User"""
    user = "Command [H for Help] : "
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
        elif user_input == "Del":
            del_stuff()


if __name__ == "__main__":
    _main()
    print("\nHave a good Day. Bye!\n")
