# Python 接口树

## 当前接口

```text
chatnote
├── __init__.py  # __version__：包版本
└── cli.py       # main：Click 命令行入口
```

```python
from chatnote import __version__
```

当前不提供笔记业务 API。后续业务能力应实现为可导入的函数或类，命令行仅负责参数解析和输出，并同步更新测试及接口文档。
