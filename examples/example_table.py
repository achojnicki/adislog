from adislog import adislog
from func_from_ext_file import examplefunc

def example_func():
    log.debug("I'm called from the function")

log=adislog(privacy=False, debug=True)

log.warning('This is warning message')
log.fatal(['list','of','items','in','list'])

example_func()
examplefunc(log,'Me was called from the function imported from other file')
log.success('SUCCESS')

log.warning("""test
test
test""")

log.info({"example":"example","example2":"example2"})
log.success("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sodales ligula rhoncus, finibus justo ut, condimentum ex. Nam ac lacus consequat, pulvinar eros ac, sodales diam. Donec sodales ante ut facilisis interdum. Praesent condimentum egestas dolor, id blandit purus suscipit vel. Ut non quam at leo ornare auctor non a mi. Fusce ut massa urna. Proin eget nunc mollis, molestie urna quis, fringilla erat. Sed scelerisque tincidunt risus vel placerat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin elementum sollicitudin eros eget convallis.

Morbi felis sapien, pulvinar vitae pretium eget, sodales at neque. Aliquam orci elit, vestibulum et ligula id, cursus malesuada lorem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In felis lectus, sollicitudin quis iaculis eget, tincidunt vel ligula. Nunc consectetur nunc et nisl volutpat sollicitudin. In et elementum ligula, a fringilla justo. Mauris accumsan eleifend nisi, ac sollicitudin nisl facilisis tristique. Etiam tincidunt purus eu sapien posuere, sed maximus massa maximus. Aliquam erat volutpat. Vivamus vitae lobortis nisi.

Sed viverra, libero in dignissim imperdiet, mi nulla gravida sem, et bibendum nulla lorem et tortor. Aenean dictum sed ante vel semper. Pellentesque consequat felis vel rutrum efficitur. Nunc pellentesque sollicitudin mauris sit amet facilisis. Integer sed dolor eget neque fringilla rutrum. Suspendisse mattis ullamcorper eros id aliquet. Ut lobortis arcu in laoreet ornare. Curabitur scelerisque blandit massa, vitae maximus lectus congue ut. In ac faucibus orci. Vestibulum euismod ultricies lectus sit amet varius.

Etiam urna sapien, elementum eget rutrum at, convallis in neque. Pellentesque ac justo eu tortor eleifend aliquet id dapibus ipsum. Donec in lobortis est, vitae cursus ante. Pellentesque pellentesque sapien vitae purus volutpat imperdiet a blandit erat. Nulla facilisi. Donec dictum dictum lacus ut semper. Pellentesque vel pulvinar libero, at laoreet enim. Duis tempus porttitor ante nec fermentum.

Sed ut felis a libero vestibulum gravida. Vestibulum augue neque, lobortis ac quam et, interdum malesuada neque. Morbi at leo sit amet metus eleifend congue sit amet et metus. Sed magna nibh, aliquet tincidunt lectus quis, sollicitudin congue tellus. Aliquam ligula sem, pretium euismod elementum non, condimentum sit amet arcu. Pellentesque condimentum ex enim, at vestibulum urna maximus eu. Aliquam elementum, nisl vel consectetur viverra, sapien orci venenatis tellus, consectetur pretium elit orci at velit. Integer sagittis sapien metus, nec porttitor mi consectetur non. Suspendisse vel metus quis sem rutrum laoreet. Sed molestie egestas commodo.

""")
2/0
