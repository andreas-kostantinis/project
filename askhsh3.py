#!/usr/bin/python
# -*- coding: utf-8 -*-


code=open("test.txt" , "r")
code_back = open("new_test1.txt" , "w")
for line in code: #για κάθε γραμμή στον κώδικα txt
   if not line.startswith("#"): #εαν δεν ξεκινάει με #
      code_back.write(line)

code.close()
code_back.close()      
