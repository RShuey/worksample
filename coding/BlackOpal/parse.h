#ifndef PARSE_H
#define PARSE_H

#include <string>
#include <sstream>
#include <iostream>
#include "table.h"
#include "variable.h"

void parseLine(std::string line);
int ifCheck(std::string varName);

#endif
