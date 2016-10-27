#ifndef VARIABLE_H
#define VARIABLE_H
#include <string>
#include <iostream>

class variable{
    public:
        int intPayload;
        std::string strPayload;
        int type;
        std::string alias;

        variable();
        variable(int type, std::string alias);
};

#endif
