import sys, time, logging
from flask import Blueprint
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

bp = Blueprint('watchdog', __name__)

if __name__ == '__main__':
    # format for logging info
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s -%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = FileSystemEventHandler()

    observer = Observer()
    try:
        while True:
            # Set the thred sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()