from tkinter import *
from tkinter.scrolledtext import ScrolledText
from srcclass import *
from selenium import webdriver
class UI:
    def __init__(self,exct,excob,exc_str):
        self.okno = Tk()
        self.cr = crawler(exct,excob,self) # creating our crawler that looks for sites with the exceptions in them
        Label(text="Oops, seems like your code has crashed with this error statement:").pack()
        Label(text=exc_str).pack()
        Label(text = "Do you wish to search the internet for fixes?(Enter)").pack()
        file1 = open("Auto.txt","r")
        self.okno.bind("<Return>",self.big)
        self.didbig = False # if it searched
        self.gothelp = False # if it scraped the other websites
        self.btns = []
        self.autoopen = int(file1.read()) # saved user choice
        self.writetofile = IntVar() # the checkbox variable that gets turned on and off
        self.bigtext = ""
    def big(self,event):
        if(self.didbig==False):
            self.clearwidg()
            self.autocheckbox = Checkbutton(text = "Do you want to open the most upvoted site automatically next time? ",variable=self.writetofile, command=self.autopen)
            self.mainhelplabel = Label(text="Analyzing Websites...")
            self.mainhelplabel.pack()
            
            self.cr.main()
            self.pr("Websites Analyzed!")
            self.autocheckbox.pack()

            if(self.autoopen == 1):
                try:
                    self.browser = webdriver.Firefox()
                    self.browser.get(self.cr.sorted[0].url)
                except:
                    try:
                        self.browser = webdriver.Chrome()
                        self.browser.get(self.cr.sorted[0].url)
                    except: # in case there is no ideal site, meaning the stackoverflow website was not found
                        pass
            self.didbig = True
            self.pr("If you are not satisfied with your results. We can try to search other sites for reasonable thoughts. Do you wish to proceed?(Enter)")
            self.okno.bind("<Return>",self.gethelpbig)
            self.text_area = ScrolledText()

    def gethelpbig(self,event): # searching non_stackoverflow sites
        self.text_area.pack()
        if(self.didbig == True and self.gothelp == False): # prevents doing this a second time
            self.gothelp = True
            for z in self.cr.sites:
                z.gethelp()
            if(len(self.cr.sites)==0):
                print("No sites found")
        
        self.text_area.configure(state ='disabled')
            
    def pr(self,x): # prints text on the big helping label - works as a print or an error catcher
        self.mainhelplabel.config(text=x)
    def lbl(self,txt): # prints text to the ScrolledText so we can see what non-stackoverflow websites have for us
        self.text_area.insert(END, txt)
        self.text_area.insert(END, "\n")
    def clearwidg(self): # Used for better user experience
        for x in self.okno.winfo_children():
            x.destroy()
    def create_button(self,url,txt,vtc,slvd): # creating buttons as a class so that every single one has a different command
        self.btns.append(btn(self,url,txt,vtc,slvd))
    def autopen(self): # saves user decision on automating opening the first site
        if self.writetofile.get() == 1:
            file1 = open("Auto.txt","w")
            file1.write("1")
            file1.close()
        else:
            file1 = open("Auto.txt","w")
            file1.write("0")
            file1.close()
class btn:
    def __init__(self,ui,url,txt,votecount,slvd):
        self.ui = ui
        self.url = url
        self.votecount = votecount # votecount used for sorting
        self.solved = slvd # checking if its solved so we can sort it in UI
        if(self.solved == True):
         self.buttn = Button(text = txt + "\n ✔️", command=self.gotopage)
        else:
         self.buttn = Button(text = txt, command=self.gotopage)
    def gotopage(self): # the main command which opens our stackoverflow site
        try:
         self.ui.browser.get(self.url)
        except:
         try:
            self.ui.browser = webdriver.Firefox()
            self.ui.browser.get(self.url)
         except:
            self.ui.browser = webdriver.Chrome() # for chrome users in case they dont have firefox
            self.ui.browser.get(self.url)             
    def pak(self):
        self.buttn.pack()
