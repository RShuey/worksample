from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import main

#window for the main stuff
class mainwindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        #some variables for later
        self.questionselection = (0, 0)
        self.pluginselection = (0, 0)

        self.title("Math Problem Generator")

        #menus
        self.mainmenu = Menu(self)

        #file
        self.file = Menu(self.mainmenu, tearoff=0)
        self.file.add_command(label = "Save", command = self.savefile)
        self.file.add_command(label = "Open", command = self.openfile) #changed from open to openfile due to name conflicts
        self.mainmenu.add_cascade(label = "File", menu = self.file)

        #Edit
        self.edit = Menu(self.mainmenu)
        self.edit.add_command(label = "Add Questions", command = self.addquestionprompt)
        self.edit.add_command(label = "Edit Questions", command = self.editquestionprompt)
        self.edit.add_command(label = "Delete Questions", command = self.deletequestionprompt)
        self.edit.add_command(label = "Generate Questions", command = self.generatequestions)
        self.mainmenu.add_cascade(label = "Edit", menu = self.edit)

        #Plugins
        self.plugins = Menu(self.mainmenu)
        self.plugins.add_command(label = "View plugins", command = self.pluginmenu)
        self.plugins.add_command(label = "Add plugin", command = self.addplugin)
        self.mainmenu.add_cascade(label = "Plugins", menu = self.plugins)

        self.config(menu=self.mainmenu)

        #main box
        self.questionlist = Listbox(self)
        self.questionlist.insert(1, "blank.py,1")
        self.questionlist.pack()
        self.questionlist.bind('<<ListboxSelect>>', self.updateselection)
        self.questionlist.activate(0)

        self.mainloop()

    #save file
    #compile all of the table into one long list
    #write the file with spaces and stuff
    #hope to god memory doesn't kill you
    def savefile(self):
        fhandle = filedialog.asksaveasfile()
        out = ""
        for line in self.questionlist.get(0, END):
            out += line + "\n"
        out += "blank.py,1"
        fhandle.write(out)
        fhandle.close()
    #open file
    #get the file handle
    #clear the table
    #read the lines into the page
    def openfile(self):
        self.questionlist.delete(0, END)
        fhandle = filedialog.askopenfile()
        questions = fhandle.readlines()
        for question in questions:
            question = question.replace("\n", "")
            self.questionlist.insert(END, question)
        self.questionlist.pack()
        fhandle.close
    #add question prompt
    #just go and append a blank command at the end
    #command format [plugin].py,[number of questions]
    def addquestionprompt(self):
        self.questionlist.insert(END, "blank.py,1")
        self.questionlist.pack()
    #edit question prompt
    #make a list of the plugins and the slider
    #have the slider and the listbox(?) update the programs variables
    #note to self: listbox can update on command (kinda) with listboxselect, use it retard
    def editquestionprompt(self):
        self.editmenu = Toplevel(master=self)
        self.problemcount = Scale(self.editmenu, to=10, command=self.updateproblem)
        self.problemcount.grid()
        self.pluginlist = Listbox(self.editmenu)
        self.pluginlist.bind('<<ListboxSelect>>', self.updateproblemplugin)
        self.pluginlist.grid()
        
        
        fhandle = open('plugs.ini')
        plugins = fhandle.readlines()
        for plugin in plugins:
            plugin = plugin.replace("\n", "")
            self.pluginlist.insert(END, plugin)
        fhandle.close()
        self.pluginlist.grid()
    #delete question prompt
    #just go into the listbox, and remove the selected element
    def deletequestionprompt(self):
        selected = self.questionlist.curselection()
        self.questionlist.delete(selected[0], selected[-1])
    #generate questions prompt
    #get the file name that they want and then the name to save as
    #run writefile from main
    #?????????
    #profit
    def generatequestions(self):
        openname = filedialog.askopenfilename()
        savename = filedialog.asksaveasfilename()
        main.writefile(openname, savename)
    #plugin menu
    #just copypasta what you made in the edit question prompt
    #ditch the slider, you don't need it
    def pluginmenu(self):
        self.pluginmenu = Toplevel(master=self)
        self.pluginMlist = Listbox(self.pluginmenu)
        
        fhandle = open('plugs.ini')
        plugins = fhandle.readlines()
        for plugin in plugins:
            plugin = plugin.replace("\n", "")
            self.pluginMlist.insert(END, plugin)
        fhandle.close()
        self.pluginMlist.grid()
    #add plugin menu
    #get the file name of what they are adding
    #split the actual name itself off
    #read the file
    #cross your fingers and hope memory doesn't kill you
    #write the file down elsewhere
    #add the name to plugs.ini
    #note to self: does opening the file in A mode auto add a cr+lf?
    def addplugin(self):
        toadd = filedialog.askopenfilename()
        toaddname = toadd.replace('\\', "/")
        toaddname = toaddname.split("/")
        fhandle = open(toadd)
        out = fhandle.read(999)#you knever know what you might get
        fhandle.close
        fhandle = open('plugs/' + toaddname[-1], 'w')
        fhandle.write(out)
        fhandle.close()
        fhandle = open('plugs.ini', 'a')
        #fhandle.write("\n" + toaddname[-1]) ????????
        fhandle.write(toaddname[-1])
        fhandle.close()
    #update problemset
    #When the slider is slid, update what is in the listbox
    #seems complex, but nothing to big in reality
    #Note to self: REMEMBER THAT YOU CAN ACCESS THIS STUFF BETWEEN MENUS
    def updateproblem(self, number):
        #build string to update
        out = self.pluginlist.get(self.pluginselection[0]) + "," + str(number)
        #get selected problem, and update it
        self.questionlist.delete(self.questionselection)
        self.questionlist.insert(self.questionselection, out)
    #update the problem selected
    #do the same as above but with the special thingy that listbox uses
    def updateproblemplugin(self, number):
        self.pluginseletion = self.pluginlist.curselection()
        #build string to update
        out = self.pluginlist.get(self.pluginselection[0]) + "," + str(self.problemcount.get())
        #get selected problem, and update it
        self.questionlist.delete(self.questionselection)
        self.questionlist.insert(self.questionselection, out)
    #update questionselection
    #update the variable we have made up there for use in the above two functions
    def updateselection(self, number):
        self.questionselection = self.questionlist.curselection()[0]

mainwindow()
