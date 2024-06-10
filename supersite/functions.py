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
      
    print(dict)      
    return dict
                
        

def get_content(name):
    # get all log names and ids
    # dict = get_log_info()
    # ids = list(dict.values())
    
    # # get log with the id pased in
    # name = ids.index(id)
    filename = 'logs/' + name
    print(filename)
    file = open(filename, 'r')
    
    # return log contents
    return file.read()