import urllib.request
from bs4 import BeautifulSoup
import json
import uuid

def operate(soup, tagId):
    return soup.find(class_ = str(tagId)).text.strip()

def parse_url(url):
    """
    Parse an url from cnn/travel

    Args:
        url ([str]): [url to parse]

    Returns:
        [dict]: [title, author, content]
    """

    data = urllib.request.urlopen(url).read().decode()
    soup =  BeautifulSoup(data, features='html.parser')
    
    art_title = operate(soup, 'Article__title') 
    art_author_line = operate(soup, 'Article__subtitle')
    art_body = operate(soup, 'Article__content')
    
    parsed_new = dict([
        ('title', art_title),
        ('author', art_author_line),
        ('content', art_body)
        ])
    return parsed_new

def save_as_json(data):
    """[Save as random name json]

    Args:
        data ([str])
    """
    fn = str(uuid.uuid4()) + ".json"
    with open(fn, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    import json
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Url to parse")
    parser.add_argument("-s", help="Save parsed Url", action="store_true")

    args = parser.parse_args()
    
    if args.s:
        parsed_url = parse_url(args.url)
        save_as_json(parsed_url)
        print("New has been saved")
    else:
        parsed_url = parse_url(args.url)
        print(json.dumps(parsed_url, indent=4))

