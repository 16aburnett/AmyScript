# super simple makefile for an AmyScript file 


COMPILER=amyc

SRC=helloworld.amy

DEPENDENCIES=utils/stdlib.amy utils/vector.amy utils/max.amy

$(SRC).assembly: $(SRC)
	$(COMPILER) $(SRC) $(DEPENDENCIES)

clean:
	rm $(SRC).assembly