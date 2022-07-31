import inspect

def get_caller():
    i=inspect.stack()[3]
    resp={"filename":i.filename, "function": i.function, "line_number":i.lineno}
    return resp

