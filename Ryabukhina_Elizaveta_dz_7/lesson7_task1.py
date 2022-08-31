import os
from pathlib import Path 

dir_=os.path.abspath(os.curdir)

p = Path(f'{dir_}/my_project/settings')

p.mkdir(parents=True, exist_ok=True)

p = Path(f'{dir_}/my_project/mainapp')

p.mkdir(parents=True, exist_ok=True)

p = Path(f'{dir_}/my_project/adminapp')

p.mkdir(parents=True, exist_ok=True)

p = Path(f'{dir_}/my_project/authapp')

p.mkdir(parents=True, exist_ok=True)