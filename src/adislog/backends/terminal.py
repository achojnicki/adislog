from ..constants import MSG_FORMAT,LOG_LEVELS

from sys import stdout, stderr

class terminal:
    def __init__(self):
        self._stderr=stderr
        self._stdout=stdout
    
    def emit(self,
             message:str,
             datetime:str,
             filename:str,
             function: str,
             line_number:int,
             log_level:int,
             pid:int,
             ppid:int,
             cwd:str,
             uid:int):
        
        msg=MSG_FORMAT.format(message=message,
                              datetime=datetime,
                              filename=filename,
                              function=function,
                              line_number=line_number,
                              log_level=LOG_LEVELS[log_level],
                              pid=pid,
                              ppid=ppid,
                              cwd=cwd,
                              uid=uid)
        
        print(msg,file=self._stdout if log_level!=LEVEL_FATAL and log_level!=LEVEL_ERROR else self._stderr)

