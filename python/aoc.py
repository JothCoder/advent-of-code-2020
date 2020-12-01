from os import path


def get_input(day):
    input_file_path = path.join(path.abspath(path.join(path.dirname(__file__), '..')), 'input', f'day{day:02d}.txt')
    return open(input_file_path, 'r').read()
