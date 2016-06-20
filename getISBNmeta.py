import isbntools
#using isbntools
def getIMeta(query):
    
    print query
    isbn = app.isbn_from_words(query)    
    
        
    if isbn != None:
        meta=isbntools.app.meta(isbn)
        author=str(meta['Authors'][0])
        title=str(meta['Title'])
        fileName = author+" - "+title
        return [fileName,meta]
    else:
        return "Query Failed"