class MyCustomContextManager:
    def __enter__(self):
        print('entered')

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('left')


with MyCustomContextManager() as hello:
    print(hello)

