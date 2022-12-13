import requests
url = 'https://rentry.co/triesexam/pdf'
r = requests.get(url, allow_redirects=True)
open('exam.pdf', 'wb').write(r.content)