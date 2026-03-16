from handlers.BookHandler import BookHandler
from handlers.ReaderHandler import ReaderHandler
from Library import Library


library = Library("Library", "42nd Avenue")
book_service = BookHandler(library)
reader_service = ReaderHandler(library)

def show_info(msg: str, error: bool = False) -> None:
    color = "\033[31m" if error else "\033[33m"
    reset = "\033[0m"
    print(f"\n{color}{msg}{reset}")


def get_input(name: str, default: bool = True) -> str:
    prompt = f"Provide {name}: "

    if not default:
        return input(prompt).strip().lower()

    while not (user_input := input(prompt).strip().lower()):
        show_info("Empty string, please try again.", error=True)

    return user_input


def display_books(books):
    if not books:
        show_info("No books to display")
        return
    print(f"{'ISBN':<15} {'Title':<30} {'Author':<20} {'Year':<6} {'Available':<10}")
    print("-" * 90)
    for book in books:
        print(f"{book.ISBN:<15} {book.title:<30} {book.author:<20} {book.publication_year:<6} {book.is_available}")


def display_readers(readers):
    if not readers:
        show_info("No readers registered")
        return
    print(f"{'ID':<10} {'First name':<15} {'Last name':<15}")
    print("-" * 45)
    for reader in readers:
        print(f"{reader.reader_id:<10} {reader.first_name:<15} {reader.last_name:<15}")


def add_book():
    title = get_input("title")
    author = get_input("author")
    isbn = get_input("ISBN")
    year = get_input("publication year")
    try:
        book_service.add_book(title, author, isbn, year)
        show_info("Book added")
    except Exception as e:
        show_info(str(e), error=True)


def add_reader():
    first = get_input("first name")
    last = get_input("last name")
    reader_id = get_input("reader id")
    try:
        reader_service.register_reader(first, last, reader_id)
        show_info("Reader registered")
    except Exception as e:
        show_info(str(e), error=True)


def borrow_book():
    reader_id = get_input("reader id")
    isbn = get_input("ISBN")
    try:
        book_service.borrow_book(reader_id, isbn)
        show_info("Book borrowed")
    except Exception as e:
        show_info(str(e), error=True)


def return_book():
    reader_id = get_input("reader id")
    isbn = get_input("ISBN")
    try:
        book_service.return_book(reader_id, isbn)
        show_info("Book returned")
    except Exception as e:
        show_info(str(e), error=True)


def search_books():
    field = get_input("field (title/author/isbn)", default=False) or "title"
    if field not in {"title", "author", "isbn"}:
        show_info("Field must be one of: title, author, isbn", error=True)
        return
    keyword = get_input("keyword")
    try:
        results = book_service.search(keyword, field)
        display_books(results)
    except Exception as e:
        show_info(str(e), error=True)


def show_books_borrowed():
    reader_id = get_input("reader id")
    try:
        loans = reader_service.loans(reader_id)
        display_books(loans)
    except Exception as e:
        show_info(str(e), error=True)


def show_all_books():
    display_books(book_service.list_all())


def show_readers():
    display_readers(reader_service.list_readers())


def main():
    prompt = f"""
    {'*'*20}
    * Choose action:
    * book    - add new book
    * reader  - register new reader
    * borrow  - borrow a book
    * return  - return a book
    * show    - display books borrowed by a reader
    * search  - search books
    * list    - list all books
    * readers - list readers
    * end     - exit
    {'*'*20}
    """

    while (action := input(prompt).strip().lower()) != "end":
        match action:
            case "book": add_book()
            case "reader": add_reader()
            case "borrow": borrow_book()
            case "return": return_book()
            case "show": show_books_borrowed()
            case "search": search_books()
            case "list": show_all_books()
            case "readers": show_readers()
            case other: show_info(f"No action named '{other}'. Try again", error=True)


if __name__ == "__main__":
    main()
