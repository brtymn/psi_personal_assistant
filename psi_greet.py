## Greet Function.

import getpass

def Greet():
    get_user_name = getpass.getuser()
    print(".---.| Ψ |'---'")
    print("Hello, {}. My name is Psi. I am a terminal based assitant.".format(get_user_name))
