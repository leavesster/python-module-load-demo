# Directory package

如果想编写工程化代码，在一个文件夹中编写 python 代码，同时用上相对地址引用时。需要使用代码 import `__init__.py`，然后调用 `__init__.py` 中 import 的内容。

同时需要手动将`__init__.py`生成的 module 添加到 sys.modules，此时系统会自动将 parent module 添加到 sys.modules，这样就可以支持 import 相对地址了。

带来的问题是 `importlib.util` 生成的 module 只是 `__init__.py` 的 module，其他相对地址引用的 module 因为已经自动被加载，会造成缓存，无法更新。需要手动删除。

