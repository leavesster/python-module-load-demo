import asyncio
import importlib.util
import sys

async def main():
    module_name = "funccc"

    origin_module = sys.modules.copy()
    # delete = []
    # for name in sys.modules.keys():
    #     if name.startswith(module_name):
    #         delete.append(name)

    # for module_name in delete:
    #     del sys.modules[module_name]
            

    spec = importlib.util.spec_from_file_location(module_name, "./funccc/__init__.py")
    assert spec is not None

    module = importlib.util.module_from_spec(spec)

    assert spec.loader is not None
    spec.loader.exec_module(module)


    delete = sys.modules.keys() - origin_module.keys()
    for module_name in delete:
        del sys.modules[module_name]
    module.main()

async def loop():
    while True:
        print("Looping")
        await main()
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(loop())