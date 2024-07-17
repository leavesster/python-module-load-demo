from .a import a

count = 1

def main():
    global count
    print("value from a.py is", a())
    print("count is", count)
    count += 1