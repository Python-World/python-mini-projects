import hashlib
import os

def hashFile(filename):
    BLOCKSIZE=65536
    hasher=hashlib.md5()
    with open(filename,'rb') as file:
        buf=file.read(BLOCKSIZE)
        while(len(buf)>0):
            hasher.update(buf)
            buf=file.read(BLOCKSIZE)
    return hasher.hexdigest()




if __name__ == "__main__":
    hashMap={}
    deletedFiles=[]
    filelist=[f for f in os.listdir() if os.path.isfile(f)]
    for f in filelist:
        key=hashFile(f)
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashMap[key]=f
    if len(deletedFiles)==0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found')


