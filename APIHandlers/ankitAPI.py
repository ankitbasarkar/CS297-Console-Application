from ProcessPkg.RunningAnalysisProcesses import RunningAnalysisProcesses
import time
def ankitAPI(Name,MLAlgorithm,Scaling,Location,Normalization,Filtering):
    fileOut = open(Name,'w')
    from sklearn import datasets
    iris = datasets.load_iris()
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
    fileOut.write("Number of mislabeled points out of a total %d points : %d"% (iris.data.shape[0],(iris.target != y_pred).sum()))
    fileOut.write("\nTerminating")