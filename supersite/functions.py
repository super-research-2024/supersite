import os

def get_names():
    # save list of log names to 'log_names'
    log_names = os.listdir('logs')
    
    return log_names

def get_logs():
    
    logs = []
    
    for name in get_names():
        filename = 'logs/' + name
        # return file contents
        file = open(filename, 'r')
        logs.append(file.read())
    
    logs.reverse()
    return logs

