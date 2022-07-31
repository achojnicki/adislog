from ..constants import LOG_LEVELS, LEVEL_FATAL

from colored import stylize, fg, bg, attr
from sys import stdout, stderr

MSG_FORMAT="{datetime} {filename} {function} {line_number} {log_level} {message}\n"
COLORS=[fg(248),fg(255),fg(227),fg(9),fg(10)]

class console_fancy:
    def __init__(self):
        self._stderr=stderr
        self._stdout=stdout
    
    def validate(self, **kwargs):
        pass
    
    def emit(self, message:str, datetime:str, filename:str, function: str, line_number:int, log_level:int ):
        msg_data={
        "datetime":stylize(datetime,COLORS[log_level]),
        "filename":stylize(filename,COLORS[log_level]),
        "function":stylize(function,COLORS[log_level]),
        "line_number":stylize(str(line_number),COLORS[log_level]),
        "log_level":stylize(LOG_LEVELS[log_level],COLORS[log_level]+attr('bold')),
        "message":stylize(message,COLORS[log_level])}
        
        msg=MSG_FORMAT.format(**msg_data)
        
        if log_level==LEVEL_FATAL:
            self._stderr.write(msg)
            self._stderr.flush()
        else:
            self._stdout.write(msg)
            self._stdout.flush()
            
