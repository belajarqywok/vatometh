class Logs:

    def logsInformation( self, HOST, PORT, ROLE ) :

        print(

            f'| HOST | =---> {HOST}\n'+
            f'| PORT | =---> {PORT}\n\n'+
            f'| ROLE | =---> {ROLE}\n'

        )


    def logsConfigurationError(self, MESSAGE):

        print(f'+-[ CONFIGURATION FAILED ]-> {MESSAGE}')
        

    def logsConfigurationSuccess(self, MESSAGE):

        print(f'+-[ CONFIGURATION SUCCESS ]-> {MESSAGE}')


    def logsCommandsError(self, TYPE = "str"):
        
        if TYPE == "dict":

            print('+-[ CONFIGURATION FAILED ]-> Key "commands" MUST dict | list, NOT int, str, tuple, etc.')

        else:
            
            print('+-[ CONFIGURATION FAILED ]-> Key "commands" MUST str | list, NOT int, dict, tuple, etc.')

    def Line(self):

        print("\n"+"=+"*20+"\n")


