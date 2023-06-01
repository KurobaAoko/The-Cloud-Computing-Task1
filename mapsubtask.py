import os
import threading

class MapSubTask(threading.Thread):
    def __init__(self, file, flag):
        threading.Thread.__init__(self)
        self.file = file
        self.flag = flag

    def run(self):
        try:
            with open(self.file, 'r') as f:
                lines = f.readlines()
                map = {}
                for line in lines:
                    passId = line.split(",")[0].strip()
                    if passId not in map:
                        map[passId] = 1
                    else:
                        map[passId] += 1

            output_file = os.path.join('data', 'part', f'part{self.flag}.txt')
            with open(output_file, 'w') as f:
                for key, value in map.items():
                    f.write(f"{key}:{value}\n")
        except Exception as e:
            print(e)

def main():
    folder = 'data/split'
    files = os.listdir(folder)
    threads = []
    flag = 0
    for file in files:
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            thread = MapSubTask(file_path, flag)
            threads.append(thread)
            flag += 1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
