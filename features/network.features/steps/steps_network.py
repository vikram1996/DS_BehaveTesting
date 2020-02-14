from behave import *
from DS import *


#contains steps for network testing wrt generating networks, expanding genes and deriving hierarchies
#Each given/when/then is mapped to its corresponding scenario
#we use context to pass information between each method. All testing here is done against context variables ONLY
#each 'then' maps to the previous 'when' and 'given'


@given('a doid {doid} and its generated PCNetwork')
def step_impl(context,doid):
    context.dsTestObj = DS_Test(doid)
    context.network = context.dsTestObj.getNetwork()

@when('we expand gene set with alpha={alpha} , n={n:d} and add subnetwork = {addSubNetwork}')
def step_impl(context,alpha,n,addSubNetwork):
    try:
        context.expandedGeneset = context.dsTestObj.getExpandGeneset(alpha,n,addSubNetwork)
    except TypeError:
        print("Could not create an expanded geneset")
    else:
        context.geneset = context.dsTestObj.getGeneset()


@then('The expnansion is valid')
def step_impl(context):
    assert isValidExpansion(context.geneset , context.expandedGeneset)

#######################################################################################################################

@when('we infer hierarchical model with method={method} , edge_attr={edgeAttr} and method args')
def step_impl(context,method,edgeAttr):
    kwargs = dict()
    for row in context.table:
        kwargs[row['argument']] = float(row['value'])
    try:
        context.hiviewurl = context.dsTestObj.inferHierarchical(method,edgeAttr,kwargs)
    except TypeError:
        print("could not retrieve hiviewUrl. Check that the hierarchial service is running")




@then('the generated hierarchical model is valid')
def step_impl(context):
    assert isValidHierarchy(context.hiviewurl)

#######################################################################################################################

@given('a doid {doid}')
def step_impl(context,doid):
    context.dsTestObj = DS_Test(doid)

@when('we pull a PCNet')
def step_impl(context):
    context.network = context.dsTestObj.getNetwork()

@then('we get a valid {network_type}  with {nodes:d} and {edges:d}')
def step_impl(context,network_type,nodes,edges):
    graph = context.network.network
    truthFlag = True
    errormessage =""

    if str(graph).strip() != network_type.strip() :
        truthFlag = False
        errormessage = "The network is not formed. Expected type = " + str(graph)
    if len(graph.nodes()) != nodes or len(graph.nodes()) != edges:
        truthFlag = False
        errormessage = errormessage + " Expected numnber of nodes and edges = "+str(len(graph.nodes())) + " "+ str(len(graph.edges()))

    assert truthFlag , errormessage


#######################################################################################################################