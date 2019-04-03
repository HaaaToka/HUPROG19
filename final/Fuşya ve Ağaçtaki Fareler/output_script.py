import os, subprocess

compile_str = "g++ solution.cpp"
run_str = "a.exe"
os.system(compile_str)


"""for i in range(20):
    fin = open("input/input" + str(i).zfill(2) + ".txt", "r")
    fout = open("output/output" + str(i).zfill(2) + ".txt", "w")
    output = subprocess.check_output([run_str], stdin=fin)
    print(*(str(output)[2:-1]).split("\\r\\n"), sep="\n", file=fout)"""

fin = open("ex_input.txt", "r")


output = subprocess.check_output([run_str], stdin=fin)
print(*(str(output)[2:-1]).split("\\r\\n"), sep="\n")


    
