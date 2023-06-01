import os
os.makedirs("data/split/")

def split_file(file_path, chunk_size):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    index = 0
    chunk_index = 0
    while index < len(lines):
        chunk_lines = lines[index:index+chunk_size]

        chunk_file_path = f"data/split/split{chunk_index}.txt"
        with open(chunk_file_path, 'w') as chunk_file:
            chunk_file.writelines(chunk_lines)

        chunk_index += 1
        index += chunk_size

    print("File split completed.")

# 调用示例
split_file("E:/data/AComp_Passenger_data_no_error.csv", 128)
