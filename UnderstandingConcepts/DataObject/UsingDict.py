__author__ = 'kikita'



# define sanitize function
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins,secs) = time_string.split(splitter)
    return(mins + '.' + secs)


# define top3 times function
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        # Make the txt file to a dictionary
        return({'Name':templ.pop(0),
                'DOB':templ.pop(0),
                'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})

    except IOError as ioerr:
        print('File Error'+str(ioerr))
        return(None)


# execute function and print result
james = get_coach_data('james2.txt')
print(james['Name'] + "'s fastest times are:"+ james['Times'])







'''
sarah = Athlete('Sarah Sweeney','2002-6-17',['2:58','2.58','1.56'])
james = Athlete('James Jones')

print(Athlete),
print type(Athlete)

print(sarah),
print type(sarah)

print(james),
print type(james)


a = Athlete()
b = Athlete()
c = Athlete()
d = Athlete()
'''