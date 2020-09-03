## Greet Function.

import getpass

get_user_name = getpass.getuser()


def Greet():
    print(".---.| Ψ |'---'")
    print("Greetings, {}. How can I help?".format(get_user_name))


Greet()
