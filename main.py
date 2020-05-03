import threading 

import listener

listen = threading.Thread(target=listener.bot())

listen.daemon = True
listen.start()