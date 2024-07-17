import importlib.util
import sys

# https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
def import_module(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None, f"Could not find module at {file_path}"
    
    module = importlib.util.module_from_spec(spec)
    
    # 使用 relative import 需要有这个
    sys.modules[module_name] = module

    assert spec.loader is not None, f"Could not find loader for module {module_name}"
    spec.loader.exec_module(module)
    return module

def load_module(file_path, module_name):
    if sys.modules.get(module_name):
        return sys.modules[module_name]
    return import_module(file_path, module_name)

if __name__ == '__main__':
    # directory module 只能引用  __init__.py 文件，然后使用其中 import 的内容。
    # 文件夹内可以任意使用 relative import
    m1 = import_module("./m/__init__.py", "bbb")
    m1.main()
    m1.main()

    m3 = import_module("./m/__init__.py", "bbb")
    m3.main()