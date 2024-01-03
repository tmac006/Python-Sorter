import os
import random


def alphabetical_sort(names):
    """Sort names alphabetically."""
    return sorted(names)


def random_groups(names, num_groups, balanced=True):
    """Create random groups from names."""
    random.shuffle(names)
    group_size = len(names) // num_groups
    if not balanced:
        remainder = len(names) % num_groups
        group_size += 1
    groups = [names[i:i + group_size] for i in range(0, len(names), group_size)]
    return groups


def scramble(names):
    """Scramble the order of names."""
    random.shuffle(names)
    return names


def read_names_from_file(filename):
    """Read names from a file and return a list."""
    file_path = os.path.join(os.path.expanduser("~"), "Documents", filename)
    with open(file_path, 'r') as file:
        return [name.strip() for name in file.readlines()]


def write_names_to_file(filename, names):
    """Write sorted names back to the input file."""
    file_path = os.path.join(os.path.expanduser("~"), "Documents", filename)
    with open(file_path, 'w') as file:
        file.write('\n'.join(names))


def main():
    print("Name Sorter By T-Mac")

    input_option = input("Make Things Easier And Read Names From A File? (y/n): ").lower()

    if input_option == 'y':
        input_file = input("Enter The Directory Please: ")
        names = read_names_from_file(input_file)
    else:
        names = input("Enter your names, and separate them with commas: ").split(',')

    # Automatically write sorted names to input file after each operation
    while True:
        print("\nPick Ya Sort Mode:")
        print("1. Alphabetical Sort")
        print("2. Random Groups")
        print("3. Scramble ;)")
        print("4. Exit :'(")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            names = alphabetical_sort(names)
            print("Alphabetical Sort:", ', '.join(names))


        elif choice == '2':
            num_groups = int(input("Enter the number of groups: "))
            balanced = input("Do you want balanced groups? (y/n): ").lower() == 'y'
            groups = random_groups(names, num_groups, balanced)
            for i, group in enumerate(groups, start=1):
                print(f"Group {i}: {', '.join(group)}")
            # Flatten the list of groups and write back to input file
            names = [name for group in groups for name in group]


        elif choice == '3':
            names = scramble(names)
            print("Scrambled Names:", ', '.join(names))


        elif choice == '4':
            print("Ohh Bye Then :(")
            break

        else:
            print("Brotha, Just pick a number between 1-4")


if __name__ == "__main__":
    main()
