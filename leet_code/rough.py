board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCDDEA"




def word_search(board,word):
    w = list(word)
    dc = {}
    for i in board:
        for j in i:
            dc[j] = dc.get(j,0)+1


    count = 0
    ac = {}
    for wl in w:
        ac[wl] = ac.get(wl,0)+1

    for key,value in ac.items():
        if key in dc:
            if dc[key] >0:
                count+=1
                dc[key]-=1

    if count == len(word):
        return True
    
    return False


print(word_search(board,word))