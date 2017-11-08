# -*- encoding: utf-8 -*-
__author__ = 'GalaIO'
'''
使用python自带的Queue用于消息队列
'''
import Queue
urlQueue = Queue.Queue(100)
responseQueue = Queue.Queue(100)

def push(queue, element):
    queue.put(element, block=True, timeout=None)

def pop(queue):
    try:
        return queue.get(block=True, timeout=60)#接收消息
    except Queue.Empty:
        return None