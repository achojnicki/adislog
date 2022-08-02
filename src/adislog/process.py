from os import getpid, getppid, getcwd, getuid

def get_process_details():
    return {'pid':getpid(), 'ppid':getppid(), 'cwd': getcwd(), 'uid': getuid()}
