# Matthew Selakovich
#ScriptingProject1

#imports
import copy,os,getpass,zipfile, shutil
        
tuplelist=('ATTACK-RESPONSES',
 'BAD-TRAFFIC', 'CHAT IRC', 'COMMUNITY WEB',
 'DNS SPOOF', 'ET ACTIVEX', 'ET CHAT IRC',
 'ET CNC', 'ET CURRENT_EVENTS', 'ET DNS',
 'ET EXPLOIT', 'ET INFO', 'ET MALWARE', 'ET P2P',
 'ET POLICY', 'ET SCAN', 'ET SHELLCODE', 'ET TROJAN',
 'ET USER_AGENTS', 'ET WEB_CLIENT', 'ET WEB_SERVER',
 'ET WEB_SPECIFIC_APPS', 'GPL', 'ICMP', 'INFO',
 'MS-SQL', 'MULTIMEDIA', 'P2P', 'POLICY', 'SCAN',
 'WEB-ATTACKS', 'WEB-CGI', 'WEB-CLIENT', 'WEB-FRONTPAGE',
 'WEB-IIS', 'WEB-MISC', 'WEB-PHP')

#Functions

#Menu Function
def menu ():
        print(' ')
        print('---- MAIN MENU ---- ')
        print(' ')
        print('Please select from the following options: ')
        print('1. Parse alert data ')
        print('2. Major descriptors ')
        print('3. Classifications ')
        print('4. Clean up and exit ')
        print(' ')
        print(' ')
        return
#Menu Function 1: Parse Alert Data
def Parsing():
    print('Please be patient. Parsing data...')
    counter=0
    with open('alert.full.maccdc2012_cleaned.csv', 'w') as matt:
        matt.write('Date,Time,Priority,Classification,Description,Packet Type,Source IP,Source Port,Destination IP,Destination Port,\n')
        
    with open('alert.full.maccdc2012.pcap', 'r') as line:
        for i in line:
            counter += 1
            if '[**]' in i:
                split1=i.split('[**]')
                description= split1[0]
                finaldescript= description[11:].strip()
            elif 'Classification' in i:
                split2=i.split('] [')
                classification=split2[0][1:]
                prior=split2[1].split(']')
                priority=prior[0]
            elif '/' and '->' in i:
                split4=i.split('->')
                destin_IP=split4[1][1:]
                destin_Port=split4[1][15:]
                split7=i.split(':')
##                destin_Port=split7[4]
                source_IP=split4[0][22:]
                source_Port=split4[0][36:]
                split5=i.split('-')
                date=split5[0]
                split6=i.split('.')
                time=split6[0][6:]
##                try:
##                   split9=split5[1].split(':')
##                except:
##                    source_IP = split5[1]
##                    continue
##                source_IP = split9[0]
##                try:
##                    source_Port = split9[1]
##                except:
##                    source_Port='unspecified'
            elif 'DgmLen' in i:
                split8=i.split(':')
                packet_type=split8[0][:-4]
            elif '\n' in i:
                with open('alert.full.maccdc2012_cleaned.csv', 'a') as written:
                    written.write(date+','+time+','+priority+','+classification+','+finaldescript+','+packet_type+','+source_IP+','+source_Port+','+destin_IP+','+destin_Port)
            else:
                menu()
                continue
                
            
   
#Menu Function 2: Major Descriptors
def descriptors():
    descriptors=copy.deepcopy(tuplelist)
    if os.path.exists('alert.full.maccdc2012_cleaned.csv'):
        print(' ')
    else:
        print('Parse alert data first using choice 1 from the main menu.')
        return
    while True:
        userlist=[]
        print('''
        Enter one or more starting characters for your major descriptor, or
        Enter nothing to see all major descriptors, or
        Enter 'exit' to return to the main menu:
        ''')
        userchoice=input()
        userchoice.upper()
        if userchoice == 'exit':
            break
        else:
            for x in range(0, len(descriptors)):
                letters=descriptors[x].split()
                userchoice=letters[0]
                if userchoice.startswith(userchoice.title()):
                    userlist.append(descriptors)
                    print(userlist)
##                else:
##                    print('No major descriptor was found with those starting characters. Please try again.')
##                    break
                    
#Menu Function 3: Classifications
def classifications():
    filelinecounter= 0
    classlist=[]
    if os.path.exists('alert.full.maccdc2012_cleaned.csv'):
        print(' ')
    else:
        print('Parse alert data first using choice 1 from the main menu.')
        return
    with open('alert.full.maccdc2012_cleaned.csv') as classi:
        next(classi)
        for y in classi:
            filelinecounter += 1
            split3=y.split(',')
            classification=split3[0]
            counter2='not found'
            for d in classlist:
                if classification == d[0]:
                    if classification == 'tcp':
                        d[1]+=1
                    elif classification=='udp':
                        d[2]+=1
                    elif classification == 'icmp':
                        d[3]+=1
                    counter2= 'found'
                elif counter2== 'not found':
                    classlist.append(classification[:])
                    classlist[-1] = classlist + [0,0,0]
                    if classification =='tcp':
                        classlist[-1][1]+=1
                    elif classification=='udp':
                        classlist[-1][2]+=1
                    elif classification=='icmp':
                        classlist[-1][3]+=1
        classlist.sort()
        for t in classlist:
            packs=(count(len(classlist)))/counter
            multiply= int(packs *10000)
            divide= multiply/100
            print(classlist[0])
            print(sum(classlist[0]))
            if divide == 0:
                print('it comprises less than .01% of all alerts')
            else:
                print('it comprises ' +divide + '% of alerts')
                        
    
    
#Menu Function 4: Clean up and exit
def cleanup():
   os.chdir(the_desktop)
   shutil.move('alert.full.maccdc2012.pcap','.\\Selakovich\\Matthew')
   shutil.move('alert.full.maccdc2012_cleaned.csv','.\\Selakovich\\Matthew')
   new_zip=zipfile.ZipFile('Selakovich.zip','w')
   listdir =os.listdir('Selakovich\\Matthew')
   new_zip.write('Selakovich\\Matthew\\alert.full.maccdc2012_cleaned.csv',compress_type=zipfile.ZIP_DEFLATED)
   new_zip.write('Selakovich\\Matthew\\alert.full.maccdc2012.pcap',compress_type=zipfile.ZIP_DEFLATED)
   new_zip.close()
   shutil.rmtree('Selakovich')
   exit()
    
    

#Main Body Code:

#Name strings
    
MY_NAME= 'Matthew Selakovich'
Split_Name= MY_NAME.split()
First_Name=Split_Name[0]
Last_Name=Split_Name[1]

#Active Desktop Path

the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)
ADP= the_desktop+'\\'+Last_Name+'\\'+First_Name

#Student Directory

if os.path.exists(ADP):
    os.rmdir(ADP)
    os.makedirs(ADP)
else:
    os.makedirs(ADP)
    
#Data file check
    
if os.path.exists(the_desktop+'\\'+'alert.full.maccdc2012.zip'):
    unzip=zipfile.ZipFile('alert.full.maccdc2012.zip')
    unzip.extractall()
    unzip.close
else:
    print('File is not there please restart program and place file in desktop.')
    exit()
    
#Menu Start
    
while True:
    menu()
    userselection= int(input())
    if userselection == 1:
        Parsing()
    elif userselection == 2:
        descriptors()
    elif userselection == 3:
        classifications()
    elif userselection == 4:
        cleanup()
    else:
        print('Invalid option try again, choose a number from the menu.')
