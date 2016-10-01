from urllib2 import Request, urlopen
import json

def get_recipe():
    request = Request('http://food2fork.com/api/search?key=4dcf9327553c0ed33a73821107e4cb73&q=chicken,broccoli')
    response_body = urlopen(request).read()
    return json.loads(response_body)

print get_recipe()
