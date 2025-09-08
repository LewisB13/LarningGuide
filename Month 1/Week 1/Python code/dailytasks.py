dailylist = [" shave", "shower"]
print("current list ", dailylist)

task = input("please insert a task you wish to add to your list: ")
index = input("where in the list would you like to add this: ")
# index = (int(index)-1)

#print to correct location casting the index to a int then takign away 1
#so it matches where expexted unlike pcs list 0 is 1
dailylist.insert((int(index)-1), task)
print ("New List is ", dailylist)

