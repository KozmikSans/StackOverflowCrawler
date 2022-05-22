from Page import *

def search(query): # searches the ask web and returns an array of urls. Using ask because googlesearch library no longer works reliably
    usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    srch = requests.get('https://www.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q='+query,headers=usr_agent).text
    resultcode= BeautifulSoup(srch,'lxml')
    results = resultcode.find_all('a',class_='PartialSearchResults-item-title-link result-link') # objects
    lnks = []
    for x in results:
        lnks.append(x.attrs['href']) # taking the href from attrs dict
    return lnks

class crawler:
    def __init__(self,exctype,excobj,UI):
        self.excobj=excobj
        self.exctype = exctype
        self.stacksites = []
        self.urls = []
        self.language = "python"
        self.sites = []
        self.ui = UI
    def main(self): # the program...
        print("Analyzing Websites...")
        srchquery = "stackoverflow.com" + '+'+self.language +'+'+ self.exctype.__name__+':'+str(self.excobj)
        self.urls = search(srchquery) # search internet for exception
        for x in self.urls:
            IsOverFlow = False
            domain =  x.split('/') # splitting to get domain words
            for q in domain:
                if(q == 'stackoverflow.com'): # checking for stackoverflow pages
                    IsOverFlow = True
            if IsOverFlow: # creates an object and sends it to the right list
                pg = stackoverflowsite(x,self.exctype,self.ui)
                if(pg.valid==True):
                 self.stacksites.append(pg)
            else:
                pg=site(x,self.exctype,self.ui)
                if(pg.valid==True):
                 self.sites.append(pg)

        
        for y in self.stacksites: # getting stacksite data
            y.gethelp()
        try:  # prevents crashes if there are no stackoverflow pages
            highest = self.ui.btns[0]
        except:
            self.ui.mainhelplabel.config(text="No StackOverflow Websites were found")
        self.sorted = []

        while(len(self.ui.btns)>0): # this creates a list sorted by votecounts
            highest = self.ui.btns[0]
            for z in self.ui.btns:
                if(z.votecount >= highest.votecount):
                    highest = z
            if(highest.votecount == 0): # used for sorting the solved sites with 0 votes
                for z in self.ui.btns:
                    if(z.solved == True):
                        highest = z
            self.sorted.append(highest)
            self.ui.btns.remove(highest)
             
        for b in self.sorted:
            b.buttn.pack()
            b.buttn.wait_visibility()
