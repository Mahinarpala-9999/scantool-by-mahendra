

import conf.conf as conf


def print_banner():
    """
    Prints the banner with tool name, creator, and version.
    """
    print("===================================================================")
    print(conf.colored(conf.text2art("Scan Tool", "larry3d"), "cyan"))
    print(conf.colored("[>]", "red", attrs=["bold"]) +
          conf.colored("Created by : Mahendra\n", "magenta", attrs=["bold"]))
    print(conf.colored("[>]", "red", attrs=["bold"]) +
          conf.colored(f"Version : {conf.version}\n", "magenta", attrs=["bold"]))
    conf.ver_check()
    print("===================================================================")


def print_menu():
    """
    Prints the main menu options for the user.
    """
    print(conf.colored("\n1. Nmap Scan", "yellow", attrs=["bold"]))
    print(conf.colored("2. Dirsearch Scan", "yellow", attrs=["bold"]))
    print(conf.colored("3. Nikto Scan", "yellow", attrs=["bold"]))
    print(conf.colored("A. All the Scans", "yellow", attrs=["bold"]))
    print(conf.colored("E. Exit\n", "yellow", attrs=["bold"]))
    print("===================================================================")


def get_user_choice():
    """
    Prompts the user to select an action from the menu.
    """
    return input(conf.colored("\nWhat would you like to do? Enter your selection: ", "green")).upper()


def handle_user_choice(choice):
    """
    Handles the user's input by calling the appropriate function.
    """
    if choice == "1":
        conf.call_def(conf.nmap_scan)
    elif choice == "2":
        conf.call_def(conf.dirsearch_scan)
    elif choice == "3":
        conf.call_def(conf.nikto_scan)
    elif choice == "A":
        conf.call_def(conf.full_scan)
    elif choice == "E":
        conf.call_def(conf.exit)
    else:
        conf.not_valid(main, choice, 0)


def main():
    """
    The main function that runs the loop for user interaction.
    """
    while conf.ans:
        print_banner()
        print_menu()
        conf.ans = get_user_choice()
        handle_user_choice(conf.ans)


try:
    main()
except KeyboardInterrupt:
    print("\n \n Keyboard Interrupt. Exiting...")
    conf.sys.exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    conf.sys.exit()

