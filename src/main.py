import os 
import sys 

import web.host as webh

if __name__ == "__main__":
    hoster = webh.HTTPSocketWebPageHoster("127.0.0.1", "8000", "via")
    hoster.start()