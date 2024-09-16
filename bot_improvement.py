def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "enter correct name"
        except ValueError:
            return "write name and phone"
        except IndexError:
            return "enter user name"
    return inner 

def parse_input(user_input):
    cmd, *args = user_input.split()  #разбивает ввод пользователя на отдельные слова. Первое слово сохраняется как команда cmd, а оставшиеся слова сохраняются в список args с помощью оператора *.
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone 
    return f"contact {name} added"

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone 
        return f"contact {name} updated"
    else:
        return f"contact {name} not found"
    
@input_error   
def get_phone(args, contacts):
    name = args[0]
    return contacts.get(name, f"contact{name} not found")

def all_contacts(contacts):
    if contacts:
        return "\n".join(f"{name} {phone} " for name, phone in contacts.items() )
    else:
        return ("no contacts")
        
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("enter command: ")
        command, args = parse_input(user_input)
        
        if command == "close" or command == "exit":
            print("Good bye")
            break 
        elif command == "hello":
            print("how can i help you")
        elif command == "add":
            print(add_contact(args, contacts))            
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("invalid command")
            
if __name__ == "__main__":
    main()           

    