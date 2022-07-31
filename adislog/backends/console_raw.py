from ..constants import LOG_LEVELS

from sys import stdout, stderr
MSG_FORMAT="{datetime} {filename} {function} {line_number} {log_level} {message}\n"

class console_raw:
    def __init__(self):
        self._stderr=stderr
        self._stdout=stdout
    
    def validate(self, **kwargs):
        pass
    
    def emit(self, message:str, datetime:str, filename:str, function: str, line_number:int, log_level:int):
        
        msg=MSG_FORMAT.format(message=message, datetime=datetime, filename=filename, function=function, line_number=line_number, log_level=LOG_LEVELS[log_level])
        
        if log_level==LEVEL_FATAL:
            self._stderr.write(msg)
            self._stderr.flush()
        else:
            self._stdout.write(msg)
            self._stdout.flush()
