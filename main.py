import books
import users

if __name__ == '__main__':

    books_list = books.read_books(books.csv_file)
    users_list = users.read_users(users.json_file)

    while len(books_list) > 0:
        for user in users_list:
            if len(books_list) == 0:
                break
            else:
                user.books.append(books_list.pop(0))

    users.write_users(users_list, users.result_json_file)
