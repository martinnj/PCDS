from linkedInLogin.linkedin_connector import linkedin_connector
from linkedInExtract.linkToLeap import fromFile


def main():
    filePathExtractedResults = "linkedInLogin/" + linkedin_connector()
    fromFile(filePathExtractedResults)


if __name__ == "__main__":
    import sys
    main()