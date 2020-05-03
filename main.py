import threading 

import listener
import downloader

listen = threading.Thread(target=listener.listen(), daemon=True)
update = threading.Thread(target=downloader.update(), daemon=True)

update.start()
listen.start()
