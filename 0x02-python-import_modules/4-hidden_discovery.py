#!/usr/bin/python3

if __name__ == '__main__':
    """
        Prints all names defined by hidden_4
    """
    import inspect
    import hidden_4
    
    for name, obj in inspect.getmembers(hidden_4):
        if not name.startswith("__") and not inspect.ismodule(obj):
            print(name)
