FILEPATH = "todo_item.txt"

def get_todos(filepath = FILEPATH):
    """
    param filepath: Path for read file ,
    return: list of items
    """
    with open(filepath, "r") as file:
        todo = file.readlines()
        return todo


def write_todos (todo_arg, filepath = FILEPATH):
    """
    param todo_arg: items that want to add
    param filepath:  path for write file,
    return: void
    """
    with open(filepath, "w") as file:
        file.writelines(todo_arg)
