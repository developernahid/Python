from cmath import sqrt
def mean(data):
    return sum(data) / len(data)

data = [1, 2, 3, 4, 5]
mean_val = mean(data)
print(f"Manual Mean: {mean_val}")
sum=0
for i in data:
   sum= sum+(i-mean_val)**2
p=sum/len(data)
population=sqrt(p)
x=len(data)-1
q=sum/x
sample=sqrt(q)

#standard deviation
print(population)
print(sample)
