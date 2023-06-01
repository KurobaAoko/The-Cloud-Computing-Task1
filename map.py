import os
import concurrent.futures

class MapSubTask:
    def __init__(self, file, flag):
        self.file = file
        self.flag = flag

    def run(self):
        # 在这里实现 map 过程的逻辑
        # 可以使用 self.file 进行文件处理
        # 可以使用 self.flag 进行标记或其他操作
        pass

def main():
    executor = concurrent.futures.ThreadPoolExecutor()

    # 获取文件列表
    folder = "data/split"
    files = os.listdir(folder)

    # 创建多线程对象
    flag = 0
    for filename in files:
        filepath = os.path.join(folder, filename)
        # 为每个文件启动一个线程
        map_task = MapSubTask(filepath, flag)
        executor.submit(map_task.run)
        flag += 1

    executor.shutdown()

if __name__ == "__main__":
    main()

