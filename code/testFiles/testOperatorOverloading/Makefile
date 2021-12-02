# Simple build for operator overloading test 


COMPILER=amyc

SRC=driver.amy

DEPENDENCIES=utils/vector.amy

FLAGS= --emitAST --emitPreprocessed

DEST=$(SRC).assembly

$(SRC).assembly: $(SRC)
	$(COMPILER) $(SRC) $(DEPENDENCIES) $(FLAGS) -o $(DEST)

clean:
	rm -f $(DEST)
	rm -f $(SRC).preprocessed
	rm -f $(SRC).ast