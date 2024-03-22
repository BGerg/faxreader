import json
import os

def count_non_zero(input_ids):
    return sum(1 for x in input_ids if x != 0)

def count_non_zero_in_jsonl(jsonl_file):
    total_non_zero = 0
    with open(jsonl_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            total_non_zero += count_non_zero(data["input_ids"])
    return total_non_zero

def count_non_zero_in_directory(directory):
    total_non_zero = 0
    for filename in os.listdir(directory):
        if filename.endswith(".jsonl"):
            jsonl_file = os.path.join(directory, filename)
            total_non_zero += count_non_zero_in_jsonl(jsonl_file)
    return total_non_zero

# Example usage:
directory_path = "path/to/your/directory"
total_non_zero = count_non_zero_in_directory(directory_path)
print("Total non-zero elements in input_ids across all JSONL files:", total_non_zero)
