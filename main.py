#!/usr/bin/env python

from functools import partial
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import os
import shutil
import sys
import time


class Eu4SaveGameEventHandler(PatternMatchingEventHandler):
    def __init__(self, handler, *args, **kwargs):
        super(Eu4SaveGameEventHandler, self).__init__(*args, **kwargs)
        self._handler = handler

    def on_created(self, event):
        if not event.is_directory:
            src = event.src_path
            self._handler(src)

    def on_modified(self, event):
        if not event.is_directory:
            src = event.src_path
            self._handler(src)


def main():
    # FIXME: add proper option parsing
    src, dst = map(partial(os.path.join, os.getcwd()), sys.argv[1:3])
    patterns = map('*{}'.format, sys.argv[3:])

    event_handler = Eu4SaveGameEventHandler(
        partial(shutil.copy2, dst=dst), patterns=patterns)

    observer = Observer()
    observer.schedule(event_handler, src, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
