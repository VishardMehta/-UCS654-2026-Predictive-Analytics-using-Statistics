import sys
from topsis_package.topsis_vishard_102317240.topsis import topsis

if len(sys.argv) != 5:
    print("Usage: python run_cli.py <InputFile> <Weights> <Impacts> <OutputFile>")
    sys.exit(1)

topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
