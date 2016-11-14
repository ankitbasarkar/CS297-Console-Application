import time
import sys
import pickle
import os
from Config import Config
import sys

from Model.AnalysisModel import AnalysisSpecification
class CreateSpecController:
    def __init__(self):
        self.Specification = AnalysisSpecification()
        self.renderCreateSpecOptions()

    def renderCreateSpecOptions(self):
        from View.CreateSpecView import CreateSpecView
        CSView = CreateSpecView()
        CSView.renderInitialOptions()
        self.handleCreateSpecOptions()

    def saveSpecification(self):
        with open(self.Specification.Name+'.spec','wb') as outFile:
            pickle.dump(self.Specification,outFile)

    def getSpecificationFilesinPWD(self):
        fileList = []
        PWDpath = Config.PWDPath
        for f in os.listdir(PWDpath):
            if os.path.isfile(PWDpath+f):
                if f.endswith('.spec'):
                    fileList.append(f)
        return fileList


    def handleCreateSpecCommonOptions(self,Selection):
        if (Selection == 'q' or Selection == 'Q'):
            print "Exiting System"
            time.sleep(3)
            sys.exit()
        if (Selection == 'b' or Selection == 'B'):
            from Controller.CrudController import CRUDController
            crudController = CRUDController()
            return True

    def handleSpecName(self,SpecName):
        # Name for Specification provided
        if (SpecName + '.spec' in self.getSpecificationFilesinPWD()):
            print "\n" \
                  "**********************************************" \
                  "\nSpecification with same name already exists\n" \
                  "**********************************************"
            self.renderCreateSpecOptions()
            return True
        else:
            self.Specification.Name = SpecName


    def handleCreateSpecOptions(self):
        SpecName = raw_input("Enter Name of Specification.\n")
        if self.handleCreateSpecCommonOptions(SpecName):
            return
        if self.handleSpecName(SpecName):
            return

        SpecLocation = raw_input("Enter location of the input data file.\n")
        if self.handleCreateSpecCommonOptions(SpecLocation):
            return
        self.Specification.Location = SpecLocation

        count = 0
        for mlAlgo in Config.AvailableMLAlgorithms:
            print str(count) + " "+ mlAlgo
            count = count+1
        SpecMLAlgorithm = raw_input("Select the ML algorithm you want to implement.\n")
        if self.handleCreateSpecCommonOptions(SpecMLAlgorithm):
            return
        self.Specification.MLAlgorithm = SpecMLAlgorithm






