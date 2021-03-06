import subprocess
import json

from Models.Item import Item
from Utils.cookies import SESS_ID
from Utils.config import CHARACTER_NAME, LEAGUE_NAME

def queryItemsFromStash(tab):
    url = "https://www.pathofexile.com/character-window/get-stash-items?accountName=%s&realm=pc&league=%s&tabs=0&tabIndex=%d" \
          % (CHARACTER_NAME, LEAGUE_NAME, tab)

    commands = [
        'curl',
        '--cookie',
        "POESESSID=" + SESS_ID,
        url
    ]

    response = subprocess.check_output(commands)

    items = json.loads(response)['items']

    for item in items:
        try:
            yield(Item(item))
        except:
            print("failed to parse", item)
            pass # just skip unparsable garbage