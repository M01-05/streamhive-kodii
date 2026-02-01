import xbmcgui, xbmcplugin, sys

handle = int(sys.argv[1])

items = [
    ("Action", "https://www.netzkino.de/action/"),
    ("Komödie", "https://www.netzkino.de/komoedie/"),
    ("Horror", "https://www.netzkino.de/horror/"),
    ("Liebesfilme", "https://www.ardmediathek.de/"),
    ("Bollywood", "https://www.pluto.tv/de/genre/bollywood"),
    ("Kriegsfilme", "https://www.arte.tv/de/videos/serie/krieg-und-konflikt/"),
    ("Animation / Familie", "https://www.pluto.tv/de/genre/kinder-und-familie"),
    ("Slasher", "https://www.netzkino.de/slasher/"),
    ("Serien", "https://www.joyn.de/serien")
]

for name, url in items:
    li = xbmcgui.ListItem(label=name)
    xbmcplugin.addDirectoryItem(handle, url, li, isFolder=False)

xbmcplugin.endOfDirectory(handle)
