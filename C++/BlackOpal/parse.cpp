#include "parse.h"

varTable * vt = new varTable;

void parseLine(std::string line){
    std::istringstream linestream(line);
    std::string hold;
    variable * varHold;

    getline(linestream, hold, ' ');
    
    /* here comes the wall of commands
     */

    /* SYNTAX:
     * print "text to print"
     */
    if (hold == "print"){
        getline(linestream, hold, '"');
        getline(linestream, hold, '"'); /*- We do this twice so we can get over the first quote mark -*/
        std::cout << hold << std::endl;
    }
    /* SYNTAX:
     * printvar variable
     */
    else if (hold == "printvar"){
        getline(linestream, hold, ' ');
        getline(linestream, hold);/*- go untill end -*/
        varHold = vt->get(hold);
        if (varHold->type == 1){
            std::cout << varHold->intPayload << std::endl;
        }
        else if (varHold->type == 2){
            std::cout << varHold->strPayload << std::endl;
        }
        else{
            std::cout << "Variable type not reconized." << std::endl;
        }
    }
    /* SYNTAX:
     * make int testvariable
     */
    else if (hold == "make"){
        std::string type, alias;
        getline(linestream, type, ' ');
        getline(linestream, alias, ' ');
        vt->make(type, alias);
    }
    /* SYNTAX:
     * set variable (1)
     * OR
     * set variable "this"
     */
    else if (hold == "set"){
        getline(linestream, hold, ' '); /*- get the variable name -*/
        varHold = vt->get(hold);
        if (varHold->alias == hold){
            if (varHold->type == 1){
                getline(linestream, hold, '\"');
                getline(linestream, hold, '\"');
                varHold->intPayload = std::stoi(hold);
            }
            else if (varHold->type == 2){
                getline(linestream, hold, '\"');
                getline(linestream, hold, '\"');
                varHold->strPayload = hold;
            }
            else{
                std::cout << "Unreconized variable type \"" << varHold->type << "\"" << std::endl;
            }
        }
        else{
            std::cout << "The variable returned via get was not the variable we wanted.  Collision?" << std::endl;
        }
    }

}

int ifCheck(std::string varName){
    variable * varhold = vt->get(varName);
    if (varhold->type == 1){
        if (varhold->intPayload == 0){
            return 0;
        }
        else{
        return 1;
        }
    }else{
        return 0;
    }
}
