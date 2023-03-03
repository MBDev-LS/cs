
# from pynytimes import NYTAPI
# from custom_api_wrappers import NYT_Newswire

# nyt = NYTAPI('AAaD35Ag8HWYrh2Rfc6GkEBwtbMBGte3', parse_dates=True)

# top_story = nyt.top_stories(section='politics')[0]

# newswire = NYT_Newswire('AAaD35Ag8HWYrh2Rfc6GkEBwtbMBGte3')

# print(newswire.get_latest())

import bbc_feeds

stories = bbc_feeds.news().top_stories('uk', limit=3)
forestHillWeather = bbc_feeds.weather().forecast('se23')

print(forestHillWeather)

# for story in stories:
#     print(story.title)
#     print(story.summary)
#     print(type(story))


# Next tasks: Create full wrapper (with Article class)
# and create Django endpoint and cacheing.
# Then create live news page.
