import random
def alphabetical_sort(names):
    return sorted(names)
#2nd ever python project, and Im just now learning how to comment

#How random Groups are made, uses shuffle and determines how many groups and group size by asking the user
def random_groups(names, num_groups):
    random.shuffle(names)
    group_size = len(names) // num_groups
    groups = [names[i:i + group_size] for i in range(0, len(names), group_size)]
    return groups
#Scramble was my fun idea for this application, of course it was the easiest to make
def scramble(names):
    random.shuffle(names)
    return names

def main():
    print("Name Sorter By T-Mac")

    names = input("Enter your names, and seperate them with comas ").split(',')

    while True:
        print("\nPick Ya Sort Mode:")
        print("1. Alphabetical Sort")
        print("2. Random Groups")
        print("3. Scramble ;)")
        print("4. Exit :'(")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sorted_names = alphabetical_sort(names)
            print("Alphabetical Sort:", ', '.join(sorted_names))

        elif choice == '2':
            num_groups = int(input("Enter the number of groups: "))
            groups = random_groups(names, num_groups)
            for i, group in enumerate(groups, start=1):
                print(f"Group {i}: {', '.join(group)}")

        elif choice == '3':
            scrambled_names = scramble(names)
            print("Scrambled Names:", ', '.join(scrambled_names))
        #exiting :(
        elif choice == '4':
            print("Ohh Bye Then :(")
            break
        #just incase people mess up
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
#doing some fun checking
if __name__ == "__main__":
    main()
