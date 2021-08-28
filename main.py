import requests
import time
import random
import hashlib
from cf_requests import CFRequest
from credentials import key, secret


def get_link(key, secret, now):
    link_template = 'https://codeforces.com/api/contest.hacks?contestId=566&apiKey={}&time={}&apiSig={}{}'
    head = random.randint(100000, 999999)
    # now = int(time.time())
    tohash = f'{head}/contest.hacks?apiKey={key}&contestId=566&time={now}#{secret}'
    h = hashlib.sha512(tohash.encode('utf-8'))
    hash = h.hexdigest()
    link = link_template.format(key, now, head, hash)
    print(link)


s = CFRequest(key, secret).query(
    'contest.hacks',
    contestId=566
)

print(s['result'])