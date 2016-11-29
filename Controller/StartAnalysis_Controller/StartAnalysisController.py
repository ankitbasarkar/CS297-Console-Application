import time
import sys
from Controller.CRUD_Controller.CreateSpecController import CreateSpecController
from View.StartAnalysisView import StartAnalysisView

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

    def handleStartAnalysisOptions(self):
        if (Selection == 'q' or Selection == 'Q'):
            print "Exiting System..."
            time.sleep(3)
            sys.exit()
        if (Selection == 'b' or Selection == 'B'):
            from Controller.Landing_Controller.LandingController import LandingController
            LandingControllerObj = LandingController()
        if (Selection == '1'):
            CRSPECTRL = CreateSpecController()
            print "Here are the list of analysis specifications to choose from"
            CRSPECTRL.getSpecificationFilesinPWD()
        if (Selection == '2'):
            from Controller.StartAnalysis_Controller.SelectAndStartAnalysis import SelectAndStartAnalyis
            STARTANAL = SelectAndStartAnalyis()
        else:
            self.renderStartAnalysisOptions()
            self.getStartAnalysisOptions()

