# Converts EID tag bucket files as sent through by Nordic Star
# to a format that is read OK by the TruTest system

f=open('tag_bucket.txt','r')
f_out=open('tag_bucket_output.txt','w')
for line in f.readlines():
    data = line.split(',')
    man = int(data[0][4:-9],16)
    tag = int(data[0][7:],16)
    f_out.write("982 " + str(tag).zfill(12) + ',' + data[1] + "\n")
f.close()
