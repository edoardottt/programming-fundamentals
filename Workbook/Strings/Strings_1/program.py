def es30(fname1,fname2,fname3):
    '''
    Create the function es30(fname1,fname2,fname3) that takes as input the paths 
    of three txt files.
    The first file contains an encoded message where each character has been replaced 
    by a three-digit character.
    All no-numeric chars have to be transferred as they are.
    In the second file it's possible to retrieve the matches numbers-characters 
    between numbers of text and the respective char.
    More precisely this file is organizeb by rows, in each row there are a char 
    and a three-digit integer that matches it into the separated txt file 
    by at least one space.
    Different numbers can refer to the same char and not all the numbers that
    appears in fname1 necessarily have to be in decode-file.
    The function es30 have to decode the message present in the first file due
    to second file's info.
    The numbers not present in the second file have to be decoded with '?' symbol.
    The decoded message have to be stored in the third file.
    The funcion finally returns the number of decoded chars with the '?' value
    in the decoded file.
    E.g:
    - the file fname1 contains the text '991118991991345      103    091027003091103?'
    - the file fname2 contains the text 'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 '
    the decoded text to be registered into file3 will be: 'tutt? a n?nna?'
    and the function returns the number 2.
    You can assume that the numeric chars always appear grouped by three.
    '''
    encoded_text = extract_encoded_text(fname1)
    decoder_dict = build_decoder_dict(fname2)
    result = 0
    decoded_text = ''
    j = 0
    while j < len(encoded_text):
        aggiungi = True
        if encoded_text[j] == '?':
            decoded_text+='?'
        elif encoded_text[j].isalpha():
            decoded_text+=encoded_text[j]
        elif encoded_text[j] == ' ':
            decoded_text+=' '
        elif encoded_text[j].isnumeric():
            value = encoded_text[j] + encoded_text[j+1] + encoded_text[j+2]
            j+=3
            aggiungi = False
            if value in decoder_dict:
                decoded_text += decoder_dict[value]
            else: 
                decoded_text+='?'
                result +=1
        else: decoded_text+=encoded_text[j]
        if aggiungi: j+=1
    decoded_text+=' '
    decoded_text = decoded_text[:-1]
    print(decoded_text)
    with open(fname3,'w') as f:
        f.write(decoded_text)
    return result

def extract_encoded_text(fname1):
    with open(fname1) as f:
        text = f.read()
    return text

def build_decoder_dict(fname2):
    with open(fname2) as f:
        text = f.readlines()
    dict = {}
    for elem in text:
        c=''
        v=''
        for char in elem:
            if char!='\n':
                if char.isalpha():
                    c = char
                elif char.isnumeric():
                    v+=char
        dict[v] = c
    return dict