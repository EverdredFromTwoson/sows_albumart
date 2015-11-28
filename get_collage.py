import requests

session='gUL7TOouY798J%2FFa%2B%2BDjx7O8GL67OS8t8s1AAn4ZDf8zvizAuXRPE80cOG7C1h6aHuhwHz8XXtZHJZB0SEfq80g0B%2FPqHKMhwWGFzjdhMw5A0YBTq%2FLcUuApNCh82khUELeTaGRpZORQR2abt5exSQ%3D%3D'

cookies = {'session':session}
url='https://bemaniso.ws/collages.php?id=59'
r = requests.get(url, cookies=cookies)
f=open('collages.html', 'w')
f.write(r.text.encode('utf8'))
f.close()
