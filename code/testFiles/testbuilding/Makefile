# super simple makefile for an AmyScript file 


COMPILER=amyc

SRC=helloworld.amy

DEPENDENCIES=utils/stdlib.amy utils/vector.amy utils/max.amy

FLAGS= --emitAST --emitPreprocessed

DEST=helloworld.amy.assembly

$(SRC).assembly: $(SRC)
	$(COMPILER) $(SRC) $(DEPENDENCIES) $(FLAGS) -o $(DEST)

clean:
	rm -f $(DEST)
	rm -f $(SRC).preprocessed
	rm -f $(SRC).ast