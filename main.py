import os
from helper_func import *

if __name__ == "__main__":
    os.system("clear")
    graph, people_data = None, None

    print(
        "Welcome to Graph maker!\n" +
        "To Start making, you want to...\n" +
        "1. Create a new one\n" +
        "2. Load from existed data(json)\n"
    )
    command = input("Your command: ")

    if command == '1':
        graph = graph_init()
        set_graph_attribute(graph)
        people_data = dict({})

    elif command == '2':
        people_data = read_existing_data()
        graph = draw_graph_from_existing_data(people_data)

    while True:
        os.system("clear")
        print(
            "1: New Person\n" +
            "2: Set person attribute\n" +
            "3: Check person attribute\n" +
            "4: Delete Person\n" +
            "5: Set relation\n" +
            "6: Check relation\n" +
            "7: Edit relation\n" +
            "8: Delete relation\n" +
            "9: Export data\n" +
            "0: Export graph\n" +
            "Quit: Quit and save a file"
              )

        command = input("Your command: ")
        if command == "Quit":
            os.system("clear")
            break

        os.system("clear")
        if command == "1":
            graph, people_data = new_person(graph, people_data)

        elif command == "2":
            people_data = set_person_attribute(people_data)

        elif command == "3":
            check_person_attribute(people_data)

        elif command == "4":
            graph, people_data = delete_person(graph, people_data)

        elif command == "5":
            graph, people_data = set_relation(graph, people_data)

        elif command == "6":
            print(check_relation(graph, people_data))

        elif command == "7":
            graph, people_data = edit_relation(graph, people_data)

        elif command == "8":
            graph, people_data = delete_relation(graph, people_data)

        elif command == "9":
            export_data(people_data)

        elif command == "0":
            export_graph(graph)

        print("Done!")
        empty = input("Press Enter to continue")

    for person, attr in people_data.items():
        print(f"{person}: {attr}")
