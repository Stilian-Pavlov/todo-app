FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todo(todo_arg, file_path=FILEPATH):
    with open(file_path, 'w') as file:
        file.writelines(todo_arg)
