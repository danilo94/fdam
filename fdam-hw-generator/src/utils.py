import sys
import re

if sys.version_info < (2, 7):
    import commands
else:
    import subprocess


# Begin Red color
def begin_red_fontcolor():
    print("\033[1;31m")


# End Red color
def end_red_fontcolor():
    print("\033[1;m")


# Begin Green color
def begin_green_fontcolor():
    print("\033[32;1m")


# End green color
def end_green_fontcolor():
    print("\033[0m")


def commands_getoutput(cmd):
    if sys.version_info < (2, 7):
        return commands.getoutput(cmd)
    else:
        byte_out = subprocess.check_output(cmd.split())
        str_out = byte_out.decode("utf-8")
        return str_out


def numBits(n):
    count = 1
    while n / 2 > 1:
        n = n / 2
        count = count + 1
    return count


def find_files(dir, typeFile, extensions):
    begin_green_fontcolor()
    print("Finding %s files ... " % typeFile)
    end_green_fontcolor()
    str_sim = ""
    for extn in extensions:
        str = commands_getoutput("find " + dir + " -type f -name *" + extn)
        if (len(str.strip()) != 0):
            print(str)
            for f in str.split('\n'):
                if (len(f) != 0):
                    aux = f.split('/')
                    ind = 0
                    for a in aux:
                        if a == "rtl":
                            break
                        ind = ind + 1
                    filename = ".."
                    for i in range(ind, len(aux)):
                        filename = filename + "/" + aux[i]
                    str_sim = str_sim + filename + "\n"
    return str_sim

def split_modules(str_modules,dir):
    modules = str_modules.split('endmodule')
    for m in modules:
        m = m.strip(' \n')
        if m.strip('\n') != '':
            name = m.split(' ')[1]
            name = re.sub('[\n\t()!#$%&*-+@=;:<>\/\[\{\}\]]','',name)
            with open(dir+'/%s.v'%(name),'w') as fm:
                m = m + '\n\nendmodule'
                fm.write(m)
    
    
    
    
    
    
    
    
    
    
    
    
