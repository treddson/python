from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I think that this is going to be ok")

print(res)