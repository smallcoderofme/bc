ACoins = []
'''
请注意，随着时间的流逝，区块链中的块数对于打印来说将是异常高的。因此，当您打印区块链的内容时，您可能必须决定要检查的范围
'''
def dump_blockchain (self):
	print("Number of blocks in the chain: " + str(len (self)))
	for x in range (len(TPCoins)):
		block_temp = TPCoins[x]
		print ("block # " + str(x))
		for transaction in block_temp.verified_transactions:
			display_transaction(transaction)
			print('--------------')
		print('=====================================')



