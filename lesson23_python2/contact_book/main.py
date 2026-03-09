from ContactHandler import ContactHandler

handler = ContactHandler.initialize()
contact_data = ["first_name", "last_name", "email", "mobile"]

def show_info(msg: str, error: bool = False) -> None:
    COLOR = "\033[31m" if error else "\033[33m"
    RESET = "\033[0m"
    print(f"\n{COLOR}{msg}{RESET}")


def get_input(name: str, default: bool = True) -> str:
    prompt = f"Provide {name} of this contact: "

    if not default:
        return input(prompt).strip().lower()

    while not (user_input := input(prompt).strip().lower()):
        show_info("Empty string, please try again.\n")

    return user_input


def display_table(contacts: list[object]) -> None:
    if not contacts:
        show_info("No contacts found.")
        return

    headers = ["id", *contact_data]
    widths = [3, 20, 20, 25, 15]
    line = " | ".join(f"{{:<{width}}}" for width in widths)

    print(line.format(*headers))
    print("-" * (sum(widths) + 3 * (len(widths) - 1)))
    for contact in contacts:
        print(line.format(getattr(contact, "id", ""), *(getattr(contact, field, "") for field in contact_data)))


def add_contact() -> None:
    input_data = {data: get_input(data) for data in contact_data}

    try:
        new_contact = handler.add(*input_data.values())
        display_table([new_contact])
    except Exception as e:
        show_info(f"{e.capitalize}. Action aborted.", error=True)

def show_contacts():
    contacts = handler.get_all()

    display_table(contacts)

def get_contact_by_id_from_input():
    try:
        contact_id = int(get_input("contact id"))
    except ValueError:
        show_info("Id must be a number.", error=True)
        return None

    contact = handler.get_by_id(contact_id)
    if contact is None:
        show_info(f"No contact with id {contact_id}", error=True)
        return None
    return contact


def remove_contact() -> None:
    show_contacts()
    if handler.isEmpty(): return

    contact = get_contact_by_id_from_input()
    if contact is None:
        return

    show_info("Selected contact:")
    display_table([contact])
    if get_input("confirmation (y/n)") != "y":
        show_info("Cancelled.")
        return

    handler.remove(contact.id)
    show_info(f"Contact {contact.id} removed.")


def edit_contact() -> None:
    show_contacts()
    if handler.isEmpty(): return

    contact = get_contact_by_id_from_input()
    if contact is None:
        return

    print("Selected contact:")
    display_table([contact])
    if get_input("confirmation (y/n)") != "y":
        show_info("Cancelled.")
        return

    changes = {}
    for field in contact_data:
        value = get_input(f"new {field} (leave empty to keep current)", default=False)
        if value:
            changes[field] = value

    if not changes:
        show_info("No changes provided.")
        return

    try:
        handler.edit(contact.id, **changes)
        show_info(f"Contact {contact.id} updated.")
        display_table([handler.get_by_id(contact.id)])
    except Exception as e:
        show_info(f"{e.capitalize}. Action aborted.", error=True)


def search_contacts() -> None:
    if handler.isEmpty(): 
        show_info("No contacts found")
        return
    
    fields = ", ".join(contact_data)
    field = get_input(f"search column ({fields})")
    if field not in contact_data:
        show_info(f"Column must be one of: {fields}.", error=True)
        return

    value = get_input(field)
    if not value:
        show_info("Search value cannot be empty.", error=True)
        return

    found = handler.search_by_attribute(field, value)
    display_table(found)


def main() -> None:
    try:
        handler.load()
        show_info("Existing contacts loaded from the file.")
    except FileNotFoundError:
        show_info("Initiated an empty contact book")


    prompt = f"""
    {'*'*20}
    * Choose action:
    * add - add a new contact
    * remove - remove existing contact
    * edit - edit existing contact
    * show - displey all contacts
    * search - display by specific search criteria
    * end - close the contacts book
    {'*'*20}
    """
    while (action := input(prompt).strip().lower()) != "end":
        match action:
            case "add": add_contact()
            case "show": show_contacts()
            case "remove": remove_contact()
            case "edit": edit_contact()
            case "search": search_contacts()
            case other: show_info(f"No action named '{other}'. Try again")

    try:
        handler.save()
    except:
        pass


if __name__ == "__main__":
    main()
