from .methods import adislog_methods 
from .inspect import get_caller
from .backends import console_raw, console_fancy

from pprint import pformat
from time import strftime

class adislog(adislog_methods):
    def __init__(self, timeformat=None, backends=['console_fancy'], **kwargs):
        self._backends=[]
        self._timeformat="%H:%M:%S %d:%m:%Y" if timeformat is None else timeformat
        
        for a in backends:
            if a == 'console_raw':
                o=console_raw.console_raw()
                self._backends.append(o)
                
            elif a == 'console_fancy':
                o=console_fancy.console_fancy()
                self._backends.append(o)
        
    def _message(self,log_level:int, log_item):
        if type(log_item) is str:
            message=log_item
        
        elif type(log_item) is tuple or type(log_item) is list:
            message="\n"+pformat(log_item)
            
        elif type(log_item) is dict:
            message="\n"+pformat(log_item)
            
        time=strftime(self._timeformat)
        caller_info=get_caller()
        msg={"log_level":log_level, "message":message, "datetime":time, **caller_info}
        
        for backend in self._backends:
            backend.emit(**msg)

    
    
