from io import BytesIO
from zipfile import ZipFile
from base64 import b64encode, b64decode
from importlib import import_module


def save(path, **data):
    '''
    生成指定的压缩源码文件。
    '''

    lines = ['___pkg___={}']
    for p, n in data.items():
        with BytesIO() as bio:
            with ZipFile(bio, 'w') as zf:
                zf.write(p, n)
            r = b64encode(bio.getbuffer())
            lines.append(f'{n}={r}')
    with open(path, 'w', encoding='utf8') as writer:
        writer.writelines(lines)


def load(module, name):
    '''
    获取压缩模块的指定数据。
    '''

    m = import_module(module)
    if name not in m.___pkg___:
        b = b64decode(getattr(m, name))
        with BytesIO(b) as bio:
            with ZipFile(bio, 'r') as zf:
                r = BytesIO(zf.read(name))
                m.___pkg___[name] = r
    return m.___pkg___[name]
