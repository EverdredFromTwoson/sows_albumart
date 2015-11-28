import json
f=open('collage.json', 'r')
j = json.loads(f.read())
f.close()
torrents = j['response']['torrentgroups']
for torrent in torrents:
	if torrent['musicInfo']:	
		if 'artists' in torrent['musicInfo']:
			artists = torrent['musicInfo']['artists']
		else:
			artists = 'sigh...'
		name = torrent['name']
		print "%s - %s\n" %(artists, name)

print len(torrents)
