# super simple makefile for an AmyScript file 


COMPILER=python3 ../code/amyc/amyScriptCompiler.py

SRC=

DEPENDENCIES=Vector.amy

FLAGS= --emitAST --emitPreprocessed --target x86

DEST=helloworld.asm

$(SRC).asm: $(SRC)
	$(COMPILER) $(SRC) $(DEPENDENCIES) $(FLAGS) -o $(DEST)

clean:
	rm -f $(DEST)
	rm -f $(SRC).preprocessed
	rm -f $(SRC).ast