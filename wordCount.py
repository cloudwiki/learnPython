
paragraph=r'''Washington Democrats wasted no time this week trying to tie congressional Republicans facing re-election to Donald Trump, now that he's the presumptive GOP presidential nominee.

Their major focus appears to be the Senate, considering they have to win a net total of four seats to retake control of the chamber, though the more outside chance of also flipping the House now seems more attainable.

Democrats will have plenty of soundbites and video clips of Trump talking about Muslims, women and other politically-sensitive issues in ways that party members will find offensive.

However, linking him and his remarks to vulnerable GOP incumbents right away will be more difficult, considering few have endorsed Trump -- the lone Republican presidential candidate after his commanding win Tuesday in Indiana forced out primary rivals Texas Sen. Ted Cruz and Ohio Gov. John Kasich.

"There's no going back for vulnerable incumbents and candidates who've pledged to support Trump," the Democratic Senatorial Campaign Committee said Wednesday. "Now they have the herculean task of explaining their own out-of-touch records while running alongside their party's new standard bearer: a divisive and dangerous personality."
'''

#print paragraph

wordList = paragraph.split()
print wordList
print "=" * 20
wordMap = {}
for word in wordList:
	if word in wordMap:
		wordMap[word]+=1
	else:
		wordMap[word] = 1

print wordMap

wordMap.sort(len(key))
print wordMap
