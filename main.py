alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']


myAlphabet = input("Kirjoita aakkonen:")
numberOfA  = alphabets.index() #-funktiota tässä

## for-loop kirjainlistan läpikäymiseen
for alphabet in alphabets:
        if alphabet in alphabets:
                print(myAlphabet ,'on aakkosten',numberOfA,'.kirjain')
                break
        else:
                print(myAlphabet , 'ei kuulu aakkosiin')





