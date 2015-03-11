from linkedInExtract.linkToLeap import fromFile
from linkedInTesting.linkedInJsonGenerator import generate


def main():
    filePathExtractedResults = generate() 
    return fromFile(filePathExtractedResults)


if __name__ == "__main__":
    import sys
    main()
