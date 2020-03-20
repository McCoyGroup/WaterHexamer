import numpy as np
import struct
wfns=[]
weights=[]

skip_ws = lambda data, b=4: data.read(b)
get_int = lambda a: struct.unpack("i", a)[0]
read_int = lambda data: get_int(data.read(4))
get_float = lambda ag: struct.unpack("d", ag)[0]
read_float = lambda datag: get_float(datag.read(8))
read_float_block = lambda data, nblocks: np.frombuffer(data.read(8*nblocks), dtype=float)
#fstrings
#list of files
files=['d2o6_book','d206_prism','d206_cage','h2o_d2o5_book','h2o_d2o5_prism','h2o_d2o5_cage','h2o5_d2o_book','h2o5_d2o_prism','h2o5_d2o_cage','h2o6_book','h206_prism','h206_cage','sample']


#numberofsets=1
count=0
numbersum=0
for file in files:
    data = open(f"NickFiles/VictorData/{file}/{file}_coords.dat", "rb")
    weightfile = open(f"NickFiles/VictorData/{file}/{file}_weight.dat", "r")
    skip_ws(data)
    numberofsets = read_int(data)
    print(file)
    print(numberofsets)
    for x in range(0,numberofsets):
        # skip_ws(data, 2)
        count=count+1
        wfns=[]
        read_int(data);
        read_int(data)
        number=read_int(data)
        initialwalkers= read_int(data)
        time=read_float(data)
        # print(read_int(data))
        # print(read_int(data))
        # print(read_float(data))
        # print(read_float(data))
        # read_int(data);
        # read_int(data)
        # print(read_float_block(data, 54))
        for x in range(0, number):
            # print(read_int(data))
            # print(read_int(data))
            # print(read_float_block(data, 54))
            read_int(data)
            read_int(data)
            wfns.append(read_float_block(data, 54))
        wfns=np.array(wfns)
        newwfns=np.reshape(wfns,(number,18,3))
        # wfnsx=wfns[:,0::3]
        # wfnsy=wfns[:,1::3]
        # wfnsz=wfns[:,2::3]
        # print(newwfns)
        #filename='SampleCoords/'+str(count)+'NumWalkers'+str(number)+'InitialWalkers'+str(initialwalkers)+'Time'+str(int(time))
        # print(filename)
        #np.save(filename,newwfns)
        #Weights file:
        weightfile.readline()
        weights=[]
        for x in range(0, number):
            weights.append(weightfile.readline())
            weights[x] = weights[x].strip()
            weights[x] = np.double(weights[x])

        numbersum=numbersum+number

        np.savez(f'NickFiles/VictorData/{file}/PythonData/{file}{str(count)}',coords=newwfns,weights=weights,time=time,NumWalkers=number,InitialWalkers=initialwalkers)
        #weightsname='SampleCoords/'+str(count)+'NumWalkersWeights'+str(number)
        #np.save(weightsname, weights)
        #print(weights)

# oranges=weights.readline()
# print(oranges)
#
#         print(type(weights[0]))
#np.concatonate
#np.save
#np.load
# print(struct.unpack("i",weights.read(4)))
# read_int(data);read_int(data)
# print(read_int(data))
# print(read_int(data))
# print(read_float(data))
# # print(read_float(data))
# read_int(data);read_int(data)
# print(read_float_block(data, 54))
# for x in range(0,199,1):
#     print(read_int(data))
#     print(read_int(data))
#     print(read_float_block(data, 54))

#np.loadtext




