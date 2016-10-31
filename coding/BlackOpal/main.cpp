#include "parse.h"
#include "table.h"
#include "variable.h"
#include "read.h"
#include <iostream>
#include <fstream>

int main(){
    std::ifstream file;
    file.open("test.opal");
    read(file);
}
