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
def SearchText(query, text):
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

def SearchTextRatio(query, text):
    return len(query)/(len(text) - SearchText(query, text))

#print(SearchTextRatio(input(), "i love cats"))