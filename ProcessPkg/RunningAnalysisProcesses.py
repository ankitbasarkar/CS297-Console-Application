import pickle
class RunningAnalysisProcesses:
    RunningProcessesDict = dict()

    @staticmethod
    def getRunningProcessesDict():
        try:
            with open('RunningProcesses', 'r') as inFile:
                RunningAnalysisProcesses.RunningProcessesDict = pickle.load(inFile)
        except:
            pass
        return RunningAnalysisProcesses.RunningProcessesDict
    @staticmethod
    def add(AnalysisName,ProcessHandle):
        RunningAnalysisProcesses.RunningProcessesDict[AnalysisName] = ProcessHandle
        return
    @staticmethod
    def remove(AnalysisName):
        del RunningAnalysisProcesses.RunningProcessesDict[AnalysisName]
        return

    @staticmethod
    def terminateAll():
        for specSelected in RunningAnalysisProcesses.RunningProcessesDict.keys():
            SpecAnalysisProcessHandle = RunningAnalysisProcesses.RunningProcessesDict[specSelected]
            SpecAnalysisProcessHandle.terminate()