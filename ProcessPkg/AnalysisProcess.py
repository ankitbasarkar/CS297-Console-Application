import time
from multiprocessing import Process
from Model.AnalysisModel import AnalysisSpecification
from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
from APIHandlers.APICaller import APICaller
class AnalysisProcess:
    def __init__(self,SpecFile):
        self.Name = SpecFile.Name
        self.MLAlgorithm = SpecFile.MLAlgorithm
        self.Scaling = SpecFile.Scaling
        self.Location = SpecFile.Location
        self.Normalization = SpecFile.Normalization
        self.Filtering = SpecFile.Filtering
        self.pHandle = Process(target=self.run)

    def run(self):
        # Whatever You want to do runs in over here
        # Below is the example run method that illustrates run over multiple methods
        #Example run starts below
        # print self.Name + " Started\n"
        # count = 0
        # while True:
        #     with open(self.Name,'w') as out:
        #         out.write(str(count))
        #     time.sleep(2)
        #     count+=2
        # Example Run end

        # The below static call will handle the calls for different api
        APICaller.apiCall(self.Name,self.MLAlgorithm,self.Scaling,self.Location,self.Normalization,self.Filtering)





    def start(self):
        self.pHandle.start()

    def terminate(self):
        print "Terminating Process : "+ self.Name
        self.pHandle.terminate()

