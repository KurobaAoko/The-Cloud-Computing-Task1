import os
import operator


def main():
    map = {}
    folder = "data/part"
    files = os.listdir(folder)

    for filename in files:
        file_path = os.path.join(folder, filename)  # 构建完整的文件路径
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()  # 移除行首尾的空白字符
                passId, sum = line.split(":")
                sum = int(sum)
                if passId not in map:
                    map[passId] = sum
                else:
                    map[passId] += sum

    sorted_map = sorted(map.items(), key=operator.itemgetter(1), reverse=True)

    for item in sorted_map:
        print(f"{item[0]}:{item[1]}")


if __name__ == "__main__":
    main()
