all:
	g++ -std=c++11 -c variable.h
	g++ -std=c++11 -c variable.cpp
	g++ -std=c++11 -c table.h
	g++ -std=c++11 -c table.cpp
	g++ -std=c++11 -c parse.h
	g++ -std=c++11 -c parse.cpp
	g++ -std=c++11 -c read.h
	g++ -std=c++11 -c read.cpp
	g++ -std=c++11 -c main.cpp
	g++ -std=c++11 variable.o table.o parse.o read.o main.o

clean:
	rm *.o
	rm *.gch
