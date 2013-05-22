from mpd import MPDClient, MPDError

# Those Settings should be suitable for most mpd installations

HOST = "localhost"      #Host and Port of the MPD Server
PORT = 6600             
COLOR = "#FFFFFF"       #Color of the output

json_dict = {'name': 'mpd', 'full_text': '', 'color': COLOR} 

def return_json():
    try:
        c = MPDClient()
        c.connect(HOST, PORT)
        data = c.currentsong()
        c.disconnect()
    except MPDError:
        json_dict['full_text'] = 'MPD not running'
        return json_dict 

    if 'artist' in data.keys():
        artist = data['artist']
    else:
        artist = '???'

    if 'title' in data.keys():
        title = data['title']
    else:
        title = '???'

    json_dict['full_text'] = "%s - %s" % (artist, title)

    return json_dict
