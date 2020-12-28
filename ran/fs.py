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
