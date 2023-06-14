#!/usr/bin/python3
'''Provides fn to add command line args to list and save them to file'''
sys = __import__('sys')
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list_and_save():
    """
        Add command-line arguments to list and save them to file.

        Returns:
            None
    """
    try:
        items = load_from_json_file("add_item.json")
    except Exception:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    add_items_to_list_and_save()
