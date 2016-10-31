import sys
import string
import subprocess

#open the file, put it in a list
#split the list into smaller lists
#then bitch about life
def getplugs():
    fhandle = open('plugs.ini')
    plugins = fhandle.readlines()
    for plugin in plugins:
        plugin = plugin.replace("\n", "")
    return plugins

#checks if the plugin acutally exists
#calls each plugin specified
#writes the responce down in
#the file that the user set
def callandwrite(plugin, place):
    plugins = getplugs() #update this now
    flag = False #we need this for later
    for check in plugins: #check if the plugin is in the list we have
        if check.strip("\n") == plugin:
            flag = True
    if flag:
        #triming out the string so it is readable
        out = subprocess.getstatusoutput("python ./plugs/" + plugin)
        print(out[1])
        out = out[1].split("|||")
        #start working with the file
        fhandle = open(place + "&q.html", "a")#questions
        fhandle.write(out[0] + "\n<br><br><br>\n")
        fhandle.close()
        fhandle = open(place + "&a.html", "a")#answers
        fhandle.write(out[1]+ "\n<br><br><br>\n")
        fhandle.close()
        return
    else:
        print("Error findign the plugin.  (have you added it to plugs.ini?)")
        return

#write the header down
#nothing really else
def writeheader(place):
    headertext  = "<p>Name:__________________  Date:__\__\__</p>"
    headertext += "\n<!--I pitty da fool who think that mah files are xhtml compliant-->"
    fhandle = open(place + "&q.html", "a")#questions
    fhandle.write(headertext)
    fhandle.close()
    fhandle = open(place + "&a.html", "a")#answers
    fhandle.write(headertext)
    fhandle.close()

#parse the .ini files for each test.
#files are structured like this:
#1|quadratic.py,3
#2|solveforx.py,10
#3|pluginname.py,7
# the format is [pluginname],[number]
# the plugin name is before the comment,
# number of problems separated by a comma
# each set separated by a CR+LF, so don't
# fucking strip those from your ini.
def parseini(ini):
    fhandle = open(ini)
    out = fhandle.readlines()
    fhandle.close()
    return out # each line get split later, not here.  Don't hold your breath

def writefile(config, place):
    writeheader(place)
    counter = 1
    config = parseini(config)
    for problemset in config:
        problemset = problemset.strip("\n")
        problemset = problemset.split(",")
        i = 0
        while int(problemset[1]) >= i:
            problemnum = "<br>" + str(counter) + ".) "
            fhandle = open(place + "&q.html", "a")#questions
            fhandle.write(problemnum)
            fhandle.close()
            fhandle = open(place + "&a.html", "a")#answers
            fhandle.write(problemnum)
            fhandle.close()
            callandwrite(problemset[0], place)
            counter += 1
            i += 1
