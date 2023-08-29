from functions import *
from base_cls import *



command_maps = {
    "hello" : hello,
    ("bye", "close", "exit", "quit") : bye,
    "help": help,
    "add" : add,
    "edit" : edit,
    "delete" : delete,
    ("search", "find") : search,
    "showall" : showall,
    "congratulate" : congratulate,
    "organize": sort.organize_files
}
     

   
def main():
    print("Welcome to Virtual Assistant!")
    contacts = Contacts()
    notes = Notes()
    load_books(filename)

    while True:
        command_list = list(map(lambda x: x if type(x) == str else ", ".join(x), command_maps.keys()))
        command_list = ", ".join(command_list)
        print(f"\n{Colors.HEADER}Available commands: {Colors.UNDERLINE}{command_list}.{Colors.ENDC}")
        command = nick_str(command_item = input("Enter the command: ").lower(), command_items = command_maps.keys())
        if command:
            try:
                print(command_maps[command]())
            except TypeError:
                try:
                    print(f"{Colors.HEADER}Available options: {Colors.UNDERLINE}{', '.join(list(filter(lambda x: available_options[command][x] == True, available_options[command])))}{Colors.ENDC}")
                    items = re.findall(r'[а-яА-Яa-zA-Z]+', input(f"What would you like to {command}?: ").lower())
                    items = nick_str(command = command, command_items = items)
                    for item in items:
                        if item == "note":
                            name = input(f"Enter the {Colors.HEADER}note title{Colors.ENDC}: ").lower()
                            print(command_maps[command]([item], name))
                            items.remove(item)
                        if len(items) < 1:
                            continue
                
                
                        if item == "tags" and item in list(filter(lambda x: available_options[command][x] == True, available_options[command])):
                            name = input(f"Enter the note title of the tags: ").lower()
                            print(command_maps[command](items, name))
                    
                        elif item in list(filter(lambda x: available_options[command][x] == True, available_options[command])):
                            name = input(f"Enter the name of the contact: ").lower()
                            print(command_maps[command](items, name))

                        else:
                            print(f"{Colors.FAIL}{Colors.UNDERLINE}Error: choose from available options.{Colors.ENDC}")

                except KeyError:
                    folder = input("Enter the path of the folder to organize: ")
                    print(command_maps["organize"](folder))
                    continue
                    
            
if __name__ == "__main__":
    main()
