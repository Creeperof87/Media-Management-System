
def main():
    while True:
        print("| MediaVault |")
        print("1. Movie Manager\n2. Game Library\n3. Exit")
        
        choice = input("\nEnter your choice: ").strip().rstrip(".")
        
        if choice == "1" or choice == "1.":
            #movie_menu()
            pass
        elif choice == "2" or choice == "2.":
            #game_menu()
            pass
        elif choice == "3" or choice == "3.":
            print("Exiting Mediavault...")
            break
        else:
            print("Invalid choice. Please enter either options 1, 2, or 3.\n")

if __name__ == "__main__":
    main()