from urllib.request import urlopen
from django.http import JsonResponse

source_url = "https://time.com"

def get_stories(request):
    page = urlopen(source_url)
    page_data = page.read().decode("utf-8")
    ptr_start = 0
    find = lambda keyword,start: page_data.find(keyword, start)
    list_of_stories = []
    while len(list_of_stories)!=6:
        ptr_start = find("latest-stories__item",ptr_start)
        if ptr_start==-1:
            break
        ptr_start = find("=", ptr_start)
        story_link_start = ptr_start + 2
        ptr_start = find(">", story_link_start)
        story_link__end = ptr_start-1
        story_link = page_data[story_link_start:story_link__end]
        ptr_start = find(">", ptr_start+1)
        story_headline_start = ptr_start+1
        ptr_start = find("<", story_headline_start)
        story_headline=page_data[story_headline_start:ptr_start]
        list_of_stories.append({
            "title": story_headline,
            "link": source_url + story_link
        })
        ptr_start = find("</li>", ptr_start)
    
    return JsonResponse(list_of_stories, safe= False)
    

