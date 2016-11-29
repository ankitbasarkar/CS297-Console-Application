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
        try:
            with open(self.Specification.Name+'.spec','wb') as outFile:
                pickle.dump(self.Specification,outFile)
        except IOError:
            print "\nDon't have permission to make changes to the working directory\n"
            print "Try changing working directory from the application or give permissions\n"
            print "HACK : Another workaround is run the application as administrator\n "

    def getSpecificationFilesinPWD(self):
        fileList = []
        PWDpath = os.getcwd()+Config.PathSeperator
        for f in os.listdir(PWDpath):
            if os.path.isfile(PWDpath+f):
                if f.endswith('.spec'):
                    fileList.append(f)
        return fileList


    def handleCreateSpecCommonOptions(self,Selection):
        if (Selection == 'q' or Selection == 'Q'):
            print "Exiting System"
            from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
            RunningAnalysisProcesses.terminateAll()
            time.sleep(3)
            sys.exit()
        if (Selection == 'b' or Selection == 'B'):
            from Controller.CRUD_Controller.CrudController import CRUDController
            crudController = CRUDController()
            return True


    def handleSpecName(self):
        SpecName = raw_input("Enter Name of Specification.\n")
        if self.handleCreateSpecCommonOptions(SpecName):
            # Return to previous call
            return True

        if (SpecName + '.spec' in self.getSpecificationFilesinPWD()):
            print "\n" \
                  "**********************************************" \
                  "\nSpecification with same name already exists\n" \
                  "**********************************************"
            time.sleep(1)
            self.renderCreateSpecOptions()
            return True
        else:
            self.Specification.Name = SpecName

    def handleSpecLocation(self):
        SpecLocation = raw_input("Enter location of the input data file.\n")
        if self.handleCreateSpecCommonOptions(SpecLocation):
            return True
        self.Specification.Location = SpecLocation

    def handleSpecML(self):
        count = 0
        for mlAlgo in Config.AvailableMLAlgorithms:
            print str(count) + " " + mlAlgo
            count = count + 1
        SpecMLAlgorithm = raw_input("Select the ML algorithm you want to implement.\n")
        if self.handleCreateSpecCommonOptions(SpecMLAlgorithm):
            return True
        try :
            SpecMLAlgorithm = int(SpecMLAlgorithm)
            if SpecMLAlgorithm in range(len(Config.AvailableMLAlgorithms)):
                self.Specification.MLAlgorithm = Config.AvailableMLAlgorithms[SpecMLAlgorithm]
            else:
                # Something else entered rather than Available ML algo indices
                print "\nInCorrect Selection made, Please select appropriate option\n"
                time.sleep(1)
                self.handleSpecML()
                return
        except:
            print "\nInCorrect Selection made, Please select appropriate option\n"
            time.sleep(1)
            self.handleSpecML()
            return

    def handleSpecScaling(self):
        SpecScaling = raw_input("Enter Scaling parameter for your Specification.\n")
        if self.handleCreateSpecCommonOptions(SpecScaling):
            return True
        self.Specification.Scaling = SpecScaling

    def handleSpecNormalization(self):
        SpecNormalization = raw_input("Enter Normalization parameter for your Specification.\n")
        if self.handleCreateSpecCommonOptions(SpecNormalization):
            return True
        self.Specification.Normalization = SpecNormalization

    def handleSpecFiltering(self):
        SpecFiltering = raw_input("Enter Filtering parameter for your Specification.\n")
        if self.handleCreateSpecCommonOptions(SpecFiltering):
            return True
        self.Specification.Filtering = SpecFiltering


    def handleCreateSpecOptions(self):
        if self.handleSpecName():
            return

        if self.handleSpecLocation():
            return

        if self.handleSpecML():
            return

        if self.handleSpecScaling():
            return

        if self.handleSpecNormalization():
            return

        if self.handleSpecFiltering():
            return

        print "\nSaving your Specification details\n"
        time.sleep(1)
        #This will save the specification
        self.saveSpecification()
        print "\n*************Specification Saved*************\n"
        time.sleep(1)










