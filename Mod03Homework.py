#Matthew Selakovich
#Mod03Homework
import copy

#lists

name_list = ['Constance Castillo', 'Kerry Goodwin',
 'Dorothy Carson', 'Craig Williams', 'Daryl Guzman', 'Sherman Stewart',
 'Marvin Collier', 'Javier Wilkerson', 'Lena Olson', 'Claudia George',
 'Erik Elliott', 'Traci Peters', 'Jack Burke', 'Jody Turner',
 'Kristy Jenkins', 'Melissa Griffin', 'Shelia Ballard', 'Armando Weaver',
 'Elsie Fitzgerald', 'Ben Evans', 'Lucy Baker', 'Kerry Anderson',
 'Kendra Tran', 'Arnold Wells', 'Anita Aguilar', 'Earnest Reeves',
 'Irving Stone', 'Alice Moore', 'Leigh Parsons', 'Mandy Perez',
 'Rolando Paul', 'Delores Pierce', 'Zachary Webster', 'Eddie Ward',
 'Alvin Soto', 'Ross Welch', 'Tanya Padilla', 'Rachel Logan',
 'Angelica Richards', 'Shelley Lucas', 'Alison Porter', 'Lionel Buchanan',
 'Luis Norman', 'Milton Robinson', 'Ervin Bryant', 'Tabitha Reid',
 'Randal Graves', 'Calvin Murphy', 'Blanca Bell', 'Dean Walters',
 'Elias Klein', 'Madeline White', 'Marty Lewis', 'Beatrice Santiago',
 'Willis Tucker', 'Diane Lloyd', 'Al Harrison', 'Barbara Lawson',
 'Jamie Page', 'Conrad Reynolds', 'Darnell Goodman', 'Derrick Mckenzie',
 'Erika Miller', 'Tasha Todd', 'Aaron Nunez', 'Julio Gomez',
 'Tommie Hunter', 'Darlene Russell', 'Monica Abbott', 'Cassandra Vargas',
 'Gail Obrien', 'Doug Morales', 'Ian James', 'Jean Moran',
 'Carla Ross', 'Marjorie Hanson', 'Clark Sullivan', 'Rick Torres',
 'Byron Hardy', 'Ken Chandler', 'Brendan Carr', 'Richard Francis',
 'Tyler Mitchell', 'Edwin Stevens', 'Paul Santos', 'Jesus Griffith',
 'Maggie Maldonado', 'Isaac Allen', 'Vanessa Thompson', 'Jeremy Barton',
 'Joey Butler', 'Randy Holmes', 'Loretta Pittman', 'Essie Johnston',
 'Felix Weber', 'Gary Hawkins', 'Vivian Bowers', 'Dennis Jefferson',
 'Dale Arnold', 'Joseph Christensen', 'Billie Norton', 'Darla Pope',
 'Tommie Dixon', 'Toby Beck', 'Jodi Payne', 'Marjorie Lowe',
 'Fernando Ballard', 'Jesse Maldonado', 'Elsa Burke', 'Jeanne Vargas',
 'Alton Francis', 'Donald Mitchell', 'Dianna Perry', 'Kristi Stephens',
 'Virgil Goodwin', 'Edmund Newton', 'Luther Huff', 'Hannah Anderson',
 'Emmett Gill', 'Clayton Wallace', 'Tracy Mendez', 'Connie Reeves',
 'Jeanette Hansen', 'Carole Fox', 'Carmen Fowler', 'Alex Diaz',
 'Rick Waters', 'Willis Warren', 'Krista Ferguson', 'Debra Russell',
 'Ellis Christensen', 'Freda Johnston', 'Janis Carpenter', 'Rosemary Sherman',
 'Earnest Peters', 'Kelly West', 'Jorge Caldwell', 'Moses Norris',
 'Erica Riley', 'Ray Gordon', 'Abel Poole', 'Cary Boone',
 'Grant Gomez', 'Denise Chapman', 'Vernon Moran', 'Ben Walker',
 'Francis Benson', 'Andrea Sullivan', 'Wayne Rice', 'Jamie Mason',
 'Jane Figueroa', 'Pat Wade', 'Rudy Bates', 'Clyde Harris',
 'Andre Mathis', 'Carlton Oliver', 'Merle Lee', 'Amber Wright',
 'Russell Becker', 'Natalie Wheeler', 'Maryann Miller', 'Lucia Byrd',
 'Jenny Zimmerman', 'Kari Mccarthy', 'Jeannette Cain', 'Ian Walsh',
 'Herman Martin', 'Ginger Farmer', 'Catherine Williamson', 'Lorena Henderson',
 'Molly Watkins', 'Sherman Ford', 'Adam Gross', 'Alfred Padilla',
 'Dwayne Gibson', 'Shawn Hall', 'Anthony Rios', 'Kelly Thomas',
 'Allan Owens', 'Duane Malone', 'Chris George', 'Dana Holt',
 'Muriel Santiago', 'Shelley Osborne', 'Clinton Ross', 'Kelley Parsons',
 'Sophia Lewis', 'Sylvia Cooper', 'Regina Aguilar', 'Sheila Castillo',
 'Sheri Mcdonald', 'Lynn Hodges', 'Patrick Medina', 'Arlene Tate',
 'Minnie Weber', 'Geneva Pena', 'Byron Collier', 'Veronica Higgins',
 'Leo Roy', 'Nelson Lopez']


names = copy.deepcopy(name_list)

#Menu
def menu ():
        print(' ')
        print('Please select from the following options: ')
        menu='''
        1. List all first name beginning with a chose letter 
        2. List all last names beginning with a chosen letter 
        3. Add a name 
        4. Delete a name
        5. Exit
        '''
        print(' ')
        print(menu)
        print(' ')
        return
#lookup option
def lookup ():
    first_name= input()
    first_name.upper()
    for x in range(0, len(names)):
        letter=names[x][0]
        while first_name.startswith(letter):
            counter=0
            counter += 0
            print(names[x]) 
            if counter == (names):
                print('no names found for that letter')
            else:
                break
#lookup by last name
def lookuplast():
    last_name= input()
    last_name.upper()
    for i in range(0, len(names)):
        letters=names[i].split()
        first_name=letters[0]
        last_names=letters[1]
        if last_names.startswith(last_name.title()):
            print(last_names  +', ' + first_name)
#adding a name    
def adding ():
    print(' ')
    print('Enter the new first name: ')
    useraddf = input()
    print(' ')
    print('Enter the new last name: ')
    useraddl= input()
    useraddname= useraddf +' '+ useraddl
    propname=useraddname.title()
    names.append(propname)
    print(' ')
    print(propname + ' has been added. ')
#deleting a name    
def delete ():
    userdelete= input()
    try:
        names.remove(userdelete.title())
        print(' ')
        print(userdelete.title() + ' has been removed ')
    except:
        print('That name was not found')
    
#Main body
while True:
    menu()
    print('Option #: ')
    user_option= int(input())
#Option 1
    if user_option== 1:
        print('What letter does the first name begin with? ')
        lookup()            
#Option 2
    elif user_option == 2:
        print('What letter does the last name begin with? ')
        lookuplast()
#Option 3
    elif user_option == 3:
        adding()
#Option 4   
    elif user_option == 4:
        print('Enter the full name to delete: ')
        delete()
#Option 5   
    elif user_option == 5:
        exit()
#Else
    else:
        print('That is not a valid option. Please try again. ')



