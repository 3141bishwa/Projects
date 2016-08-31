import random
import string

class CaesarCipher(object):
	def __init__(self):
		self._key = random.randint(1,26) 
		print self._key

	def wordEncoderAndDecoder(self, word, isEncoder):
		if isEncoder:
			shift = self._key
		else:
			shift = 26 - self._key
		return "".join(
				[(chr((ord(letter) + shift)/123*97 + (
					ord(letter) + shift) % 123)) if letter in string.ascii_lowercase else chr(
						(ord(letter) + shift)/91*65 + (ord(letter) + shift) % 91) for letter in word])

	def encode(self, message):
		words = message.split(" ")
		
		self.encoded_message = " ".join([self.wordEncoderAndDecoder(word, True) for word in words])
		
		print "The message has been encoded. Here it is: %s " % self.encoded_message
		self.encoded = True

	
	def decode(self):
		if not self.encoded:
			raise Exception("Encode your message first: ")

		decoded_words = self.encoded_message.split(" ")
		print "The Decoded Message: %s " % " ".join([self.wordEncoderAndDecoder(word, False) for word in decoded_words])

cipher = CaesarCipher()

message = raw_input("Enter a Message: ")


cipher.encode(message)
cipher.decode()

