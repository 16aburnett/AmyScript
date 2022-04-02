# super simple makefile for an AmyScript file 


COMPILER=python3 ../amyScriptCompiler.py

SRC=helloworld.amy

DEPENDENCIES=

FLAGS= --emitAST --emitPreprocessed --target x86

DEST=helloworld.asm

$(SRC).asm: $(SRC)
	$(COMPILER) $(SRC) $(DEPENDENCIES) $(FLAGS) -o $(DEST)

clean:
	rm -f $(DEST)
	rm -f $(SRC).preprocessed
	rm -f $(SRC).ast