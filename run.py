# -*- encoding: utf-8 -*-
__author__ = 'GalaIO'

from core import DownloadThread, HandlerThread
from module.queue import urlQueue
from module import queue

if __name__ == '__main__':
    th1 = DownloadThread()
    th2 = HandlerThread()
    queue.push(urlQueue, 'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2381878087.jpg')
    # queue.push(urlQueue, "http://www.baidu.com")
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print 'app is exit!!!'

