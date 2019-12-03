############################################################################
############################## OS: Windows 10 ##############################
############################################################################

import os
import sys

# ---------------------------- Utils -----------------------------#

newLine = '\n'

# The longest common prefix of the two given strings
def longestCommomPrefix(str1, str2):
    prefix = ""
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return prefix
        prefix += str1[i]
    return prefix

# ---------------------------- Conjugations -----------------------------#

# Derieves past-SG form from the base form
def derievePastSG(base):
    if len(base) >= 2:
        if base[-1] == base[-2]:
            if base[-1] not in "aeiou":
                return base + "e"
    return base

# Checks whether the base form ends with a vowel
def baseEndsWithVowel(baseForm):
    return baseForm[-1] in 'aeiou'

# Derives the 'base' (stem) form of the verb
def derieveBase(verbInfinite, verbPastSG):
    return longestCommomPrefix(verbInfinite, verbPastSG)

# Conjugates the verb according to the matching suffixes
def getConjugation(verbInfinite, verbPastSG, vowelPos, vowelRemovedNeg, consonantPos, consonantNeg, consumeNegativeVowel):
    base = derieveBase(verbInfinite, verbPastSG)
    positive = base
    negative = 'vos' + ' ' + base
    if baseEndsWithVowel(base):
        if consumeNegativeVowel:
            negative = negative[::-1][1:][::-1]
        positive += vowelPos
        negative += vowelRemovedNeg
    else:
        positive += consonantPos
        negative += consonantNeg
    return (positive, negative)

# Past SG Conjugation
def pastSGConjugation(verbInfinite, verbPastSG):
    (_, negativePastSG) = getConjugation(verbInfinite, verbPastSG, '','o','','o', True)
    return (verbPastSG, negativePastSG)

# Past PL Conjugation
def pastPLConjugation(verbInfinite, verbPastSG):
    return getConjugation(verbInfinite, verbPastSG, 'sh','osh','ish','osh', True)

# Present SG1 Conjugation
def presentSG1Conjugation(verbInfinite, verbPastSG):
    return getConjugation(verbInfinite, verbPastSG, 'k','ok','ak','ok', True)

# Present PL1 Conjugation
def presentPL1Conjugation(verbInfinite, verbPastSG):
    return getConjugation(verbInfinite, verbPastSG, 'ki','oki','aki','oki', True)

# Present SG2 Conjugation
def presentSG2Conjugation(verbInfinite, verbPastSG):
    return getConjugation(verbInfinite, verbPastSG, 'e','o','i','i', False)

# Present PL2 Conjugation
def presentPL2Conjugation(verbInfinite, verbPastSG):
    return getConjugation(verbInfinite, verbPastSG, 'e','o','i','i', False)

# Present SG3 Conjugation
def presentSG3Conjugation(verbInfinite, verbPastSG):
    return getConjugation(verbInfinite, verbPastSG, 'e','o','a','o', False)

# Present PL3 Conjugation
def presentPL3Conjugation(verbInfinite, verbPastSG):
    return getConjugation(verbInfinite, verbPastSG, 'e','o','i','i', False)


# Checkes whether the input in a proper form
def isMalformed(verbInfinite, verbPastSG):
    base = derieveBase(verbInfinite, verbPastSG)
    pastSG = derievePastSG(base)
    return pastSG != verbPastSG

# Orginizes the conjugations in a oretty-printed string
def allConjugations(verbInfinite, verbPastSG):
    if isMalformed(verbInfinite, verbPastSG):
        return ""
    (pastSG, pastSGNeg)         = pastSGConjugation(verbInfinite, verbPastSG)
    (pastPL, pastPLNeg)         = pastPLConjugation(verbInfinite, verbPastSG)
    (presentSG1, presnetSG1Neg) = presentSG1Conjugation(verbInfinite, verbPastSG)
    (presentPL1, presnetPL1Neg) = presentPL1Conjugation(verbInfinite, verbPastSG)
    (presentSG2, presnetSG2Neg) = presentSG2Conjugation(verbInfinite, verbPastSG)
    (presentPL2, presnetPL2Neg) = presentPL2Conjugation(verbInfinite, verbPastSG)
    (presentSG3, presnetSG3Neg) = presentSG3Conjugation(verbInfinite, verbPastSG)
    (presentPL3, presnetPL3Neg) = presentPL3Conjugation(verbInfinite, verbPastSG)
    str =  "infinite "    + verbInfinite + newLine
    str += "past SG "     + pastSG     + " NEG " + pastSGNeg     + newLine
    str += "past PL "     + pastPL     + " NEG " + pastPLNeg     + newLine
    str += "present SG1 " + presentSG1 + " NEG " + presnetSG1Neg + newLine
    str += "present PL1 " + presentPL1 + " NEG " + presnetPL1Neg + newLine
    str += "present SG2 " + presentSG2 + " NEG " + presnetSG2Neg + newLine
    str += "present PL2 " + presentPL2 + " NEG " + presnetPL2Neg + newLine
    str += "present SG3 " + presentSG3 + " NEG " + presnetSG3Neg + newLine
    str += "present PL3 " + presentPL3 + " NEG " + presnetPL3Neg + newLine
    return str

# ---------------------------- Main -----------------------------#

if __name__ == '__main__':
    # arguements
    infinite  = str(sys.argv[1])
    pastSG    = str(sys.argv[2])
    outputDir = str(sys.argv[3])

    # output path
    outputPath = outputDir + os.path.sep + infinite

    # create output directory if doesnt exist
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    # get conjugations
    conjugations =  allConjugations(infinite, pastSG)

    # write conjugations to file
    with open(outputPath, 'w') as outputFile:
        outputFile.write(conjugations)