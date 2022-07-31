from adislog import adislog
from test_2 import testfunc

def test_func():
    log.debug("I'm called from the function")

log=adislog()

log.warning('This is warning message')
log.fatal(['list','of','items','in','list'])

test_func()
testfunc(log,'Me was called from the function imported from other file')
log.success('SUCCESS')

log.info({"test":"test","test2":"test2"})
