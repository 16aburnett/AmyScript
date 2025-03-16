



# Testing Parallelism

Compiling to C++
```bash
python3 amyScriptCompiler.py testcpp/testParallel.amy --target cpp -o testcpp/testParallel.cpp
```

Compiling C++
```bash
g++ testcpp/testParallel.cpp -fopenmp -o testcpp/testParallel
```

Running
```bash
OMP_DYNAMIC=TRUE ./testcpp/testParallel
```
