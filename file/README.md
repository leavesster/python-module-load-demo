# import 单文件

```python
import importlib.util
import sys

# For illustrative purposes.
import tokenize
file_path = tokenize.__file__
module_name = tokenize.__name__

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
```

单文件的 module 可以直接使用，不需要加到 sys.modules 中。这种加载方式，每次都会重新加载文件，不会缓存文件内容。如果想缓存，反而要自己持有 module 或者放进 sys.modules，然后后面从 modules 中取。