#ifndef READ_H
#define READ_H
#include "variable.h"
#include "table.h"
#include "parse.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

void read(std::ifstream & infile);
void lineloop(std::ifstream * infile, int mode);

#endif
