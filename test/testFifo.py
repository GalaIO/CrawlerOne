# -*- encoding: utf-8 -*-
__author__ = 'GalaIO'

from module import queue

queue.push(queue.urlQueue, 1)
queue.push(queue.urlQueue, 2)
queue.push(queue.urlQueue, 3)
queue.push(queue.urlQueue, 4)
print queue.pop(queue.urlQueue)
print queue.pop(queue.urlQueue)
print queue.pop(queue.urlQueue)
print queue.pop(queue.urlQueue)
print queue.pop(queue.urlQueue)

import requests

re = requests.get("http://www.baidu.com")
print re.content, re.text
