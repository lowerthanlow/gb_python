import os
import shutil

my_dir = './my_project'

files = [os.path.relpath(os.path.join(root, file), my_dir) for root, dirs, files in os.walk(my_dir) for file in files if file.endswith(".html")]


for rel_path in files:
   test_path = os.path.join(my_dir, 'templates')
  
   if not os.path.exists(test_path):
     os.mkdir(test_path)
     
   found_dir = os.path.split(rel_path)[1]
   curr_path = os.path.join(test_path, found_dir)
  
   if not os.path.exists(curr_path):
     os.mkdir(curr_path)
     
   for file in files: 
    if not os.path.exists(os.path.join(curr_path, file)):
      shutil.copy2(os.path.join(my_dir, file), curr_path) 

