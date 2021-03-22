import matplotlib.pyplot as plt 
MA= ["16", "17", "16", "19", "15", "16", "20", "19"] #Mean age of mother
MMR= [14, 21, 21, 19, 20, 16, 17, 18] #Maternal Mortality Rate rounded up to the nearst whole number
x=MA
y=MMR

plt.title ("Mean Age of Motherhood and Maternal Mortality Rates")
plt.xlabel("Mean Age of Motherhood")
plt.ylabel("Maternal Mortality Rate")
plt.bar(MA,MMR)
plt.show()



