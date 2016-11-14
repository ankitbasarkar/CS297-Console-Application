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
        if (Selection == '1'):
            pass
        if (Selection == 'q' or Selection == 'Q'):
            print "Exiting System"
            time.sleep(3)
            sys.exit()
        if (Selection == 'b' or Selection == 'B'):
            from Controller.GodController import GodController
            godController = GodController()
        if (Selection == '1'):
            from Controller.CreateSpecController import CreateSpecController
            createSpecController = CreateSpecController()
        else:
            self.renderCRUDOptions()
            self.getCRUDViewOptions()