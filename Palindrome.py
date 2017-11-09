# -*- coding: utf-8 -*-
####
#Palindome.py
#Checking that the word is Palindrome
#Agnieszka Piwowarczyk, 09.11.2017 r.
#ver.1.1
####
#sample input data
input="hlbeeykoqqqqokyeeblh"

def checkPalindrome(inputString):
    a=len(inputString)
    print a
    if a==1:
        print "a rowne 1"
    elif a%2!=0:
        if inputString[0:((a-1)/2):1]== inputString[-1:(-(a+1)/2):-1]:
            print "Wprowadzone słowo to Palindrome" 
        else:
            print "to nie Palindrome"
        
    else:
        if inputString[0:(a/2):1]== inputString[-1:(-(a+2)/2):-1]:
            print "Wprowadzone słowo to Palindrome" 
        else:
            print "to nie Palindrome"

#the methon execution
checkPalindrome(input)
