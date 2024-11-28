from functions import interface_functions

domain= interface_functions.domain()
functionn= interface_functions.function_creator()
grapher= interface_functions.grapher(domain, functionn)


while True:
    interface_functions.slope_finding_interface(functionn)