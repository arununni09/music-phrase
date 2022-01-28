
notes = ('s','r','g','m','p','d','n','*')

a = []

file1 = open('notes.csv','w')
for note1 in notes:
    for note2 in notes:
        for note3 in notes:
            a.append(note1+note2+note3)  
groups = []
for note in a:
    if note.count(note[0])>=3:groups.append(note)
file1.write(','.join(groups)+'\n') 

groups = []
main = []
for note in a:
    if note[0]==note[1] and not(note.count(note[0])>=3):groups.append(note)
main.append(groups[0])
for group in groups:
    if not group in main:
        if group[0] == main[-1][-1]:
            try:
                if group[-1] == notes[notes.index(group[0])+1]:
                    main.append(group)
            except:
                print('out')
                
file1.write(','.join(main)+'\n')         

            
file1.close()
