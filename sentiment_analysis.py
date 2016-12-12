import json
import numpy as np
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='47b0590d738c257ed994aba56cf8c42a8895daef')

f_read = open('CS181_comments.txt', 'r')
f_write = open('CS181_comments_sentiment.txt', 'w')

scores = []

for line in f_read:
	sentiment = alchemy_language.sentiment(text=line)['docSentiment']
	print line, sentiment
	if sentiment['type'] == 'neutral':
		score = 0
	else:
		score = sentiment['score']
	scores.append(score)
	f_write.write(line.strip('\n') + ', ' + str(score) + '\n')

float_scores = [float(score) for score in scores]
f_write.write("AVERAGE: " + str(np.mean(float_scores)))
