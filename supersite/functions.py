import os
import re

def get_names():
    # save list of log names to 'log_names'
    log_names = os.listdir('logs')
    
    return sorted(log_names)

def get_log_info():
    
    dict = {}
    
    for name in get_names():
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
                
        

def get_content(name):
    try:
        filename = 'logs/' + str(name)
        print(filename)
        file = open(filename, 'r')
    
        # return log contents
        return file.read()
    
    except FileNotFoundError:
        print(f"File{name} not found.")
        return None