import requests
import time
import random
import hashlib

class CFRequest:
    
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
    

    def param_string_from_params(self, params):
        '''
        {contestId=566, kek=1} --> contestID=566&kek=1&
        '''

        result = ''
        for key in sorted(params.keys()):
            result += f'{key}={params[key]}&'
        return result

    def get_link(self, method_name, **params):
        param_string = self.param_string_from_params(params)
        link_template = 'https://codeforces.com/api/{method}?{param_string}apiKey={key}&time={time}&apiSig={rand}{hash}'
        head = random.randint(100000, 999999)
        now = int(time.time())
        tohash_template = '{rand}/{method}?apiKey={key}&{param_string}time={time}#{secret}'
        tohash = tohash_template.format(
            rand=head, 
            method=method_name,
            key=self.key,
            param_string=param_string,
            time=now,
            secret=self.secret 
        ).encode('utf-8')
        
        hash = hashlib.sha512(tohash).hexdigest()
        link = link_template.format(
            method=method_name,
            param_string=param_string,
            key=self.key,
            time=now,
            rand=head,
            hash=hash
        )
        return link

    def query(self, method_name, **params):
        r = requests.get(self.get_link(method_name, **params))
        return r.json()
