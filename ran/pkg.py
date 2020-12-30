import os
from io import BytesIO
from zipfile import ZipFile
from base64 import b64encode, b64decode
from importlib import import_module
from . import fs


def save(path, filter=lambda x, y: True, **data):
    '''
    生成指定的压缩源码文件。
    '''

    lines = ['___pkg___={}\n']
    for n, p in data.items():
        with BytesIO() as bio:
            with ZipFile(bio, 'w') as zf:
                if os.path.isfile(p):
                    if filter(n, p):
                        zf.write(p, n)
                elif os.path.isdir(p):
                    for cp in fs.list_files(p):
                        cn = os.path.relpath(cp, p)
                        if filter(cn, cp):
                            zf.write(cp, cn)
            r = b64encode(bio.getbuffer())
            lines.append(f'{n}={r}\n')
    with open(path, 'w', encoding='utf8') as writer:
        writer.writelines(lines)


def load(module, name, raw=False):
    '''
    获取压缩模块的指定数据。
    '''

    m = import_module(module)
    if name not in m.___pkg___:
        b = b64decode(getattr(m, name))
        with BytesIO(b) as bio:
            with ZipFile(bio, 'r') as zf:
                m.___pkg___[name] = zf.read(name)
    r = m.___pkg___[name]
    return r if raw else BytesIO(r)


def cast(module, name, path):
    '''
    提取压缩模块的指定文件到指定路径。
    '''

    m = import_module(module)
    b = b64decode(getattr(m, name))
    with BytesIO(b) as bio:
        with ZipFile(bio, 'r') as zf:
            zf.extractall(path)
