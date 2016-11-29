import time,sys
from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
from ProcessPkg.AnalysisProcess import AnalysisProcess
class TerminateAnalysisController:
    def __init__(self):
        self.renderTerminateAnalysisOptions()
        self.getTerminateAnalysisOptions()

    def renderTerminateAnalysisOptions(self):
        print "MLPP: Terminate An Analysis"
        print "1. List all Currently Running Analyses"
        print "B. Go Back to Previous Menu"
        print "Q. Press 'Q' to Exit"

    def getTerminateAnalysisOptions(self):
        Selection = raw_input("Please select a number/letter corresponding to the desired action.\n")
        self.handleTerminateAnalysisOptions(Selection)

    def handleCommonOptions(self,Selection):
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
        self.renderTerminateAnalysisOptions()
        self.getTerminateAnalysisOptions()
        return


    def handleTerminateAnalysisOptions(self,Selection):
        if self.handleCommonOptions(Selection):
            return
        if (Selection == '1'):
            # Check first to see whether we have atleast some spec files or not
            if not RunningAnalysisProcesses.RunningProcessesDict:
                print "No Running Analysis"
                print "Returning"
                time.sleep(1)
                from Controller.Landing_Controller.LandingController import LandingController
                LandingControllerObj = LandingController()
                return

            # if we reached here that means we do have some Analysis running
            print "\nHere are the list of running analysis specifications to choose from\n"
            count = 0
            for SpecName in RunningAnalysisProcesses.RunningProcessesDict.keys():
                print str(count) + " : " + SpecName
                count += 1

            specSelected = raw_input("Please enter correct Specification Name to stop the Analysis\n")

            # if the user entered back or quit options that is 'b' or 'q'
            if self.handleCommonOptions(specSelected):
                return



            # Check if spec entered exists in the dictionary of active Process List
            if not specSelected in RunningAnalysisProcesses.RunningProcessesDict:
                # Entered spec list that is not in active processes dictionary
                self.wrongInputHandler()
                return

            # If reached here that means we have an active process which we need to terminate
            SpecAnalysisProcessHandle = RunningAnalysisProcesses.RunningProcessesDict[specSelected]
            SpecAnalysisProcessHandle.terminate()
            RunningAnalysisProcesses.remove(specSelected)