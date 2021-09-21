#!/bin/env python3


"""

 MIT lisence. 

"""

import json
from src.theme import Theme
from src.rules import Rules
from src.logging import Logs
from src.connector import Connector

# inheritance -> Rules, Logs, Theme
class Automate_run( Rules, Logs, Theme ):


    # [ constructor ]
    def __init__( self, TYPE_AUTOMATION, FILE, FILENAME ):

        self.TYPE_AUTOMATION  =  TYPE_AUTOMATION
        self.FILE             =  FILE
        self.FILENAME         =  FILENAME

        super().__init__()

    # [ read json file & return ]
    def JSONExecute( self ) :

        FILENAME_SRC  =  open( self.FILENAME, "r" )
        RESULT        =  json.load( FILENAME_SRC )

        return RESULT
        

    # [ execute file name ]
    def FilenameExecute( self ):

        
        try :

            # [ SINGLE ACTION ]

            # rule -> [ -c | --crowded ] & [ -s | --single ]
            if ( self.TYPE_AUTOMATION == self.TYPE_CMD[0] )|( self.TYPE_AUTOMATION == self.TYPE_CMD[1] ) :

                # rule -> [ -f | --file ]
                if ( self.FILE == self.FILE_CMD[0] )|( self.FILE == self.FILE_CMD[1] ):

                    # json return
                    JsonResult = self.JSONExecute()

                    # rule -> if data type key "commands" == list | array
                    if str(type(JsonResult["commands"])) == "<class 'list'>" :

                        for indexCommands in range(len(JsonResult["commands"])) :

                            self.logsInformation(

                                HOST = JsonResult["service"]["host"],
                                PORT = JsonResult["service"]["port"],
                                ROLE = JsonResult["commands"][indexCommands]["message"]
                            )

                            if str(type(JsonResult["commands"][indexCommands]["cmd"])) == "<class 'list'>" :

                                for indexCmd in range(len(JsonResult["commands"][indexCommands]["cmd"])) : 

                                    try : 

                                        result = Connector().Connect(
                                            
                                            device_type  =  "linux",
                                            address      =  JsonResult["service"]["host"],
                                            username     =  JsonResult["service"]["user"],
                                            password     =  JsonResult["service"]["password"],
                                            port         =  JsonResult["service"]["port"],
                                            
                                            command      =  JsonResult["commands"][indexCommands]["cmd"][indexCmd]
                                            
                                        )

                                        if result :

                                            self.logsConfigurationSuccess( 

                                                MESSAGE = JsonResult["commands"][indexCommands]["cmd"][indexCmd]
                                                
                                            )
                                            
                                        
                                        else :

                                            self.logsConfigurationError(
                                                
                                                MESSAGE = JsonResult["commands"][indexCommands]["cmd"][indexCmd]
                                                
                                            )
                                        

                                    except KeyboardInterrupt :

                                        print("\nEXIT")

                                self.Line()

                            elif str(type(JsonResult["commands"][indexCommands]["cmd"])) == "<class 'str'>" :

                                try :

                                    result = Connector().Connect(
                                            
                                            device_type  =  "linux",
                                            address      =  JsonResult["service"]["host"],
                                            username     =  JsonResult["service"]["user"],
                                            password     =  JsonResult["service"]["password"],
                                            port         =  JsonResult["service"]["port"],
                                            
                                            command      =  JsonResult["commands"][indexCommands]["cmd"]
                                            
                                    )

                                    if result :

                                        self.logsConfigurationSuccess( 

                                                MESSAGE = JsonResult["commands"][indexCommands]["cmd"]
                                                
                                        )

                                        
                                    else :

                                        self.logsConfigurationError(
                                                
                                                MESSAGE = JsonResult["commands"][indexCommands]["cmd"]
                                                
                                        )
                                    
                                    self.Line()

                                except KeyboardInterrupt :
                                    
                                    print("\nEXIT")

                            else :

                                self.logsCommandsError(
                                    
                                    TYPE = "str"

                                )

                                self.Line()


                    elif str(type(JsonResult["commands"])) == "<class 'dict'>" :

                        self.logsInformation(

                            HOST = JsonResult["service"]["host"],
                            PORT = JsonResult["service"]["port"],
                            ROLE = JsonResult["commands"]["message"]
                        )
                                    
                        result = Connector().Connect(
                                            
                            device_type  =  "linux",
                            address      =  JsonResult["service"]["host"],
                            username     =  JsonResult["service"]["user"],
                            password     =  JsonResult["service"]["password"],
                            port         =  JsonResult["service"]["port"],
                                            
                            command      =  JsonResult["commands"]["cmd"]
                                            
                        )

                        if result :

                            self.logsConfigurationSuccess( 

                                MESSAGE = JsonResult["commands"]["cmd"]
                                                
                            )
                                                
                        else :

                            self.logsConfigurationError(
                                                
                                MESSAGE = JsonResult["commands"]["cmd"]
                                                
                            )
                                    
                        self.Line()

                    else :

                        self.logsCommandsError(
                                    
                                    TYPE = "dict"

                        )
                        
                        self.Line()

                else :

                    self.Theme_show()


                    
            # [ CROWDED ACTION ]
            elif ( self.TYPE_AUTOMATION == self.TYPE_CMD[2] )|( self.TYPE_AUTOMATION == self.TYPE_CMD[3] ):

                if ( self.FILE == self.FILE_CMD[0] )|( self.FILE == self.FILE_CMD[1] ):

                    JsonResult = self.JSONExecute()

                    for indexServices in JsonResult["services"] :

                        if str(type(indexServices["commands"])) == "<class 'list'>" :

                            for indexCommands in range(len(indexServices["commands"])) :

                                self.logsInformation(

                                    HOST = indexServices["host"],
                                    PORT = indexServices["port"],
                                    ROLE = indexServices["commands"][indexCommands]["message"]
                                    
                                )

                                if str(type(indexServices["commands"][indexCommands]["cmd"])) == "<class 'list'>" :

                                    for indexCmd in indexServices["commands"][indexCommands]["cmd"] :

                                        result = Connector().Connect(
                                                
                                                device_type  =  "linux",
                                                address      =  indexServices["host"],
                                                username     =  indexServices["user"],
                                                password     =  indexServices["password"],
                                                port         =  indexServices["port"],
                                                
                                                command      =  indexCmd
                                                
                                            )
                                        
                                        if result :

                                            self.logsConfigurationSuccess(

                                                MESSAGE = indexCmd

                                            )
                                            
                                        
                                        else :

                                            self.logsConfigurationError(

                                                MESSAGE = indexCmd

                                            )

                                    self.Line()

                                elif str(type(indexServices["commands"][indexCommands]["cmd"])) == "<class 'str'>" :

                                    for indexCmd in indexServices["commands"] :

                                        result = Connector().Connect(
                                                
                                                    device_type  =  "linux",
                                                    address      =  indexServices["host"],
                                                    username     =  indexServices["user"],
                                                    password     =  indexServices["password"],
                                                    port         =  indexServices["port"],
                                                    
                                                    command      =  indexCmd["cmd"]
                                                    
                                                )

                                        if result :

                                            self.logsConfigurationSuccess(

                                                MESSAGE = indexCmd["cmd"]

                                            )
                                        
                                        else :

                                            self.logsConfigurationError(

                                                MESSAGE = indexCmd["cmd"]

                                            )

                                    self.Line()

                                else : 
                                
                                    self.logsCommandsError(

                                        TYPE = "str"

                                    )
                                    
                                    self.Line()


                        elif str(type(indexServices["commands"])) == "<class 'dict'>" :

                            self.logsInformation(

                                HOST = indexServices["host"],
                                PORT = indexServices["port"],
                                ROLE = indexServices["commands"]["message"]
                                    
                            )

                            result = Connector().Connect(
                                                
                                device_type  =  "linux",
                                address      =  indexServices["host"],
                                username     =  indexServices["user"],
                                password     =  indexServices["password"],
                                port         =  indexServices["port"],
                                                    
                                command      =  indexServices["commands"]["cmd"]
                                                    
                            )

                            if result :

                                self.logsConfigurationSuccess(

                                    MESSAGE = indexServices["commands"]["cmd"]

                                )

                                self.Line()
                                        
                            else :


                                self.logsConfigurationError(

                                    MESSAGE = indexServices["commands"]["cmd"]

                                )

                                self.Line()

                        else :

                            self.logsCommandsError(

                                TYPE = "dict"

                            )

                            self.Line()
                else:

                    self.Theme_show()

            else:

                self.Theme_show()


        except KeyboardInterrupt:

            print("\nEXIT")


        