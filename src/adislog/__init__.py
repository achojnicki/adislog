"""Simple log with function of logging the caller function with arguments and colorful output"""

from .methods import adislog_methods 
from .inspect import inspect
from .process import get_process_details
from .backends import terminal, terminal_colorful, terminal_table, file_plain, rabbitmq_emiter
from .traceback import parse_frame
from .exceptions import EXCEPTION_BACKEND_DO_NOT_EXISTS

from pprint import pformat
from time import strftime

import sys
import traceback
#import IPython

class adislog(adislog_methods):
    def __init__(self,
                 time_format=None,
                 log_file:str=None,
                 privacy:bool=True,
                 debug:bool=False,
                 init_message:str="adislog module initializated.",
                 replace_except_hook:bool=True,
                 backends:list or array=['file_plain','terminal_table'],
                 rabbitmq_host=None,
                 rabbitmq_port=None,
                 rabbitmq_credentials=None,
                 rabbitmq_queue='logs',
                 **kwargs):
        """Time format have to be format of the time.strftime function.
log_file:str                 - Specify the path of the log file,
privacy:bool                 - Set to true log the caller of the function with the arguments. Name of the function otherwise.
debug:bool                   - Sets the condition to store the debug messages or not.
init_message:str             - Message showed after initialisation of the adislog,
backends:list or array       - List is a list with enabled backends. Backends:
    file_plain        - Saves the log to the spewcified file as a plain text.
    terminal          - Prints the log to the console with no formatting.
    terminal_colorful - Same as above - additionally colores the output.
    terminal_table    - Show tabulated log on the console - never be confused by log again.

Note that all of the console backends writes the fatal messages to the STDERR pipe.
"""
        self._backends=[]
        self._time_format="%a %d:%b:%Y %H:%M:%S" if time_format is None else time_format
        self._log_file='log.log' if log_file is None else log_file
        self._privacy=privacy
        self._debug=debug
        self._init_message=init_message
        self._replace_except_hook=replace_except_hook
        
        self._exception_data=[]
        
        self._inspect=inspect(privacy=self._privacy)
        
        
        
        for a in backends:
            o=None        
            
            if a == 'terminal':
                o=terminal.terminal()
                
            elif a == 'terminal_colorful':
                o=terminal_colorful.terminal_colorful()
                
            elif a == 'terminal_table':
                o=terminal_table.terminal_table()
                
            elif a == 'file_plain':
                o=file_plain.file_plain(log_file=self._log_file)
            
            elif a == 'rabbitmq_emitter':
                o=rabbitmq_emiter.rabbitmq_emiter(
                    rabbitmq_host=rabbitmq_host,
                    rabbitmq_port=rabbitmq_port,
                    rabbitmq_credentials=rabbitmq_credentials,
                    rabbitmq_queue=rabbitmq_queue
                    )
            
            
            else:
                raise EXCEPTION_BACKEND_DO_NOT_EXISTS
            
            if o:
                self._backends.append(o)
            
        if self._replace_except_hook:
            sys.excepthook=self._except
            
        self._init_msg()
        
    def _init_msg(self):
        self.info(self._init_message)
        
    def _message(self,log_level:int, log_item):
        if log_level >0 or self._debug: 
            if type(log_item) is str:
                message=log_item
            
            #TODO move the formatting of the text to the backends
            elif type(log_item) is tuple or type(log_item) is list:
                message=pformat(log_item)
                
            elif type(log_item) is dict:
                message=pformat(log_item)
            
            elif type(log_item) is int:
                message=log_item
                
            elif type(log_item) is bytes or type(log_item) is bytearray:
                message=log_item.decode('utf-8')
            else:
                message=str(log_item) 
            #end TODO
            
            time=strftime(self._time_format)
            caller_info=self._inspect.get_caller()
            process_details=get_process_details()
                            
            msg={"log_level":log_level,
                 "message":message, 
                 "datetime":time, 
                 **caller_info, 
                 **process_details}
            
            if self._exception_data:
                msg['excpt_data']=[parse_frame(a) for a in self._exception_data] 
                
            
            for backend in self._backends:
                backend.emit(**msg)

    def _parse_tb(self, tb):
        self._exception_data.append(tb.tb_frame)

    def _except(self, etype,value, tb):
        #TODO: use the value: traceback.format_exception(value)

        while True:
            self._parse_tb(tb)
            if tb.tb_next:
                tb=tb.tb_next
            else:
                break
            
        self.fatal("Exception %s occured!" % value)
        sys.exit(1)
        
