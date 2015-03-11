from makeMatch import *
import random
import string


random.seed()

#Test for empty input
def test_matchSkills_Empty():
    assert matchSkills([], [], strictCompare) == -1
    assert matchSkills([], [], containsStringCompare) == -1

    assert matchSkills([], ["1"], strictCompare) == -1
    assert matchSkills([], ["1", "2"], strictCompare) == -1
    assert matchSkills(["1"], [], strictCompare) == -1
    assert matchSkills(["1", "2"], [], strictCompare) == -1


    assert matchSkills(["", ""], [], strictCompare) == -1
    assert matchSkills([], ["", ""], strictCompare) == -1
    assert matchSkills(["", ""], ["","",""], strictCompare) == -1


#Test for border cases input using strictCompare and containsStringCompare
def test_matchSkills_full_match():
    sourceList = ["test1", "test2", "bob the builder"]
    targetList = ["test1", "test2", "bob the builder"]
    assert matchSkills(sourceList, targetList, strictCompare) == 1
    assert matchSkills(sourceList, targetList, containsStringCompare) == 1

    sourceList = ["test1"]
    targetList = ["test1", "test2", "bob the builder"]
    assert matchSkills(sourceList, targetList, strictCompare) == 1
    assert matchSkills(sourceList, targetList, containsStringCompare) == 1

def test_matchSkills_full_match_using_containsStringCompare():
    #assert that matches are only counted once
    sourceList = ["test"]
    targetList = ["test1", "test2", "test3", "test4"]
    assert matchSkills(sourceList, targetList, containsStringCompare) == 1
    targetList = ["test", "test", "test", "test"]
    assert matchSkills(sourceList, targetList, containsStringCompare) == 1


def test_matchSkills_no_match():
    sourceList = ["test1", "test2", "bob the builder"]
    targetList = ["alpha", "beta", "gamma"]
    assert matchSkills(sourceList, targetList, strictCompare) == 0
    assert matchSkills(sourceList, targetList, containsStringCompare) == 0

    sourceList = ["test1", "test2", "bob the builder"]
    targetList = ["alpha", "beta", "gamma"]
    assert matchSkills(sourceList, targetList, strictCompare) == 0
    assert matchSkills(sourceList, targetList, containsStringCompare) == 0


#Do automatic random testing asserting bounds of match degree are never broken
def test_matchSkills_withing_match_degree_bounds_BLACKBOX():
    repeatTimes = 20
    for _ in range(repeatTimes):
        sourceList = []
        targetList = []
        #Setup lists with random strings
        listLength = random.randint(0,200)
        for x in range(listLength):
            sourceList.append(''.join(random.choice(string.ascii_uppercase) for i in range(6)))
            targetList.append(''.join(random.choice(string.ascii_uppercase) for i in range(6)))
        assert 0 <= matchSkills(sourceList, targetList, strictCompare) <= 1
        assert 0 <= matchSkills(sourceList, targetList, containsStringCompare) <= 1