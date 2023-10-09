import os
import glob

def manage_static_folder(static_folder, max_files=80):    
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)
    
    files = glob.glob(os.path.join(static_folder, "*"))
    
    if len(files) > max_files:        
        files.sort(key=os.path.getmtime)       
        num_files_to_delete = len(files) - max_files

        for i in range(num_files_to_delete):
            os.remove(files[i])
        
        print('Excluindo arquivos ...')    
    
    return glob.glob(os.path.join(static_folder, "*"))