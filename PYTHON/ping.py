import subprocess

# empty list that will store ping results
ping_result = "\n\n"
#ping size can be adjusted by changing the number here"(["ping", "-c 2", address])"
with open('./servers.text') as f:
        for line in f:
            address = line.strip("\n")

            res = subprocess.call(["ping", "-c 2", address])
            if res == 0:
                ping_result = ping_result + "ping to " + address + " OK" + " \n"
            elif res == 2:
                ping_result = ping_result + "no response from " + address + " \n"
            else:
                ping_result = ping_result + "ping to " + address + " failed!" + " \n"

#python3
print (ping_result)

#python2
#print ping_result

with open('./servers.text') as i, open('./nslookup.csv', 'w') as o:
   for line in i:
     if line.strip(): # skips empty lines
        proc = subprocess.Popen(["nslookup", line.strip()],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        o.write('{}\n'.format(proc.communicate()[0]))

print('Done')