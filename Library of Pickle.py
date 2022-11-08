import pickle
import os


def load_library(filename):
    if os.path.exists(filename):
        print(f'File Found, opening library -> {filename}')
        with open(filename, 'rb') as binary_fh:  # r reads and b is for binary
            return_library = pickle.load(binary_fh)
    else:
        print('File NOT Found and will be created')
        return_library = []
    return return_library


def save_library(filename, working_library):
    with open(filename, 'wb') as binary_fh:
        pickle.dump(working_library, binary_fh)


def list_books(working_library):
    entry_counter = 1
    print()
    for book in working_library:
        print(f'{entry_counter}:')
        entry_counter += 1
        for key, value in book.items():
            print(f'{key} {value}')


def add_book(working_library, book, author, year_of_release):
    book_dict = {'title': book, 'Author': author, 'year': year_of_release}
    working_library.append(book_dict)


def remove_book(working_library, index_to_remove):
    del working_library[index_to_remove - 1]


def edit_a_book(working_library, book, key_to_update, value):
    working_library[book - 1][key_to_update] = value


def display_options():
    print("1. Add Book")
    print("2. List Books")
    print("3. Remove Book")
    print('4. Edit a book:')
    print("9. Change Library")
    print("0. Exit")
    print('save')
    print('exit without saving')


if __name__ == '__main__':
    while True:
        filename = input('Enter file name: ')
        if filename[-4:] == '.pkl':
            break
    library = load_library(filename)

    while True:
        display_options()

        user_choice = input("Enter Choice: ")
        match user_choice:
            case "1":
                book_name = input("Enter Book Name: ")
                author_name = input("Enter Author's Name: ")
                year = int(input("Enter Book Year: "))
                add_book(library, book_name, author_name, year)

            case "2":
                list_books(library)

            case "3":
                list_books(library)
                book_index = int(input("Enter index of the book to be removed: "))
                remove_book(library, book_index)

            case '4':
                list_books(library)
                book_index = int(input("Enter index of the book to be edited: "))
                key_input = input('Enter what you want to edit(Title,Author,Year): )').lower()
                correction = input('Enter your correction: ')
                if key_input == 'year':
                    correction = int(correction)
                edit_a_book(library, book_index, key_input, correction)
            case '9':
                filename = input('Enter file name: ')
                library = load_library(filename)
            case "0":
                save_library(filename, library)
                break
            case 'save' | 'Save':
                save_library(filename,library)
                continue
            case 'exit without saving':
                break
            case _:
                print("Invalid Choice. Try Again...")
