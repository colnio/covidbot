import threading 

import listener
import downloader
import quiz

downloader.first_run()
listen = threading.Thread(target=listener.listen(), daemon=True)
update = threading.Thread(target=downloader.update(), daemon=True)
quiz = threading.Thread(target=quiz.quizer(), daemon=True)

update.start()
listen.start()
quiz.start()