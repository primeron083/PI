from userfnc import ask_name
from print_alert import print_alert
if __name__ == "__main__":
 name = ask_name()
 print(name)
 if name == "HACKERMAN":
    print_alert()