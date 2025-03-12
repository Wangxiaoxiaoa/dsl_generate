import json

def save_file(file_path, content, mode):
    if file_path.endswith('.txt'):
        with open(file_path, mode) as file:
            file.write(content+'\n')
    elif file_path.endswith('.json'):
        with open(file_path, mode) as file:
            json.dump(content, file, ensure_ascii=False)
            file.write('\n')
    else:
        with open(file_path, mode) as file:
            file.write(content)