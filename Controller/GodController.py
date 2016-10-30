import time
import sys
from View.LandingView import LandingView
from View.CRUDAnalysisSpecView import CRUDAnalysisSpecView as CRUDspecView
from Controller.CrudController import CRUDController
from View.StartAnalysisView import StartAnalysisView
class GodController:
    def __init__(self):
        self.renderFirstPage()
        self.getLandingViewOptions()

    def renderFirstPage(self):
        landingView = LandingView()
        landingView.renderLandingView()

    def getLandingViewOptions(self):
        Selection = raw_input("Please select a number/letter corresponding to the desired action.\n")
        self.handleLandingViewOptions(Selection)

    def handleLandingViewOptions(self,Selection):
        if(Selection=='1'):
            CRUDSV = CRUDController()
        if(Selection=='q'or Selection=='Q'):
            print "Exiting System"
            time.sleep(3)
            sys.exit()
        else:
            self.renderFirstPage()
            self.getLandingViewOptions()




