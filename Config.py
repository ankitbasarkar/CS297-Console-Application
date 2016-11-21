import os
import platform
class Config:
    AvailableMLAlgorithms = {}
    PathSeperator = ""
    # The below method is called just once to initialise the config static variables above
    @staticmethod
    def initialiseConfig():
        Config.AvailableMLAlgorithms = ['SVM Classification', 'SVM Regression', 'Naive Bayes', 'Logistic Regression']
        platformName = platform.system()
        if(platformName=='Windows'):
            Config.PathSeperator = "\\"
        else:
            Config.PathSeperator = "//"
        Config.PWDPath = os.getcwd()+Config.PathSeperator


