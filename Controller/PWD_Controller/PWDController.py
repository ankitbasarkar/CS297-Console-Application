import os
import time
import sys


class PWDController:
    def __init__(self):
        self.renderInitialOptions()
        self.handlePWD()

    def renderInitialOptions(self):
        print "MLPP: Create Specification Menu"
        print "At any point of time in this menu you can select the following options"
        print "These 2 characters are reserved for back and quit throughout the MLPP"
        print "B. Go Back to Previous Menu"
        print "Q. Press 'Q' to Exit"

    def handlePWDCommonOptions(self, Selection):
        if (Selection == 'q' or Selection == 'Q'):
            print "Exiting System"
            from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
            RunningAnalysisProcesses.terminateAll()
            time.sleep(3)
            sys.exit()
        if (Selection == 'b' or Selection == 'B'):
            from Controller.Landing_Controller.LandingController import LandingController
            landingControllerObj = LandingController()
            return True

    def handlePWD(self):
        PWD = raw_input("Enter/Specify the path you want to use as working directory")
        if self.handlePWDCommonOptions(PWD):
            return
        if not os.path.exists(PWD):
            print "\n" \
                  "**********************************************" \
                  "\n       Invalid Path Specified\n" \
                  "**********************************************"
            self.handlePWD()
            return
        else:
            os.chdir(PWD)
            print "\nWorking Directory Changed Successfully\n"
            print "Working Directory Changed to : "+os.getcwd() +" "+PWD
            time.sleep(1)
            from Controller.Landing_Controller.LandingController import LandingController
            landingControllerObj = LandingController()
            return


