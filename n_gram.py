import numpy as np

def generate_ngrams(list,n):
	output = [list[i : i+n] for i in range(len(list)-n)]
	return output

def conditional_probability_bigram(text, ngrams):
	for i in ngrams:
		print("probability that ",i[0]," occurs given ",i[1]," is ",ngrams.count(i) / text.count(i[1]))
		print("probability that ",i[1]," occurs given ",i[0]," is ",ngrams.count(i) / text.count(i[0]))

def conditional_probability_ngram(text, ngrams):
	for i in ngrams:
		print("probability that _",i,"_ occurs  is ",ngrams.count(i) / len(ngrams))


with open("./sample_text.txt","r") as f:
	text= f.read()
	print(len(text))
	print(text.split("."))

	#counting the tokens
	tokens = text.split()
	
	#generate n-grams
	n = 3
	ngrams = generate_ngrams(tokens,n)
	print("these are the ngrams\n",ngrams)

	#calculating conditional probability
	print("\n now let us generate the conditional probability for each token in given the bigram \n")
	conditional_probability_ngram(text,ngrams)
