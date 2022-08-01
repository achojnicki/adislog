from ..constants import LOG_LEVELS, LEVEL_FATAL

MSG_FORMAT="{datetime} {filename} {function} {line_number} {log_level} {message}\n"

class file_raw:
    def __init__(self,log_file, **kwargs):
        self._log_file=log_file
        
    def emit(self, message:str, datetime:str, filename:str, function: str, line_number:int, log_level:int):
        with open(self._log_file,'a') as log_file:
            msg=MSG_FORMAT.format(message=message, datetime=datetime, filename=filename, function=function, line_number=line_number, log_level=LOG_LEVELS[log_level])
            
            log_file.write(msg)
        
    
        
