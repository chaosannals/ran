'''
filesystem
'''

import os


def load(path, **kws):
    '''
    加载文件内容。
    '''

    mode = kws.get('mode', 'r')
    encoding = kws.get('encoding', 'utf8')
    with open(path, mode, encoding=encoding) as reader:
        return reader.read()


def save(path, data, **kws):
    '''
    写入文件内容。
    '''

    mode = kws.get('mode', 'w')
    encoding = kws.get('encoding', 'utf8')
    with open(path, mode, encoding=encoding) as writer:
        writer.write(data)


def list_files(folder, deep=True):
    '''
    列举文件。
    '''

    files = []
    for name in os.listdir(folder):
        path = os.path.abspath(folder + '/' + name)
        if deep and os.path.isdir(path):
            files.extend(list_files(path))
        elif os.path.isfile(path):
            files.append(path)
    return files
