from behave import *
from DS import *

#contains steps for base testing wrt gene/tissue/disease mapping
#Each given/when/then is mapped to its corresponding scenario
#we use context to pass information between each method. All testing here is done against context variables ONLY
#each 'then' maps to the previous 'when' and 'given'

@given('a doid {doid}')
def step_impl(context,doid):
    context.inputDoid = doid


@when('we look the doid up with diseaseScope')
def step_impl(context):
    context.validity = isValidDoid(context.inputDoid)

@then('it yields {validity}')
def step_impl(context,validity):
    errormessage = "validity expected  = " + validity + " but validity determined = " + context.validity
    assert context.validity == validity , errormessage

#######################################################################################################################

@given('a valid doid {valid_doid}')
def step_impl(context,valid_doid):
    context.dsTestObj = DS_Test(valid_doid)

@when('we run diseaseScope to get the disease from doid')
def step_impl(context):
    context.disease = context.dsTestObj.getDisease()

@then('{disease} is correct')
def step_impl(context,disease):
    errormessage = "Disease expected  = "+disease+" but disease determined = "+context.disease
    assert (context.disease).lower() == (disease.strip(" ")).lower() , errormessage

#######################################################################################################################

@given('a disease for gene association: {disease}')
def step_impl(context,disease):
    context.dsTestObj = DS_Test(getDoidFromDisease(disease))

@when('we run diseaseScope to get the associated genes of the disease')
def step_impl(context):
    context.genes = context.dsTestObj.getGeneset()

@then('{genes} are contained by the associated genes determined')
def step_impl(context,genes):
    errormessage = "Genes expected  = "+genes+" but genes determined = "+str(context.genes)
    geneset = genes.split(',')
    for gene in geneset:
        assert gene in context.genes , errormessage

#######################################################################################################################

@given('a disease for tissue association: {disease}')
def step_impl(context,disease):
    doid = getDoidFromDisease(disease)
    context.dsTestObj = DS_Test(doid)

@when('we run diseaseScope to get the associated tissues of the disease')
def step_impl(context):
    context.tissues = context.dsTestObj.getTissueset()

@then('{tissues} are contained by the associated tissues determined')
def step_impl(context,tissues):
    errormessage = " genes determined = "+str(context.tissues)
    tissueset = tissues.split(',')
    determinedset = []
    for t in context.tissues:
       determinedset.append(t['tissue'])
    for t in tissueset:
        assert t in determinedset , t+" was not amongst the determined tissues. " +errormessage

#######################################################################################################################

@given('a file: {filename}')
def step_impl(context,filename):
    context.filename = "testFiles/"+filename

@when('we compare tissues in the file with those produced by diseasescope')
def step_impl(context):
    context.file = open(context.filename, "r")
    context.diseaseDict = {}
    for d in context.file.read().strip().split("\n"):
        dContent = d.split('#')
        context.diseaseDict[dContent[0]] = list(dContent[1].split(','))

@then('the two listings match exactly')
def step_impl(context):
    for keys in context.diseaseDict:
        dsTestObj = DS_Test(getDoidFromDisease(keys))
        tissueSetToCompare = []
        for t in dsTestObj.getTissueset():
            tissueSetToCompare.append(t['tissue'])

        errormessage= "for "+keys+": tissues provided = "+str(context.diseaseDict[keys])  + " Tissues determined = "+str(tissueSetToCompare)
        assert set(context.diseaseDict[keys]) ==  set(tissueSetToCompare) , errormessage


#######################################################################################################################

@when('we compare disease in the file with those produced by diseasescope')
def step_impl(context):
    context.file = open(context.filename, "r")
    context.diseaseDict = {}
    for d in context.file.read().strip().split("\n"):
        dContent = d.split(':')
        context.diseaseDict[dContent[0]] = dContent[1]

@then('all entries are correct')
def step_impl(context):
    for keys in context.diseaseDict:
        dsTestObj = DS_Test(keys)
        errormessage= "for "+keys+": disease provided = "+context.diseaseDict[keys] + " Disease determined = "+dsTestObj.getDisease()
        assert context.diseaseDict[keys] == dsTestObj.getDisease(), errormessage

