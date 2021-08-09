'''
filesystem
'''

import os


def load(path, mode='r', encoding='utf8'):
    '''
    加载文件内容。
    '''

    with open(path, mode, encoding=encoding) as reader:
        return reader.read()


def save(path, data, mode='w', encoding='utf8'):
    '''
    写入文件内容。
    '''

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
