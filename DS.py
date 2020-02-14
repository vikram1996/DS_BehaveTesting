#contains pilot code which runs diseasescope code to test on the behave suite
#more information on individual methods can be found here: https://github.com/shfong/DiseaseScope/blob/master/examples/example_diseasescope.ipynb
from diseasescope import DiseaseScope

#DS_Test is used to test all aspects of diseasescope. All parameters being tested have to be assigned to some attribute of DS_Test.
class DS_Test():
    def __init__(self,ipDoid=None):
        self.doid = ipDoid #set doid
        self.scope = None # diseasescope scope
        self.network = None #scope network

        #set scope from doid
        try:
            self.scope = DiseaseScope(self.doid, convert_doid=True)
        except:
            print("Behave: Doid "+self.doid+" could not be mapped to a disease")
        else:
            self.disease = self.scope.disease


        #get genes from scope
        try:
            self.scope.get_disease_genes(method="disgenet") # method  = disgenet , biothings
        except:
            print("Behave: Doid "+self.doid+" could not be mapped to its genes")
        else:
            self.geneset = self.scope.genes


        #get tissues
        try:
            self.scope.get_disease_tissues(method="pubmed")
        except:
            print("Behave: Doid " + self.doid + " could not be mapped to its tissues")
        else:
            self.tissueset = self.scope.tissues




    def getDoid(self):
        return self.doid
    def getDisease(self):
        return self.disease
    def getGeneset(self):
        return self.geneset
    def getTissueset(self):
        return self.tissueset

    #build network
    def getNetwork(self):
        try:
            self.scope.get_network(method="ndex", uuid=self.scope.PCNET_UUID)
        except:
            print("Behave: Doid " + self.doid + " could not generate a netowrk")
        else:
            self.network = self.scope.network
        return self.network

    #expand geneset
    def getExpandGeneset(self,alpha,n,addSubNetwork):
        try:
            if addSubNetwork.strip() == "True":
                add_sn = True
            else:
                add_sn = False
            self.scope.expand_gene_set(
                method="random walk",
                alpha=float(alpha),
                n=n,
                add_subnetwork=add_sn
            )
        except:
            print("Behave: Doid " + self.doid + " could not expand network")
        else:
            self.expandedGeneset = self.scope.expanded_genes
        return self.expandedGeneset

    #infering Hierarchical model
    def inferHierarchicalModel(self,method,edgeAttr,args):
        kwargs = {key: value[:] for key, value in args.items()}
        try:
            self.scope.infer_hierarchical_model(method = method , edge_attr= edgeAttr , method_kwargs= kwargs)
        except:
            print("Behave: Doid " + self.doid + " could not infer hierarchy")
        else:
            self.hiViewUrl = self.scope.hiview_url
        return self.hiViewUrl


    def __getattr__(self, item):
        return None



########################base testing#########################
#map all doid's to their diseases
def getAllDoidMapping():
    textfile = open("dataFiles/doid_list_data.txt", "r")
    doids= eval(textfile.read().strip())
    doidDiseaseDict = {}
    for d in doids:
        scope = DiseaseScope(d, convert_doid=True)
        doidDiseaseDict[d] = scope.disease

    return doidDiseaseDict

#map all diseases to their doid's
def getDoidFromDisease(disease):
    textfile = open("dataFiles/doid_list_data.txt", "r")
    doids = eval(textfile.read().strip())
    for d in doids:
        scope = DiseaseScope(d, convert_doid=True)
        if scope.disease.strip().lower() == disease.lower():
            return d

#check if doid is valid on the biothings dataset
def isValidDoid(doid):
     try:
         scope = DiseaseScope(doid, convert_doid=True)
     except:
        return "Invalid"
     else:
         return "Valid"


####################network testing#####################
#check if expanded gene set is valid. check if intersection with base geneset is non zero
def isValidExpansion(geneset , expandedgeneset):
    print(len(set(geneset).intersection(set(expandedgeneset))))
    if  len(set(geneset).intersection(set(expandedgeneset))) > 0:
        return True
    else:
        return False


#check if generated hierarchy is valid. We check if the hiview URL returned is a valid url
def isValidHierarchy(hiViewUrl):
    validUrl = "http://hiview.ucsd.edu/"
    if len(hiViewUrl) < len(validUrl):
        return False
    if str(hiViewUrl)[:len(validUrl)] != validUrl:
        return False
    return True

