#!/usr/bin/python
#	huffman coding
#	http://wikipedia.org/Huffman_coding

def heap_gen(Data):
	global tree,parent
	tree=list(Data)
	while len(tree)>1:
		LCh=min(tree)
		index=tree.index(LCh)
		LChL=list(tree[index])
		del tree[index]
		RCh=min(tree)
		index=tree.index(RCh)
		RChL=list(RCh)
		del tree[index]
		parent=(LChL[0]+RChL[0],LCh,RCh)
		tree.append(parent)
	return tree[0]
	
	''' generate huffman Code '''
def encode(huffheap, prefix = ''):
	global keys
	if len(huffheap) == 2:
		key=(huffheap[1],str(prefix))
		keys.append(key)
		
	else:
		encode(huffheap[1], prefix + '0')
		encode(huffheap[2], prefix + '1')

def get_data():	
	global string
	string='AAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDEWQAAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDE\
			AAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDEWQAAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDE\
			AAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDEWQAAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDE\
			AAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDEWQAAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDE\
			AAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDEWQAAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDE\
			AAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDEWQAAAAAAAAAAAAAAAAAAABBBBBBBBBFDFGCVCXSDERTYUAXZSDE'
	get_CharCount(string)
	
def get_CharCount(string):
	global charCount
	charCount = {}
	huffheap=[]
	for char in string:
		charCount[char]=charCount.get(char,0)+1
	for items in charCount.items():
		items=list(items)
		huffheap.append((items[1],items[0]))
	huffheap.sort()
	huffheap=heap_gen(huffheap)
	encode(huffheap)

def codes():
	huffcode=''
	code={}
	for items in keys:
		items=list(items)
		code[items[0]]=items[1]
	for i in string:
		huffcode=huffcode + str(code[i])
	print huffcode

if __name__== '__main__':
	
	keys=[]
	get_data()
	codes()


