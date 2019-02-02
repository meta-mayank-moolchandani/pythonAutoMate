import inflect

EntityName = "Account"
EntityObject = "account"
pluralEngine = inflect.engine()
EntityPlural = pluralEngine.plural(EntityName)

selectorTemplateFile = open('./templates/selector.txt', 'r')
selectorData = selectorTemplateFile.read()
selectorTemplateFile.close()

domainTemplateFile = open('./templates/domain.txt', 'r')
domainData = domainTemplateFile.read()
domainTemplateFile.close()

iServiceFile = open('./templates/serviceInterface.txt', 'r')
iServiceData = iServiceFile.read()
iServiceFile.close()

baseServiceFile = open('./templates/serviceImpl.txt', 'r')
serviceImpl = baseServiceFile.read()
baseServiceFile.close()

mainServiceFile = open('./templates/service.txt', 'r')
mainServiceData = mainServiceFile.read()
mainServiceFile.close()

params = [EntityName, EntityPlural, "account"]
selectorResult = ""
domainResult = ""
iServiceResult = ""
baseService = ""
mainService = ""

with open("./Result/" + EntityPlural + "Selector.cls", "w") as text_file:
    selectorResult = selectorData.replace("{{0}}", EntityName)
    selectorResult = selectorResult.replace("{{1}}", EntityPlural)
    text_file.write(selectorResult)

with open("./Result/" + EntityPlural + ".cls", "w") as text_file:
    domainResult = domainData.replace("{{0}}", EntityName)
    domainResult = domainResult.replace("{{1}}", EntityPlural)
    text_file.write(domainResult)

with open("./Result/I" + EntityName + "Service.cls", "w") as text_file:
    iServiceResult = iServiceData.replace("{{0}}", EntityName)
    iServiceResult = iServiceResult.replace("{{1}}", EntityPlural)
    text_file.write(iServiceResult)

with open("./Result/" + EntityName + "ServiceImpl.cls", "w") as text_file:
    baseService = serviceImpl.replace("{{0}}", EntityName)
    baseService = baseService.replace("{{1}}", EntityPlural)
    baseService = baseService.replace("{{2}}", EntityObject)
    text_file.write(baseService)

with open("./Result/" + EntityName + "Service.cls", "w") as text_file:
    mainService = mainServiceData.replace("{{0}}", EntityName)
    mainService = mainService.replace("{{1}}", EntityPlural)

    text_file.write(mainService)

