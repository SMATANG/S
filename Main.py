from getpass import getpass
import os
import time
def menu():
      while True:
           try:
                print("═══════════════════════╗")
                x = str(input('\033[1;92m • [ SJH2130] >  \033[1;93m:                  >
                e = getpass('\033[1;92m • [Password] >  \033[1;93m: ')
                print("═══════════════════════╝")
                if x=="S" and e=="0":
                   print("═══════════════════════╗")
                   print('      Welcome sir')
                   print("═══════════════════════╝")
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      print("")
           except Exception:

                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
menu()
