import search

BASE_TAG_ACCEPTANCE_RATE = 0.2

def run_dubeTube_algorithm(video_list, cookies_list):

    if len(cookies_list) == 0:
        return video_list

    accumulation = dict()
    for cookie in cookies_list:
        if cookie not in accumulation:
            accumulation[cookie] = 1
        else:
            accumulation[cookie] += 1
    
    accepted_tags = []
    for tag in accumulation:
        if accumulation[tag] / len(cookies_list) >= BASE_TAG_ACCEPTANCE_RATE:
            accepted_tags.append(tag)
    
    display = search.search_by_tags(video_list, accepted_tags)
    return display

