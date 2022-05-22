import requests
from bs4 import BeautifulSoup

class site: # basic site
    def __init__(self,url,exc,ui):
        self.valid = True
        self.ui = ui
        try: # prevents timeout stuff
            pg = requests.get(url).text
        except:
            print("Couldn't make contact")
            self.valid = False
            return
        self.exc_type = exc
        self.code = BeautifulSoup(pg,'lxml')
        self.url = url
    def getpars(self): # gets site paragraphs
        paragraphs = self.code.find_all('p')
        return paragraphs
    def gethelp(self): # searches for paragraphs using keywords and prints source
        parag = self.getpars()
        if(len(parag)>0): # only if the page has something to say
            self.ui.lbl('A page says this:')
            self.ui.lbl("Source:" + self.url) 
        for x in parag:
            sortlst = x.text.split(' ')
            IsHelp = False
            for w in sortlst: # keywordscan
                if(w=='error' or w=='solve' or w==self.exc_type.__name__ or w=='problem'):
                    IsHelp = True
                    break
            if IsHelp:       
                self.ui.lbl(x.text.strip())

class stackoverflowsite(site):
    def __init__(self,*args,**kwargs):
        super(stackoverflowsite, self).__init__(*args, **kwargs)
        self.votecount = 0 # the amount of votes, it only applies to stackoverflow sites but a reference is needed
        self.vcounts = []
    def gethelp(self): # figures out the site type and gets results
        rightans = self.code.find_all('div',class_='answer js-answer accepted-answer') 
        for w in rightans: # use forloop to prevent crashing
            self.votecount = int(w.find('div',class_='js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title').attrs['data-value'])
            self.ui.create_button(self.url,"Found a solved thread mentioning your exception here, "+"with an upvote count of: "+ str(self.votecount),self.votecount,True)
        if(len(rightans)==0): # sorting out the unsolved
            for c in self.code.find_all('div', class_ = 'js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title'):
                self.vcounts.append(int(c.attrs['data-value']))
            greatest = self.vcounts[0]
            for n in self.vcounts:
                if(n>greatest):
                    greatest=n
            self.ui.create_button(self.url,"Found an unsolved thread here, with the most upvoted comment having " + str(greatest) + " upvotes",greatest,False)



