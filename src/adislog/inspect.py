from lib2to3 import fixer_base, refactor
from inspect import stack

import pprint

class scraper(fixer_base.BaseFix):
    PATTERN="simple_stmt"
    
    def __init__(self,line_number:int):
        super().__init__(None,None)
        
        self.lineno = line_number
        self.statement = ""
        
    def transform(self,n,r):
        if not self.statement and len(str(n).split("\n")) > self.lineno - n.get_lineno():
            prev = str(n.prev_sibling)
            if prev == ' ':
                self.statement += prev.lstrip('\n')
                
            self.statement +=str(n)
        return n
    
class get_function_by_line(refactor.RefactoringTool):
    def __init__(self,s:str , l:int):
        self.source=s
        self.scraper=scraper(l)
        
        super().__init__(None)
    
    def get_fixers(self):
        return [[self.scraper], []]

    def __str__(self):
        self.refactor_string(self.source,'')
        return self.scraper.statement
    

class inspect:
    def __init__(self, privacy:bool, use_code_context:bool):
        self._privacy=privacy
        self._use_code_context=use_code_context
    
    def _clear(self,data):
        data=bytearray(data, 'utf-8')
        while 1:
            if data[0] == ord(' ') or data[0] == ord('\t') or data[0]==ord("\n"):
                del data[0]
            else:
                break
        if data[-1] == ord("\n"):
            del data[-1]
            
        data=data.decode('utf-8')
        data.replace('\n','<newline>')
        return data
        
    def get_caller(self):
        i=stack()[3]
        resp={"filename":i.filename,
              "function": i.function if self._privacy else self._clear(i.code_context[0] if self._use_code_context else str(get_function_by_line(open(i.frame.f_code.co_filename).read(),i.frame.f_lineno))),
              "line_number":i.lineno}
        return resp
