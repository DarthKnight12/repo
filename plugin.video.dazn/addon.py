# -*- coding: utf-8 -*-

from resources.lib.client import Client
from resources.lib import items
from resources.lib.common import *

client = Client()

def run():
    if mode == 'rails':
        items.rails_items(client.rails(id,params))
    elif mode == 'rail':
        items.rail_items(client.rail(id,params))
    elif mode == 'play':
        items.playback(client.playback(id))
    elif mode == 'play_context':
        items.play_context(client.playback(id), title)

args   = urlparse.parse_qs(sys.argv[2][1:])
mode   = args.get('mode', ['rails'])[0]
title  = args.get('title', [''])[0]
id     = args.get('id', ['home'])[0]
params = args.get('params', [''])[0]
if not args:
    args = version
log('[%s] arguments: %s' % (addon_id, str(args)))

if id == 'home':
    client.startUp()
    if client.TOKEN:
        run()
else:
    run()