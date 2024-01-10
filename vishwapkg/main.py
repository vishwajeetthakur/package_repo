# import numpy  as np 
# import pandas as pd 
import os
import os

class Demo:
    def __init__(self) -> None:
        pass

    def make_folder_and_file(self):
        folder_name = 'my_folder'
        file_name = 'my_file.txt'
        # Create the folder if it doesn't already exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Create and open the file in write mode
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            file.write("This is a test file.")

        print(f"Folder '{folder_name}' and file '{file_name}' created successfully.")

obj = Demo()

obj.make_folder_and_file()

        
