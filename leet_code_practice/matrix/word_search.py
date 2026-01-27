board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"




#DFS -Deapth First Search + Backtracking


def word_search(board,word):
    row,col = len(board),len(board[0])
    def dfs(r,c,i):
        if i == len(word):
            return True 
        
        if r<0 or c<0 or r>=len(board)or c>=len(board[0])or board[r][c]!=word[i]:
            return False
        
        temp = board[r][c]
        board[r][c]="#"

        found = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
        board[r][c] = temp
        return found
    
    for r in range(row):
        for c in range(col):
            if dfs(r,c,0):
                return True
            
    return False
 
  
print(word_search(board,word))





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

    for key in ac:
        if key in dc:
            if dc[key] >0:
                count+=1
                dc[key]-=1

    if count == len(word):
        return True
    
    return False


print(word_search(board,word))


    



