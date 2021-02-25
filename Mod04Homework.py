#Matthew Selakovich
#Mod04Homework

#imports
import os, getpass
#Make directories
the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)

#adding headers
with open('alert_data.csv','w') as matt:
        matt.write('Date,Time, Priority, Classification, Description, Source IP, Destination IP\n')
#Spliting data      
with open('alert.pcap', 'r') as data_file:
    for i in data_file:
                split1 = i.split('[**]')
                date_time = split1[0]           		#date/time
                attack_date = date_time[:5]     	#date
                attack_time = date_time[6:11]   	#time
                split2 = split1[1].split('] ')
                description = split2[1].strip() 		#description
                split3 = split1[2].split('] [')
                classification = split3[0]
                classification = classification.strip(' ,')
                classification = classification[16:] #classification
                priority=split3[1].split(']')
                priority=priority[0]
                startip=split3[1].split('->')
                destinationip=startip[1] #destinationip
                startip=startip[0].strip('] ')
                startip=startip[13:]    #Startip
                with open('alert_data.csv', 'a') as file:   #Posting data
                 file.write(attack_date +','+attack_time+','+priority+','+classification+
                 ','+description+','+startip+','+destinationip+'\n')
input()
    




