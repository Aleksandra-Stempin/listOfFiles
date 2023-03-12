import ClassListOfFilesInDirectory

inputDirectory = r"C:\Users\Olenka\Documents\ebooks"
# inputDirectory = r"E:\books"
# inputDirectory = r"E:\download"
outputDirectory = r"C:\Users\Olenka\Desktop"
fileName = "Ola_list_of_books"
filesFormats = ["epub", "mobi", "pdf", "acsm"]
filesFormats = [".EPUB",  ".mObi", "PDF", "acsm"]

lf = ClassListOfFilesInDirectory.ListOfFilesInDirectory()
lf.saveFilesListToFile(inputDirectory=inputDirectory
                       ,outputDirectory=outputDirectory
                       ,fileName=fileName
                       ,filesFormats = filesFormats)