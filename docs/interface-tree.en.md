# Python Interface Tree

## Current Interfaces

```text
chatnote
├── __init__.py  # __version__: package version
└── cli.py       # main: Click command-line entry point
```

```python
from chatnote import __version__
```

No note-management API is currently provided. Future domain behavior should live in importable functions or classes, with thin CLI adapters and matching tests and interface documentation.
