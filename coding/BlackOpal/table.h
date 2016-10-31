#ifndef TABLE_H
#define TABLE_H
#include <string>
#include <iostream>
#include <vector>
#include "variable.h"

class varTable {
    private:
       variable *table = new variable[100]; 
    public:
        varTable();
        ~varTable();
        int hash(std::string varName);
        variable * get(std::string varName);
        void make(std::string type, std::string varName);
};

#endif
