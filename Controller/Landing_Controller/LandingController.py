import time
import sys
from View.LandingView import LandingView
from View.CRUDAnalysisSpecView import CRUDAnalysisSpecView as CRUDspecView
from Controller.CRUD_Controller.CrudController import CRUDController

from View.StartAnalysisView import StartAnalysisView
class GodController:
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
        if(Selection=='1'):
            CRUDSV = CRUDController()
        if(Selection=='q'or Selection=='Q'):
            print "Exiting System"
            time.sleep(3)
            sys.exit()
        if(Selection=='2'):
            pass
            # Krithika working on start Analysis
            # StartAnalysis = StartAnalysis()

        # The below part of code will get executed regardless of which option was selected
        self.renderFirstPage()
        self.getLandingViewOptions()





