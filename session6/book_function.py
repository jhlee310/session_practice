def extract_info(book_list):
    result = []
    for book in book_list:
        title = book.find("a", {"class" : "N=a:bta.title"}).string
        img_src = book.find("div", {"class" : "thumb_type thumb_type2"}).find("img")["src"]
        link = book.find("a", {"class" : "N=a:bta.title"})["href"]
        author = book.find("dd", {"class" : "txt_block"}).find("a").string.strip()
        publisher = book.find("dd", {"class" : "txt_block"}).find("a", {"class" : "N=a:bta.publisher"}).string

        if book.find("em", {"class" : "price"}) != None:
            price = book.find("em", {"class" : "price"}).string
        else:
            price = "X"
        
        book_info = {
            "title" : title,
            "img_src" : img_src,
            "link" : link,
            "author" : author,
            "publisher" : publisher,
            "price" : price
        }

        result.append(book_info)
    return result


        

