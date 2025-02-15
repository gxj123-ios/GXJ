class page:
    def __init__(self,driver):
        self.driver = driver
        self.baseurl='http://127.0.0.1/mgr/sign.html'
        self.timeout=2
    def _open(self,url):
        urlPlus = self.baseurl + url
        self.driver.get(urlPlus)
    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)