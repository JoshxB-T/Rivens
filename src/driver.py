import objecttier
import sqlite3

def print_menu():
    print()
    print("Select a menu option:")
    print("1.  Convert .json to .db")
    print("or x to exit the program.")
    print()

def convertFile():
    print("Converting .json to .db")

def main():
    print("Rivens Driver Application (N-Tier)")
    print()

    dbName = input("Enter the database name: ")
    dbConn = sqlite3.connect(dbName) # FIXME: Adjust to look in the data directory

    print("Database connection established.")
    print_menu()
    cmd = input("Your choice --> ")

    while cmd != 'x':
        if cmd == '1':
            convertFile()
        else:
            print("Invalid option. Please try again.")
        print_menu()
        cmd = input("Your choice --> ")
        print()

    dbConn.close()
    print("Database connection closed.")
    print("Exiting the program.")

# Check if this script is being run directly
if __name__ == '__main__':
    main()
