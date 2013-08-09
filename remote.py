import subprocess as sub

currentremote = ""

def getcommands(name):
    p = sub.Popen('irsend LIST '+name+' ""',stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    return output

if __name__=="__main__":
    print getcommands("SamsungRemote")