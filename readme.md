# [ran](https://github.com/chenshenchao/ran)

## 安装

```bash
pip install ran
```

## 示例

### fs

```python
from ran import fs

# 读取文件内容
content = fs.load('path')
```

### mm

自动重载修改的模块。

```python
from ran.mm import ModuleReloader
mr = ModuleReloader()
mr.watch()
```

### idmk

生成 ID

```python
from ran.idmk import IdentifierMaker

idmkr = IdentifierMaker(1)

for i in range(1000):
    print(idmkr.make())
```
