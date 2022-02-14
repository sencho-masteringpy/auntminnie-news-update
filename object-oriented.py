def info():
    print('how to use this package:')
    print('package News for the recent news in auntminnie')
    print('package conferences for the recent conferences radiology in auntminnie')
    print('.test for testing the web')
    print('.data for take a data from web')
    print('.run for run .test and .data')


class Dashboard:
    def __init__(self, url):
        self.url = url
        print('This the package for retrive last news and conferences about radiology')

    def test(self):
        if self.url == 'ok':
            print(f"is accsesable")
        else:
            print("Can't accses web")

    def data(self):
        pass

    def run(self):
        self.test()
        self.data()


class News(Dashboard):
    def data(self):
        print('This is the recent news:')
        data = self.url
        print(data)


class Conferences(Dashboard):
    def data(self):
        print('This is the recent radiology conferences:')
        data = self.url
        print(data)