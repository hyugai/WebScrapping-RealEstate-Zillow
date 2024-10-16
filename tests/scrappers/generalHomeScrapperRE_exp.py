# libs
import os, sys
cwd = os.getcwd()
os.chdir('src/'); path_to_src = os.getcwd()
os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from _libs import *
from _usr_libs import *

# exp
db_path = cwd + "/tests/dbs/real_estate.db"
headers = {'User-Agent': random.choice(USER_AGENTS), 'Accept-Encoding': ACCEPT_ENCODING, 
           'Accept-Language': ACCEPT_LANGUAGE}

home_tracker = TableTracker(db_path, "general_info")
url_tracker = TableTracker(db_path, "city_url")
home_scrapper = GeneralHomeScrapper_RE(headers, home_tracker, url_tracker)
home_scrapper.transform()