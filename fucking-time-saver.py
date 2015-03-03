#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import argparse
import os
import shutil
import subprocess
import sys
import time


def notify():
    # Voice notification on OSX
    if sys.platform == 'darwin':
        subprocess.call(['say', '-v', 'Vicki', 'A new savegame is available'])


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


def directory(item):
    if not os.path.exists(item):
        raise ValueError('Error: {} does not exist'.format(item))
    if not os.path.isdir(item):
        raise ValueError('Error: {} is not a directory'.format(item))
    return item


def filepattern(item):
    if not item.startswith('*'):
        item = '*{}'.format(item)
    return item


def parseArguments():
    parser = argparse.ArgumentParser(
        description=u'Synchronyzes Europa Universalis 4™ multiplayer savegames '
        u'in local directories using the DropBox™')
    parser.add_argument(
        'source', metavar='SOURCE', type=directory,
        help='the source directory to monitorize')
    parser.add_argument(
        'destination', metavar='DESTINATION', type=directory,
        help='the directory in which savegames should be copied')
    parser.add_argument(
        'patterns', nargs='+', metavar='PATTERN', type=filepattern,
        help='file patterns to be monitored (ie. shared_*.eu4)')

    args = parser.parse_args()
    return args


def main():
    args = parseArguments()

    src, dst = args.source, args.destination
    patterns = args.patterns

    def handler(src):
        partial(shutil.copy2, dst=dst)(src)
        notify()

    event_handler = Eu4SaveGameEventHandler(handler, patterns=patterns)

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
