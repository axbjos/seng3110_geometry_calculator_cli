import sphere
import cylinder

def main():

    while True:
        print("\nWelcome to the Geometry Program\n")
        print("1. Sphere")
        print("2. Cylinder")
        print("0. Quit")
        selection = int(input("\nPlease enter your selection: "))
        if selection == 1:
            sphere.prompt()
        elif selection == 2:
            cylinder.prompt()
        if selection == 0:
            print("\nProgram Terminating...\n")
            break

if __name__ == '__main__':
    main()