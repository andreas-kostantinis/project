#!/usr/bin/python
# -*- coding: utf-8 -*-


from sys import maxsize #κάνουμε import
def maxSequence(a,size): #η συνάρτηση δέχεται δυο ορίσματα την λίστα a και το μέγεθος του, δηλαδη το len(a)
  
    max_so_far = -maxsize - 1 #αρχικό max
    max_ending_here = 0 #αρχικοποίηση των μεταβλητών
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] #καθε επανάληψη προσθέτει το στοιχείο του πινακα
  
        if max_so_far < max_ending_here: #σύγκριση των δύο μεταβλητών 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: #εαν γίνει αρνητικό τότε αρχικοποιείται ξανά
            max_ending_here = 0
            s = i+1
  
    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print ((a[start:end+1]))
