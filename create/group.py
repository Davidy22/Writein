from fuzzywuzzy import fuzz, process
from .models import poll, entry

def groupEntries(ID):
	entries = entry.objects.filter(pollID=ID)
	if (len(entries) == 0):
		return []
	buckets = []
	buckets.append([1, entries[0].text, [entries[0].text]])
	for a in entries[1:]:
		text = a.text
		i = 0
		for bucket in buckets:
			if (fuzz.ratio(text,bucket[1]) > 70):
				buckets[i][0] += 1
				buckets[i][2].append(text)
				break
			elif (i == len(buckets)-1):
				buckets.append([1,text,[text]])
				break
			i += 1
	out = []
	for bucket in buckets:
		out.append(bucket[1])
	return sorted(buckets,key=lambda x:x[0],reverse=True)
