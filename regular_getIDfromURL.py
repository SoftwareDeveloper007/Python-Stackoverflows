import re

page = 'https://itunes.apple.com/us/podcast/foossapod/id1254680685'
regex = r"id([\d]+)"
match = re.findall(regex, page)
id = match[0]
print(id)
API = 'https://itunes.apple.com/lookup?id=1254680685'

