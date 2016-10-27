#include "read.h"

void read(std::ifstream & infile){
    std::string hold;

    getline(infile, hold, ' ');/*- FIRST LINE -*/
    if (hold == "gate"){/*- this is a file that we need to read right? -*/
        getline(infile, hold);/*- What is my name -*/
        std::cout << "Running program \"" << hold << "\"." << std::endl << std::endl; /*- So that is my name? -*/
        /*- What a beautiful name... -*/
        lineloop(&infile, 1);
    }
    else{
        std::cout << "Error: This is not a program." << std::endl;
    }
}

void lineloop(std::ifstream * infile, int mode){
    int sentry = 0;
    std::string hold[2];
    while (sentry == 0){
        getline(*infile, hold[0]);
        if (hold[0] == "}"){
            sentry == 1;
            return;
        }
        else if (mode == 1){
            std::istringstream iss(hold[0]);
            getline(iss, hold[1], ' ');
            if (hold [1] == "gate"){
                getline(iss, hold[1], ' ');
                if (hold[1] == "if"){
                    getline(iss, hold[1], ' ');
                    int tOrF = ifCheck(hold[1]);
                    if (tOrF != 0){
                        lineloop(infile, 1);
                    }
                    else{
                        lineloop(infile, 0);
                    }
                }
            }
            else{
                parseLine(hold[0]);
            }
        }
    }
}
