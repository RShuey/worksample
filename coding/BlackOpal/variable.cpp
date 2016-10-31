#include "variable.h"

variable::variable(){
    variable::type = 1;
    variable::alias = "";
    variable::intPayload = 0;
}

variable::variable(int type, std::string alias){
    variable::alias = alias;
    switch(type){
        case 1:
            variable::type = 1;
            variable::intPayload = 0;
        case 2:
            variable::type = 2;
            variable::strPayload = "";
    }
}
