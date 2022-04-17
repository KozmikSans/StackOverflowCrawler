# StackOverflowCrawler
A simple python crawler that searches up stackoverflow posts based on your exception.

Ok thats the easy explanation. I will now further elaborate on how it works(Its not complex):
I take the exception of our except block and search the exception name in Ask(googlesearch library does not work reliably so i just coded my own simple search method). Then I scrape the search results and sort them into objects of either stackoverflow pages or normal pages. After that I sort the stackoverflow pages by upvotes(the most upvoted help) and create tkinter buttons(these buttons open up the browser with the url) in the right order. Then I also check if the stackoverflow pages are solved so i can tell the user.  
That's the stackoverflow pages...

For each paragraph in a normal page, I check for keywords like error/issue etc. and then i just put the paragraph inside a tkinter textbox(obviously only if it has the keywords). I didn't expect it at first, but turns out it works somehow.

The entire UI is done in tkinter. Scraping is done with bs4 and requests. Opening pages is done with selenium.
However you need firefox or chrome to start it up. I will probably add something for other browsers as well...
