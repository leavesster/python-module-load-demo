import importlib.util
import sys

# https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
def import_module(file_path, module_name):

    original_keys = set(sys.modules.keys())

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None, f"Could not find module at {file_path}"
    
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module

    assert spec.loader is not None, f"Could not find loader for module {module_name}"
    spec.loader.exec_module(module)

    try:
        return module
    finally:
        # remove the module from sys.modules
        for key in set(sys.modules.keys()) - original_keys:
            del sys.modules[key]

async def main():
    while True:
        m = import_module('./m/__init__.py', 'bbb')
        m.main()
        await asyncio.sleep(3)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
