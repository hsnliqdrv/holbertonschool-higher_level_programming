#!/usr/bin/python3
"""7-add_item

This script adds all arguments to a list
and saves to a file
"""
if __name__ == "__main__":
    from sys import argv
    save_fun = __import__('5-save_to_json_file').save_to_json_file
    load_fun = __import__('6-load_from_json_file').load_from_json_file
    filename = "add_item.json"
    try:
        initial = load_fun(filename)
    except FileNotFoundError:
        initial = []
    finally:
        save_fun(initial + argv[1:], filename)
