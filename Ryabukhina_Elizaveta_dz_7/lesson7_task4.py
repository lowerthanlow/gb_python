import os

dict = {}


def show_stat(folder_path):
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      size = os.stat(os.path.join(root, file)).st_size
      key = 10 ** len(str(size))

      dict[key] = dict.get(key, 0) + 1


my_folder_path = './'
show_stat(my_folder_path)
print(dict)
