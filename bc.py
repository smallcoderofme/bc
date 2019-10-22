'''  Client '''
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
	"""
	客户端类生成的私人和公众使用内置Python键RSA算法
	请注意，您绝不要丢失私钥。为了保持记录，可以将生成的私钥复制到安全的外部存储中，或者您可以简单地将其ASCII表示记在一张纸上
	"""
	def __init__(self):
		random = Crypto.Random.new().read
		self._private_key = RSA.generate(1024, random)
		self._public_key = self._private_key.publickey()
	# 生成的公共密钥将被用作客户端的身份
	@property
	def identity(self):
		return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
'''
Dinesh = Client()
print(Dinesh.identity)
'''
class Transaction:
	"""创建一个Transaction类，以便客户能够向他人汇款。请注意，客户既可以是付款人，也可以是付款人。当您想收款时，其他发送者会创建交易并在其中指定您的公共地址"""
	def __init__(self, sender, recipient, value):
		self.sender = sender
		self.recipient = recipient
		self.value = value
		self.time = datetime.datetime.now()
	
	# 仅仅是为了通过单个变量访问整个交易信息
	def to_dict(self):
		if self.sender == 'Genesis':
			identity = 'Genesis'
		else
			identity = self.sender.identity
	# 我们使用以下代码行构造字典
		return collections.OrderedDict({
			'sender': identity,
			'recipient': self.recipient,
			'value': self.value
			'time': self.time})
	# 第一个参数是发送者，第二个参数是接收者的公钥，第三个参数是要转移的金额。该sign_transaction方法检索发件人的从第一个参数为演唱交易私钥
	def sign_transaction(self):
		private_key = self.sender._private_key
		signer = PKCS1_v1_5.new(private_key)
		h = SHA.new(str(self.to_dict)).encode('utf8')
		return binascii.hexlify(signer.sign(h)).decode('ascii')

	def display_transaction(transaction):
		dct = transaction.to_dict()
	    print ("sender: " + dct['sender'])
		print ('-----')
		print ("recipient: " + dct['recipient'])
		print ('-----')
		print ("value: " + str(dct['value']))
		print ('-----')
		print ("time: " + str(dct['time']))
		print ('-----')

'''
	# 各种客户进行的交易在系统中排队；矿工从该队列中提取交易并将其添加到区块中。然后他们将开采该区块，获胜的矿工将有特权将该区块添加到区块链中，从而为自己赚钱。
'''

'''
	# 为了创建一个队列，我们​​声明一个称为事务的全局列表变量
'''

transactions = []


'''
# 当实例化Client类时，将创建该客户端唯一的公钥和私钥。当Dinesh向Ramesh发送付款时，他将需要Ramesh的公钥，该公钥是通过使用客户端的identity属性获得的

Dinesh = Client()
Ramesh = Client()
t = Transaction(
   Dinesh,
   Ramesh.identity,
   5.0
)
# 创建事务对象之后，您将通过调用其sign_transaction方法对其进行签名。此方法以可打印格式返回生成的签名。我们使用以下两行代码生成并打印签名：

signature = t.sign_transaction()
print (signature) 

'''	

'''现在，我们将开始创建交易。首先，我们将创建四个客户，他们将互相汇款以从他人那里获得各种服务或商品。'''

# Dinesh = Client()
# Ramesh = Client()
# Seema = Client()
# Vijay = Client()

'''现在，我们开始如下的第一笔交易'''

# t1 = Transaction(
#    Dinesh,
#    Ramesh.identity,
#    15.0
# )
# t1.sign_transaction()
# transactions.append(t1)

# t2 = Transaction(
#    Dinesh,
#    Seema.identity,
#    6.0
# )
# t2.sign_transaction()
# transactions.append(t2)

# t3 = Transaction(
#    Ramesh,
#    Vijay.identity,
#    2.0
# )
# t3.sign_transaction()
# transactions.append(t3)

# t4 = Transaction(
#    Seema,
#    Ramesh.identity,
#    4.0
# )
# t4.sign_transaction()
# transactions.append(t4)

# t5 = Transaction(
#    Vijay,
#    Seema.identity,
#    7.0
# )
# t5.sign_transaction()
# transactions.append(t5)

# t6 = Transaction(
#    Ramesh,
#    Seema.identity,
#    3.0
# )
# t6.sign_transaction()
# transactions.append(t6)

# t7 = Transaction(
#    Seema,
#    Dinesh.identity,
#    8.0
# )
# t7.sign_transaction()
# transactions.append(t7)

# t8 = Transaction(
#    Seema,
#    Ramesh.identity,
#    1.0
# )
# t8.sign_transaction()
# transactions.append(t8)

# t9 = Transaction(
#    Vijay,
#    Dinesh.identity,
#    5.0
# )
# t9.sign_transaction()
# transactions.append(t9)

# t10 = Transaction(
#    Vijay,
#    Ramesh.identity,
#    3.0
# )
# t10.sign_transaction()
# transactions.append(t10)



'''因为每个块都需要前一个块的哈希值，所以我们声明一个名为last_block_hash的全局变量'''
last_block_hash = ''

class Block:
	"""一个区块由不同数量的交易组成"""
	def __init__(self):
		# 仅将经过验证的有效交易添加到该区块
		self.verified_transactions = []
		# 每个块还保存前一个块的哈希值，因此块链变得不可变
		self.previous_block_hash = ''
		# 最后，我们声明另一个名为Nonce的变量，用于存储矿工在采矿过程中创建的随机数
		self.Nonce = ''


''' 我们假设TPCoins的发起者最初将500 TPCoins分发给已知的客户端Dinesh '''

Dinesh = Client()
t0 = Transaction(
	'Genesis',
	Dinesh.identity,
	500.0)	

'''我们创建一个Block类的实例，并将其称为block0'''
block0 = Block()
'''我们将previous_block_hash和Nonce实例变量初始化为None，因为这是存储在区块链中的第一个事务。'''
block0.previous_block_hash = None
block0.Nonce = None

'''将上述t0事务添加到维护在该块内的verify_transactions列表中'''
block0.verified_transactions.append(t0)
'''
该区块已完全初始化，可以添加到我们的区块链中。我们将为此创建区块链。在将区块添加到区块链之前，我们将对区块进行哈希处理并将其值存储在我们先前声明的名为last_block_hash的全局变量中。该值将由下一个矿工在其区块中使用。
我们使用以下两行编码来哈希该块并存储摘要值。
'''
digest = hash(block0)
last_block_hash = digest

'''创建区块链'''

'''
 挖矿功能 
 为了启用挖掘，我们需要开发挖掘功能。挖掘功能需要在给定的消息字符串上生成摘要，并提供工作量证明。让我们在本章中对此进行讨论
'''

def sha256(message):
	return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message,difficulty=1):
	assert difficulty >= 1
	prefix = '1' * difficulty
	for i in range(1000):
		digest = sha256(str(hash(message))+str(i))
		if digest.startswith(prefix):
			print('after' + str(i) + 'iterations found nonce:' + digest)
		return digest

last_transaction_index = 0
block = Block()
for i in range(3):
	temp_transaction = transactions[last_transaction_index]
	# validate transaction
	# if valid
	block.verified_transactions.append (temp_transaction)
	last_transaction_index += 1

block.previous_block_hash = last_block_hash
block.Nonce = mine (block, 2)
digest = hash (block)
TPCoins.append (block)
last_block_hash = digest