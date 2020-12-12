
# Function: Generate all crifan ebook list
# Author: Crifan Li
# Update: 20201212
# Latest: https://github.com/crifan/crifan_ebook_readme/blob/master/allEbookList/generateAllBookList.py

import re
import codecs

################################################################################
# Config
################################################################################

################################################################################
# Util Functions
################################################################################

def uniqueList(oldList):
    """remove overlapped item in the list"""
    # newList = []
    # for x in oldList:
    #     if x not in newList:
    #         newList.append(x)
    newSet = set(oldList)
    newList = list(newSet)
    return newList

def loadTextFromFile(fullFilename, fileEncoding="utf-8"):
    """load file text content from file"""
    with codecs.open(fullFilename, 'r', encoding=fileEncoding) as fp:
        allText = fp.read()
        # logging.debug("Complete load text from %s", fullFilename)
        return allText

def saveTextToFile(fullFilename, text, fileEncoding="utf-8"):
    """save text content into file"""
    with codecs.open(fullFilename, 'w', encoding=fileEncoding) as fp:
        fp.write(text)
        fp.close()

################################################################################
# Const & Config & Settings
################################################################################

InputMdFile = "README.md"
OutputMdFile = "AllCrifanEbookList.md"

################################################################################
# Main
################################################################################

mdStr = loadTextFromFile(InputMdFile)
# print("mdStr=%s" % mdStr)

# * [Notepad++](http://www.crifan.com/files/doc/docbook/rec_soft_npp/release/html/rec_soft_npp.html)
allDocbookUrlList = re.findall("https?://www\.crifan\.com/files/doc/docbook/\w+/release/html/\w+.html", mdStr)
docbookTotalNum = len(allDocbookUrlList)
print("docbookTotalNum=%s" % docbookTotalNum) # 113
uniqueDocbookUrlList = uniqueList(allDocbookUrlList)
uniqueDocbookUrlList.sort()
uniqueDocbookUrlTotalNum = len(uniqueDocbookUrlList)
print("uniqueDocbookUrlTotalNum=%s" % uniqueDocbookUrlTotalNum) # 56

# * [VSCode](http://book.crifan.com/books/best_editor_vscode/website)
allGitbookUrlList = re.findall("https?://book\.crifan\.com/books/\w+/website", mdStr)
allGitbookNameTotalNum = len(allGitbookUrlList)
print("allGitbookNameTotalNum=%s" % allGitbookNameTotalNum) # 139
uniqueGitbookUrlList = uniqueList(allGitbookUrlList)
uniqueGitbookUrlList.sort()
uniqueGitbookUrlTotalNum = len(uniqueGitbookUrlList)
print("uniqueGitbookUrlTotalNum=%s" % uniqueGitbookUrlTotalNum) # 74

allDockbookMdStr = "\n    * ".join(uniqueDocbookUrlList)
allGitbookMdStr  = "\n    * ".join(uniqueGitbookUrlList)

allBookMdStr = """
* crifan所有电子书列表
  * docbook
    * %s
  * gitbook
    * %s
""" % (allDockbookMdStr, allGitbookMdStr)

saveTextToFile(OutputMdFile, allBookMdStr)