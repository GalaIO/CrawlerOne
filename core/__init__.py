# -*- encoding: utf-8 -*-
__author__ = 'GalaIO'

import threading

from module.queue import urlQueue
from module import queue
from module.queue import responseQueue
from module import downloader
from module import handler

class DownloadThread(threading.Thread):
    def __init__(self):
        self.stop_thread = False
        threading.Thread.__init__(self)

    def run(self):
        while not self.stop_thread:
            # 取出url 下载
            url = queue.pop(urlQueue)
            if url == None:
                self.stop()
                break
            response = downloader.download(url)
            queue.push(responseQueue, (url, response))
        print 'download thread exit!'

    def stop(self):
        self.stop_thread = True

class HandlerThread(threading.Thread):
    def __init__(self):
        self.stop_thread = False
        threading.Thread.__init__(self)

    def run(self):
        while not self.stop_thread:
            # 取出url 下载
            response = queue.pop(responseQueue)
            if response == None:
                self.stop()
                break
            urls = handler.deal(response)
            while len(urls):
                queue.push(urlQueue, urls.pop(0))
        print 'handler thread exit!'

    def stop(self):
        self.stop_thread = True