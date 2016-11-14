import os
import platform
class Config:
    AvailableMLAlgorithms = {}
    PWDPath = ""
    PathSeperator = ""
    @staticmethod
    def initialiseConfig():
        Config.AvailableMLAlgorithms = {'SVM Classification', 'SVM Regression', 'Naive Bayes', 'Logistic Regression'}
        platformName = platform.system()
        if(platformName=='Windows'):
            Config.PathSeperator = "\\"
        else:
            Config.PathSeperator = "//"
        Config.PWDPath = os.getcwd()+Config.PathSeperator


