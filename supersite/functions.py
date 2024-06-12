import os
import re

def get_names():
    # save list of log names to 'log_names'
    log_names = os.listdir('logs')
    
    return sorted(log_names)

def get_log_info() -> dict:
    
    dict = {}
    
    for name in get_names():
        #print(name)
        filename = 'logs/' + name
        file = open(filename, 'r')
        content = file.read()
        
        # searchs for 'ID:' in file and creates capture group for digits
        id = re.search("ID\: (\d+)", content)
        if id:
            # ids.append(id.group(1))
            dict[name] = id.group(1)
      
    #print(dict)
    return dict
                
        

def get_content(log_info) -> dict:

    dict = {}
    
    for filename in log_info:
        try:
            path = 'logs/' + str(filename)
            #print("PATH:",path)
            file = open(path,'r')

            dict[filename] = file.read()
    
        except FileNotFoundError:
            print(f"File{filename} not found.")
            continue

    return dict