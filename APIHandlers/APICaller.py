class APICaller:
    @staticmethod
    def apiCall(Name,MLAlgorithm,Scaling,Location,Normalization,Filtering):
        #   In this method you can use these parameters in which ever way you want
        if(Name=='ankit'):
            import APIHandlers.ankitAPI as abAPI
            abAPI.ankitAPI(Name,MLAlgorithm,Scaling,Location,Normalization,Filtering)

