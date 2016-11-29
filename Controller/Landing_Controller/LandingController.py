import time
import sys
from View.LandingView import LandingView
from View.CRUDAnalysisSpecView import CRUDAnalysisSpecView as CRUDspecView
from View.StartAnalysisView import StartAnalysisView

from Controller.CRUD_Controller.CrudController import CRUDController
from Controller.StartAnalysis_Controller.StartAnalysisController import StartAnalysisController
from Controller.TerminateAnalysis_Controller.TerminateAnalysisController import TerminateAnalysisController
from Controller.PWD_Controller.PWDController import PWDController

class LandingController:
    def __init__(self):
        self.renderFirstPage()
        self.select = self.getLandingViewOptions()

    def renderFirstPage(self):
        landingView = LandingView()
        landingView.renderLandingView()

    def getLandingViewOptions(self):
        Selection = raw_input("Please select a number/letter corresponding to the desired action.\n")

        self.handleLandingViewOptions(Selection)

    def handleLandingViewOptions(self,Selection):

        if(Selection=='q'or Selection=='Q'):
            print "Exiting System..."
            from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
            RunningAnalysisProcesses.terminateAll()
            time.sleep(3)
            sys.exit()

        if (Selection == '1'):
            CRUDSV = CRUDController()

        if(Selection == '2'):
            STARTANAL = StartAnalysisController()

        if(Selection=='3'):
            STOPANAL = TerminateAnalysisController()

        if(Selection=='4'):
            PWDObj = PWDController()

        # The code below will get executed regardless of which option was selected
        self.renderFirstPage()
        self.getLandingViewOptions()





