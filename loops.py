#List: Data structure whcih can hold multiple values of multiple type
#Arrays: Data structure whcih can hold multiple values of same type
#list start from 0
list_of_cloud = ["AWS", "Azure", "GCP", "Ali baba", "oracle cloud", "didgital ocean", "utho"]
print(list_of_cloud)

#adding new cloud to list
list_of_cloud.append("salesforce") #append-- add at the end of list 
list_of_cloud.append("IBM")
print(list_of_cloud)

list_of_cloud.insert(2,"horiku")
print(list_of_cloud)

list_of_cloud.insert(0, "ocean")
print(list_of_cloud)

print(len(list_of_cloud)) #len of list

#Iterate the list
for cloudlist in list_of_cloud:
    print(" ")
    print(cloudlist)
    #print(" ")

for i in range(0,10):
    print(i)
    #print("Hello Affu")
