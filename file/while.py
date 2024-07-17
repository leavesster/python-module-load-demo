import importlib.util
import sys

# https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
def import_module(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None, f"Could not find module at {file_path}"
    
    module = importlib.util.module_from_spec(spec)
    # 如果是 file，没有相对引用，可以忽略这个，这样还能避免污染
    # sys.modules[module_name] = module

    assert spec.loader is not None, f"Could not find loader for module {module_name}"
    spec.loader.exec_module(module)
    return module

async def main():
    while True:
        m = import_module('./func.py', 'b')
        m.main()
        await asyncio.sleep(3)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
