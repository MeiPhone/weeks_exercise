# 开文件
with open ('../votes.txt','r',encoding='utf8') as f:
    ballots = f.readlines()
result = {}
# 总票数
total = len(ballots)
#count the votes of each one
for vote in ballots:
    ba = vote.replace(' ','').replace('\t','').replace('<tab>','').strip()
    if ba in result:
        result[ba]=result[ba]+1
    else:
	    result[ba] = 1
print('total votes: %d' %total)
for re in result:
    print (re + ':',result[re])
#input the favorite singer
fav = input('Please input your favorite singer:')
while fav not in result:
    print (fav,'doesn\' exist')
    fav = input('Please input your favorite singer:')
print('\'%s\'get %d votes,take up %.2f%%' %(fav,result[fav],(result[fav]/total)*100))
#find the champian
ch_vote = 0

for ch in result:
    if result[ch] > ch_vote:
        champion = ch
        ch_vote = result[ch]
print ('the champion is %s who got %d votes' %(champion,ch_vote))

for same in result:
    if result[same] == ch_vote:
        if (same==champion) is False:
            print ('there is another one got the same votes! %s' %same)
