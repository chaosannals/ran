import sys
import os
from time import sleep
from threading import Thread
from inspect import getmodule
from importlib import import_module, reload


def list_module_mtime(prefix = None) -> dict:
    '''
    列举模块文件修改时间。
    '''

    result = {}
    for n, m in sys.modules.items():
        if hasattr(m, '__file__'):
            p = getattr(m, '__file__')
            if prefix != None and not p.startswith(prefix):
                continue
            s = os.stat(p)
            result[n] = s.st_mtime_ns
    return result


def diff_module_mtime(one: dict, two: dict) -> dict:
    '''
    比较模块前后的修改时间。
    '''

    result = {}
    for n, t in one.items():
        tt = two[n]
        if tt != t:
            result[n] = max(tt, t)
    return result


class ModuleReloader:
    '''
    模块加载器。
    '''

    def __init__(self, prefix=None):
        '''
        设置初始值。
        '''

        self.ticker = None
        self.able = True
        self.prefix = prefix
        self.mts = list_module_mtime(prefix)

    def watch(self, interval=1):
        '''
        监听模块修改。
        '''

        if self.ticker == None or not self.ticker.is_alive():
            def tick(reloader, interval):
                while reloader.able:
                    reloader.reload()
                    sleep(interval)
            self.ticker = Thread(target=tick, args=[self, interval])
            self.ticker.daemon = True
            self.ticker.start()

    def reload(self):
        '''
        重新加载模块。
        '''

        nmts = list_module_mtime(self.prefix)
        mmts = diff_module_mtime(nmts, self.mts)
        self.mts = nmts

        # 重新加载模块
        for n in mmts.keys():
            if n == '__main__':
                continue
            m = import_module(n)
            reload(m)
        
        # 替换 from xx import xx 引入的变量。
        if len(mmts) == 0:
            return
        for n in nmts.keys():
            m = import_module(n)
            for k, v in m.__dict__.items():
                if not hasattr(v, '__module__'):
                    continue
                imn = getattr(v, '__module__')
                if imn in mmts:
                    im = getmodule(v)
                    nv = getattr(im, k)
                    setattr(m, k, nv)
