import datetime
import os


class ListOfFilesInDirectory():
    def _takeCurrentDatatimeStamp(self):
        ct = datetime.datetime.now()
        ts = ct.timestamp()
        tsStr = str(ts).split(".")[0]
        return tsStr

    def _createFileName(self, outputDirectory, fileName):
        """creates files name in user's chosen directory and adding currrent timestamp to file's name"""
        currentDatatimeStamp = ListOfFilesInDirectory._takeCurrentDatatimeStamp(self)
        fullFileName = r"%s\%s_%s.txt" % (outputDirectory, fileName, currentDatatimeStamp)
        return fullFileName

    def _createFilesList(self, inputDirectory, filesFormats):
        """create list of files in listed formats in given directory"""
        listOfFiles = ""
        formatList = []
        # removing "." from user given list of files formats and covering them to lowercase
        for f in filesFormats:
            listedFormat = f.replace(".", "").lower()
            formatList.append(listedFormat)
        for path, subdirs, files in os.walk(inputDirectory):
            for name in files:
                format = name.split(".")[-1].lower()
                if format in formatList or len(filesFormats) == 0:
                    listOfFiles = listOfFiles + name + "\n"

        return listOfFiles

    def saveFilesListToFile(self, inputDirectory, outputDirectory, fileName, filesFormats):
        """creates list of files and saves it to a file"""
        finalFileName = ListOfFilesInDirectory._createFileName(self, outputDirectory, fileName)
        filesList = ListOfFilesInDirectory._createFilesList(self, inputDirectory, filesFormats)
        # saving to file
        file = open(finalFileName, "w", encoding="utf-8")
        file.write(filesList)
        file.close()
        print(filesList)
