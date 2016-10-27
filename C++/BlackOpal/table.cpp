#include "table.h"

varTable::varTable(){
    std::cout << "Hashtable has been initialized!" << std::endl;
}

varTable::~varTable(){
    delete[] varTable::table;
}

/* shitty hashing function
 */
int varTable::hash(std::string varName){
    int i, result;
    char hold;
    result = 0;
    /*- Somewhat less colisions? -*/
    for(i = 0; i < varName.length(); i++){
        hold = varName[i];
        result += (int(hold) * (i + 1));
    }
    result = result % 100;
    return result;
}

variable * varTable::get(std::string varName){
    int where = varTable::hash(varName);
    return &varTable::table[where];
}

void varTable::make(std::string type, std::string varName){
    int where = varTable::hash(varName);
    variable* hold = &varTable::table[where];
    if (hold->alias == ""){
        hold->alias = varName;
        if (type == "int"){
            hold->type = 1;
        }
        else if (type == "str"){
            hold->type = 2;
        }
        else{
            hold->type = 1;
        }
    }
    else{
        std::cout << "This slot in the table has already been taken, possible collision." << std::endl;
    }
}
