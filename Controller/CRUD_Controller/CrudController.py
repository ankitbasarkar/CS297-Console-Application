import time
import sys
from View.CRUDAnalysisSpecView import CRUDAnalysisSpecView

class CRUDController:
    def __init__(self):
        self.renderCRUDOptions()
        self.getCRUDViewOptions()

    def renderCRUDOptions(self):
        CRUDView = CRUDAnalysisSpecView()
        CRUDView.renderView()

    def getCRUDViewOptions(self):
        Selection = raw_input("Please select a number/letter corresponding to the desired action.\n")
        self.handleCRUDViewOptions(Selection)

    def handleCRUDViewOptions(self,Selection):
        if (Selection == 'q' or Selection == 'Q'):
            print "Exiting System"
            from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
            RunningAnalysisProcesses.terminateAll()
            time.sleep(3)
            sys.exit()
        if (Selection == 'b' or Selection == 'B'):
            from Controller.Landing_Controller.LandingController import LandingController
            LandingControllerObj = LandingController()
        if (Selection == '1'):
            from Controller.CRUD_Controller.CreateSpecController import CreateSpecController
            createSpecController = CreateSpecController()
        else:
            self.renderCRUDOptions()
            self.getCRUDViewOptions()