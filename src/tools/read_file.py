import json
from datasets import load_dataset

def read_file(file_path):
    if file_path.endswith('.json'):
        try:
            return load_dataset("json", data_files=file_path, split='train')
        except Exception as e:
            with open(file_path, 'r') as file:
                return json.load(file)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        with open(file_path, 'r') as file:
            return file.read()
        

def read_stage1_output(file_path):
    skeleton_sentence = list()
    with open(file_path, 'r') as file:
        for line in file:
            skeleton_sentence.append(line.strip())
    return skeleton_sentence

def read_stage2_output(file_path):
    complete_sentence = list()
    with open(file_path, 'r') as file:
        for line in file:
            complete_sentence.append(line.strip())
    return complete_sentence