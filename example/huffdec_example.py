#!/usr/bin/python
# example code
#
data='000101011101010000010101'
keys=[['00','a'],['01','b'],['11','c']]

def _huff_code_dec_(key,bits):
	
	encoded_bits=''
	
	for char in bits:
		encoded_bits=str(encoded_bits)+char
		key_list_count=0
		
		while 1:
			
			if len(encoded_bits)==1:break
			key_list_first=key[key_list_count]
			key_list_count=key_list_count+1	
			first_item=key_list_first[0]
			second_item=key_list_first[1]
			if encoded_bits==first_item:
				print second_item,
				encoded_bits=''
				break
			#if t==len(l)-1:break
		
_huff_code_dec_(keys,data)
