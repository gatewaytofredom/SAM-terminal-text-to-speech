import os

while True:
    user_input = input()

    phrase = 0
    shit_counter = 0
    sam_output = [""]

    split_user_input = str.split(user_input," ")
    print(split_user_input)

    for word in split_user_input:

        print(str(word))
        #if it would excede the charecter buffer dont
        if (len(str(sam_output[phrase]) + str(word)) < 80):
            
            print(str(phrase) + " counter")
            print(str(shit_counter) + " shit_counter")

            #add next word to sam_output since it doesnt excede the char limit
            sam_output[phrase] = sam_output[phrase] +" " +str(word)
            shit_counter += 1
            
        else:
            sam_output.append(str(word))
            phrase += 1
            shit_counter += 1
            
    #speak each item in sam_output
    for phrasez in sam_output:
        print(str(phrasez))
        sam_command = 'sam.exe ' + str(phrasez)
        os.system('start /wait cmd /c '+sam_command)
            
