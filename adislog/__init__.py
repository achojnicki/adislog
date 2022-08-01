from .methods import adislog_methods 
from .inspect import get_caller
from .backends import console_raw, console_fancy, file_raw

from pprint import pformat
from time import strftime

class adislog(adislog_methods):
    def __init__(self, time_format=None, log_file=None, backends=['file_raw','console_fancy'], **kwargs):
        self._backends=[]
        self._time_format="%H:%M:%S %d:%m:%Y" if time_format is None else time_format
        self._log_file='log.log' if log_file is None else log_file
        
        for a in backends:
            if a == 'console_raw':
                o=console_raw.console_raw()
                
            elif a == 'console_fancy':
                o=console_fancy.console_fancy()
            
            elif a == 'file_raw':
                o=file_raw.file_raw(log_file=self._log_file)
            
            self._backends.append(o)
        
    def _message(self,log_level:int, log_item):
        if type(log_item) is str:
            message=log_item
        
        elif type(log_item) is tuple or type(log_item) is list:
            message="\n"+pformat(log_item)
            
        elif type(log_item) is dict:
            message="\n"+pformat(log_item)
            
        time=strftime(self._time_format)
        caller_info=get_caller()
        msg={"log_level":log_level, "message":message, "datetime":time, **caller_info}
        
        for backend in self._backends:
            backend.emit(**msg)

    
    
