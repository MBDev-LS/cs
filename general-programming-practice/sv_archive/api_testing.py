
import time
from waybackpy import WaybackMachineSaveAPI

url = "https://github.com/microsoft/vscode-python/issues/9433"
user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"


save_api = WaybackMachineSaveAPI(url, user_agent)



startTime = time.perf_counter()

print(save_api.save())

endTime = time.perf_counter()

print(f'Archive took {endTime - startTime} seconds.')


print(save_api.cached_save)
print(save_api.timestamp())
