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
          Exit  : Exit Or [Ctrl ^ c]

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


def edit_stuff():
    
    if not stock:
        print("There is not anything in stock")

    else :
        print(""" 
              [1]  : for Editing Stuff's code
              [2]  : for Editing Stuff's name or existence 
              Done : Exit editing
              Show : Show Stock List
          """)

        while (user_input := input("choose [1 Or 2] to Edit : ")) != "Done":

            # Edit Stuff's Code
            if user_input == "1":

                print("Editing Stuff's Code! ")
                code1 = input("previous Code? : ")
                code2 = input("New Code? : ")

                stock[code2] = stock[code1]
                del stock[code1]

            # Edit Stuff's Name or existence
            elif user_input == "2":

                print("Editing Stuff's Name or existence! ")
                code = input("Stuff's Code? : ")
                name = input("Stuff's New Name ? : ")
                existence = input("Stuff's New Existence : ")

                stock[code]["Name"] = name
                stock[code]["Exist"] = existence

            elif user_input == "Show":
                show_all_stuffs()


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
        elif user_input == "Edt":
            edit_stuff()


if __name__ == "__main__":
    try:
        _main()

    except KeyboardInterrupt:
        print("\nHave a good Day. Bye!\n")
