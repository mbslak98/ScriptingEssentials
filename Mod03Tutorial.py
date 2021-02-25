#Matthew Selakovich
#Mod02Tutorial
song1 =[]
song2=[]
song3=[]
lyrics_string=("Quisiera:Ayer:cambiarle:conocí:el:un:final"
               ":cielo:al:sin:cuento|Las:sol|Y:barras:un:y"
               ":hombre:los:sin:tragos:suelo|Un:han:santo:"
               "sido:en:testigo|De:prision|Y:el:una:dolor:"
               "canción:que:triste:me:sin:causaste:dueño|Y:"
               "y:conocí:to':tus:lo:ojos:que:negros|Y:hiciste"
               ":ahora:conmigo|Un:sí:infeliz:que:en:no:el:"
               "puedo:amor,:vivir:que:sin:aun:ellos:no:yo|"
               "Le:te:pido:supera|Que:al:ahora:cielo:camina"
               ":solo:solo:un:sin:deseo|Que:nadie:en:por:tus"
               ":todas:ojos:las:yo:aceras|Preguntándole:pueda"
               ":a:vivir|He:Dios:recorrido:si:el:en:mundo:verdad"
               ":entero|te:el:vengo:amor:a:existe|:decir|")
#Task 1
lyrics= lyrics_string.split(':')

#Task 2
for i in range(0, len(lyrics),2):
    song1.append(lyrics[i])
    song2.append(lyrics[i+1])
                 
#Task 3
    song1_print=''.join(song1)
    
#Task 4
    song1_print=' '.join(song1)
    song1_print=song1_print.replace('|','\n')
    print(song1_print)
#Task 5
    song2_print = ' '.join(song1)
    song2_print= song2_print.replace('|','\n')
    print(song1_print.strip())
    
#Task 6
    print('\nWords that are in both songs: ')
    for j in range(len(song1)):
        try:
            if song1[j] in song2:
                if song1[j] not in song3:
                    song3.append(song1[j])
        except:
            continue
#Task 7
    for m in range(len(song3)):
        print(song3[m])

    input()
                                


