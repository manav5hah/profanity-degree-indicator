from profanity_check import predict_prob
f = open('demofile.txt')
print("Profanity Degree:")
print(100 - predict_prob([f.read()])[0]*100)