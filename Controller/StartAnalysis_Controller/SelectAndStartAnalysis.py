import time
import sys
from Config import Config

from Controller.CRUD_Controller.CreateSpecController import CreateSpecController
from Model.AnalysisModel import AnalysisSpecification

class SelectAndStartAnalysis:
    def __init__(self):
        self.Specification = AnalysisSpecification()
        self.renderSelectAndStartAnalysisOptions()

    def renderSelectAndStartAnalysisOptions(self):
        ListOfAnalysisSpecFiles = []
        CRSPECTRL = CreateSpecController()
        ListOfAnalysisSpecFiles = CRSPECTRL.getSpecificationFilesinPWD()
        print (ListOfAnalysisSpecFiles)
        spec = raw_input("From the list above, please type in an analysis specification you want to choose")
        if spec not in ListOfAnalysisSpecFiles:
            print "Error! Incorrect choice."
        else:
            self.Specification.Name = spec




