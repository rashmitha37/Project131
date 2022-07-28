import csv
import pandas as pd

#read data file
df = pd.read_csv("main.csv")
#df.drop(['Unnamed:0'],axis=1,inplace=True)

#radius = []
#mass = []



#print(df.dtypes)
#print(df.columns)

del df["Luminosity"]
del df["Unnamed: 0.1"]
del df["Unnamed: 0"]

df=df.dropna()

print(df.dtypes)
print(df.columns)

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = []

#converting measurements into SI units
def convert_to_si(radius, mass):
    for i in range(0, len(radius)-1):
        try:
            #converting mass into kilograms
            mass[i] = mass[i]*1.989e+30

            #converting radius into meters
            radius[i] = radius[i]*6.957e+8

        except:pass

convert_to_si(radius, mass)

#creating function to find gravity
def find_gravity(radius, mass):
    G = 6.67e-11
    #calculating gravity and adding it into gravity array
    for index in range(0, len(mass)):
        #print('about to read')
        try:
            g = (mass[index]*G)/((radius[index])**2)
            #print('read')
            gravity.append(g)
            
        except:pass

find_gravity(radius, mass)

print(len(gravity))
print(len(radius))
print(len(mass))


#merging gravity data with column
for i in gravity:
    df["Gravity"] = gravity[0:96]
print(df)

#creating new data file
df.to_csv('star_data_with_gravity.csv')

print(df.dtypes)