import os
filepathn = os.path.join('data', 'datanasa.txt')
filenasa = open(filepathn, 'r')  #file variabe for the nasa file

filepathc= os.path.join('data', 'clean_data.csv')
mungefile= open(filepathc, 'w')   # new csv file

listoflines= filenasa.readlines()    # a list of strings with each line of the nasa file
secondy= 0  # variable to count the second time we encounter the character 'Y'
indextocut=0   # variable to hold the index of the second time 'Y' is encountered in the column heading line
temp =''
for i in listoflines:
    strippedstring= i.strip()   # removing the '\n' and any trailing and leading spaces 
    if len(strippedstring)==0:   # condition to skip the empty lines
        continue
    elif strippedstring[0] == 'Y' and secondy== 0:   # used only for one time
        index = 0                #variable to hold the index of the next character, is being used to evade the ',' after the last required character
        for n in strippedstring:
            index += 1
            indextocut +=1
            if n =='Y' and secondy==0:
                mungefile.write(n)
                secondy += 1
            elif n =='Y' and secondy==1:
                break
            else:
                if n == " ":
                    if strippedstring[index + 1] == 'Y':
                        break
                    if strippedstring[index].isalnum() == True:
                        mungefile.write(',')
                    else:
                        continue
                else:
                    mungefile.write(n)
            
    elif strippedstring[0] =='1' or strippedstring[0]=='2':   # condition for all the lines with the required data
        for n in range(0,indextocut-1):
            if strippedstring[n].isspace() == True:    #condition to check for space and add ','
                if strippedstring[n+1].isalnum() == True or strippedstring[n+1] == '-' or strippedstring[n+1] == '*':
                    mungefile.write(',')
                else:
                    continue
            else:
                if n < 4:
                    mungefile.write(strippedstring[n])
                else:
                    nostar = strippedstring[n].replace('*', '')  # file specific: the missing data is not required
                    if strippedstring[n] == '*':
                        continue
                    else:
                        temp += nostar
                        if strippedstring[n+1].isspace() == True:
                            print(n)
                            tempint = int(temp)
                            final = round(((tempint * 1.8)/100),1)
                            mungefile.write(str(final))
                            temp=''
        
    else:       #condition to skip any line that doest start with 'y' or numbers 1 and 2                 
        continue
    mungefile.write('\n')    # adding a new line at the end of each string(line of data) that is parsed
    
    
            
            