import requests


URL = 'https://pddimp.yandex.ru/api2/admin/dns/%s'


def getExtIP():
    r = requests.get('https://myexternalip.com/raw')
    return(r.text.strip())


class Pdd:

    def __init__(self, *args, **kwargs):
        self.url = URL
        self.token = kwargs.get('token')
        self.domain = kwargs.get('domain')
        self.ip = kwargs.get('ip') or getExtIP()
        self.headers = {'PddToken': self.token}
        self.__aRecord = None
        self.loadARecord()
    
    @property
    def a(self):
        if not self.check():
            return
        return self.__aRecord
    
    @a.setter
    def a(self, ip):
        if not self.check():
            return
        self.__aRecord = self.saveARecord(ip or self.ip) or self.__aRecord
        
    def checkParam(self, paramName):
        if (not getattr(self, paramName)) or (getattr(self, paramName) is None):
            print('Parameter [%s] is not specified' % paramName)
            return False
        return True

    def check(self):
        return all(map(
            lambda x: self.checkParam(x),
            ['token', 'domain']
            ))

    def loadARecord(self):
        r = requests.get(
            URL % 'list',
            params={'domain': self.domain},
            headers=self.headers
            )
        self.__aRecord = [record for record in r.json().get(
            'records') if record.get('type') == 'A'][0]


    def saveARecord(self, ip=None):
        if not self.check():
            return
        recordId = self.__aRecord.get('record_id')
        if not recordId: return
        newIp = ip or self.ip
        # print(self.__aRecord, newIp)
        oldIp = self.__aRecord.get('content')
        if (oldIp == newIp):
            return 'No IP change detected for %s with IP %s, skipping update' % (self.domain, NewIp)

        r = requests.post(URL % 'edit', data={
                        'domain': self.domain, 
                        'record_id': recordId, 'content': newIp},
                        headers=self.headers)
        result = r.json()
        self.__aRecord = result.get('record')
        return 'Updated %s from %s to %s' % (self.domain, oldIp, newIp)
