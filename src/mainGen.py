from linkedInExtract.linkToLeap import fromFile
from linkedInTesting.linkedInJsonGenerator import main 
import sys

def main():
    filePathExtractedResults = main()
    return fromFile(filePathExtractedResults)

if __name__ == "__main__":
    main()
