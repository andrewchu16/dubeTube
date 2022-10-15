import video

## Cases
##
## SearchTextRatio(query, text) is negative
## the text/title is shorter than the query, and thus text is not a valid title for the query
##
## SearchTextRatio(query, text) is one
## the exact query is in the title
##
## the closer SearchTextRatio is to one, the higher the similarity
## the larger SearchTextRatio is, the lower the similarity

## searches if text contains the query
def search_text(query, text):

    if len(text) < len(query):
        text, query = query, text

    n = len(query)+1
    m = len(text)+1

    diff_array = []

    for i in range(n):
        diff_array.append([])
        for j in range(m):
            diff_array[i].append(0)
    
    for i in range(n):
        diff_array[i][0] = i
    for j in range(m):
        diff_array[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            k = min(diff_array[i-1][j-1], diff_array[i][j-1], diff_array[i-1][j]) + 1
            if (query[i-1] == text[j-1]):
                k -= 1
            diff_array[i][j] = k

    return diff_array[n-1][m-1]


def search_text_ratio(query, text):
    denominator = len(text) - search_text(query, text)
    if denominator == 0: 
        # If denominator is 0, the two strings have no compatibility
        denominator = 0.01
    return len(query)/(denominator)


def search_by_title(video_list, query):

    sorted_videos = []
    for index, next_video in enumerate(video_list):
        similarity_score = search_text_ratio(query, next_video.title)
        sorted_videos.append((similarity_score, index))

    sorted_videos.sort()

    relevance_sorting = []
    for next_video in sorted_videos:
        relevance_sorting.append(video_list[next_video[1]])

    return relevance_sorting


def search_by_tags(video_list, tag_list):

    sorted_videos = []
    for index, next_video in enumerate(video_list):
        union = set(tag_list + next_video.tags)
        sorted_videos.append((len(union), index))

    sorted_videos.sort()
    sorted_videos.reverse()

    relevance_sorting = []
    for next_video in sorted_videos:
        relevance_sorting.append(video_list[next_video[1]])

    return relevance_sorting


def search(video_list, query, tag_list):

    title_sorting = search_by_title(video_list, query)
    tag_sorting = search_by_tags(video_list, tag_list)

    accumulated_scores = []
    for i in range(len(title_sorting)):
        accumulated_scores.append((i, i))

    for i in range(len(tag_sorting)):
        for j in range(len(title_sorting)):
            if tag_sorting[i] == title_sorting[j]:
                accumulated_scores[j][0] += i
    
    accumulated_scores.sort()
    new_relevance = []
    for i in range(len(accumulated_scores)):
        new_relevance.append(title_sorting[accumulated_scores[i][1]])

    return new_relevance

def get_tagged_videos(tag, video_list):
    output = []
    for vid in video_list:
        if tag in vid.tags:
            output.append(vid)
    return output