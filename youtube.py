from httpx import get
from xmltodict import parse
from json import dumps, loads
from time import sleep

while True:
    video_list = list()
    channel_id = 'UCtpyX3AZ1v-gInaHTsyk6tw'

    responses = loads(dumps(parse(get(f'https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}').text)))
    responses = responses['feed']['entry']
    
    if (type(responses) == dict):
        first_vids = responses['media:group']
    else: first_vids = responses[0]['media:group']

    video_urls = first_vids['media:content']['@url']
    if (video_urls not in video_list):
        video_list.append(video_urls.split('?')[0])

        media_title = first_vids['media:title']
        thumbnails_ = first_vids['media:thumbnail']['@url']
        description = first_vids['media:description']
        video_views = first_vids['media:community']['media:statistics']['@views']

    print(video_list)
    sleep(30)
