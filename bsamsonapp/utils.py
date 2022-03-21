def handle_uploaded_file(filePath, f):  
    with open(filePath, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    return filePath