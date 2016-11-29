import time
import sys
import os
from Config import Config
import pickle
from Model.AnalysisModel import AnalysisSpecification
from Controller.CRUD_Controller.CreateSpecController import CreateSpecController
from View.StartAnalysisView import StartAnalysisView
from ProcessPkg.AnalysisProcess import AnalysisProcess
from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses

class StartAnalysisController:
    def __init__(self):
        self.renderStartAnalysisOptions()
        self.getStartAnalysisOptions()

    def renderStartAnalysisOptions(self):
        STANALView= StartAnalysisView()
        STANALView.renderView()

    def getStartAnalysisOptions(self):
        Selection = raw_input("Please select a number/letter corresponding to the desired action.\n")
        self.handleStartAnalysisOptions(Selection)

    def getSpecificationFilesinPWD(self):
        fileList = []
        PWDpath = os.getcwd() + Config.PathSeperator
        for f in os.listdir(PWDpath):
            if os.path.isfile(PWDpath + f):
                if f.endswith('.spec'):
                    fileList.append(f)
        return fileList

    def handleCommonOptions(self, Selection):
        if (Selection == 'q' or Selection == 'Q'):
            print "Exiting System"
            from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
            RunningAnalysisProcesses.terminateAll()
            time.sleep(3)
            sys.exit()
        if (Selection == 'b' or Selection == 'B'):
            from Controller.Landing_Controller.LandingController import LandingController
            LandingControllerObj = LandingController()
            return True

    def wrongInputHandler(self):
        print "\nWrong Selection made Please Try Again\n"
        time.sleep(1)
        self.renderStartAnalysisOptions()
        self.getStartAnalysisOptions()

    def handleStartAnalysisOptions(self,Selection):
        if self.handleCommonOptions(Selection):
            return
        if (Selection == '1'):
            # Check first to see whether we have atleast some spec files or not
            if not self.getSpecificationFilesinPWD():
                print "No Specification Made"
                print "Returning"
                time.sleep(1)
                from Controller.Landing_Controller.LandingController import LandingController
                LandingControllerObj = LandingController()
                return

            # if we reached here that means we do have some specifications files with us
            print "\nHere are the list of analysis specifications to choose from\n"
            count = 0
            for file in self.getSpecificationFilesinPWD():
                print str(count) + " : " + file
                count+=1

            specSelected = raw_input("Please enter the corresponding number to load the specification\n")

            if self.handleCommonOptions(specSelected):
                return

            #Check Number entered
            try :
                specSelected = int(specSelected)
            except:
                self.wrongInputHandler()
                return

            # CHeck if in correct range
            # range taken is count + 1 because range(0) gives empty list
            if not specSelected in range(count+1):
                # chose number outside the limit of the specs we have
                self.wrongInputHandler()
                return

            FileName = self.getSpecificationFilesinPWD()[int(specSelected)]
            self.loadAndStart(FileName)
            return

            # if (Selection == '2'):
        #     from Controller.StartAnalysis_Controller.SelectAndStartAnalysis import SelectAndStartAnalysis
        #     STARTANAL = SelectAndStartAnalysis()
        else:
            self.wrongInputHandler()

    def loadAndStart(self, FileName):
        with open(FileName , 'r') as inFile:
            SpecFile = pickle.load(inFile)
            AnalysisProcessObj = AnalysisProcess(SpecFile)
            AnalysisProcessObj.start()
            RunningAnalysisProcesses.add(SpecFile.Name,AnalysisProcessObj)
        return
