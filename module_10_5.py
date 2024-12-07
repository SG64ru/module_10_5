from multiprocessing import Pool
import time



def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)



filenames = [f'./file {number}.txt' for number in range(1, 5)]

"""Линейный вызов"""
start = time.time()
for name in filenames:
    read_info(name)
end = time.time()
time = end - start
print(f'Линейный вызов: {time}')

"""Многопроцессный вызов"""
# if __name__ == '__main__':
#
#     with Pool(processes=4) as pool:
#         start = time.time()
#         pool.map(read_info, filenames)
#         end = time.time()
#         time = end - start
#         print(f'Многопроцессный вызов: {time} processing')
