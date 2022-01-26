import urllib.request as ur
import urllib.error as ue

t="https://www.wp.pl/"
try: 
    z=ur.urlopen(t)
    print("strona istnieje")
except ue.URLError as er:
    print("strona nie istnieje")