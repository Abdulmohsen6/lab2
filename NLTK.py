import nltk
text = "if you have an error just go to Dr Nayyar to fix it "
sentence = nltk.sent_tokenize(text)
for sent in sentence:
	 print(nltk.pos_tag(nltk.word_tokenize(sent)))