from fastapi import FastAPI, HTTPException
import schemas

app = FastAPI()

library = {}

@app.get("/books/")
def getBooks():
    catalog = []
    for book in library.values():
        catalog.append(book)
    if catalog:
        return catalog
    else:
        raise HTTPException(status_code=404, detail="Library is empty.")


@app.get("/books/{id}")
def getBook(id:int):
    if id in library.keys():
        return library[id]
    else:
        raise HTTPException(status_code=404, detail="Book not found.")
    

@app.post("/books/")
def addBook(book:schemas.Book):
    newId = len(library.keys()) +1
    book.id = newId
    library[newId] = book
    return library[newId]

@app.put("/books/{id}")
def updateBook(id:int, book:schemas.Book):
    if id in library.keys():
        book.id = id
        library[id] = book
    else:
        raise HTTPException(status_code=404, detail="Book not found.")


@app.delete("/books/{id}")
def deleteBook(id:int):
    if id in library.keys():
        del library[id]
    else:
        raise HTTPException(status_code=404, detail="Book not found.")
