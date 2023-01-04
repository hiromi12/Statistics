# 1Var Stats
# Date: Jan 2, 2023
# Author: Hiromi Honda

# Program Description: 
# These functions work same as '1-Var Stats' on TI-84 calculator. (stat -> CALC -> 1:)

import math
# sum
def sum_li(n):
  s = 0
  for i in range(len(n)):
    s += n[i]
  return s

def sum_of_sqr(n):
  t = 0
  for i in range(len(n)):
    t = t + (n[i] ** 2)
  return t

# average
def avg_li(n):
  return sum_li(n) / len(n)

# even or odd
def even(a):
  if a % 2 == 0:
    return True
  return False

# sort data
def sort_li(n):
  for i in range(len(n)):
    for j in range(len(n)-1):
      if n[i] < n[j]:
        temp = n[i]
        n[i] = n[j]
        n[j] = temp
  return n

# mean
def mean_li(n):
  m = 0
  # sort data
  s = sort_li(n)
  # find mean
  if len(s) == 2:
    return avg_li(s)
  elif even(len(s)) == False:
    m = s[(len(s) // 2)]
  else:
    m = (s[len(s) // 2] + s[(len(s) // 2) + 1]) / 2
  return m

def mean_sum_of_sqr(n):
  t = 0
  for i in range(len(n)):
    t = t + ((n[i] - mean_li(n)) ** 2)
  return t

# standard deviation
def sds_li(n):
  sd = math.sqrt(((mean_sum_of_sqr(n)) / len(n)))
  return sd

def sdp_li(n):
  sd = math.sqrt(((mean_sum_of_sqr(n)) / (len(n) - 1)))
  return sd

def min_li(n):
  s = sort_li(n)
  return s[0]

def max_li(n):
  s = sort_li(n)
  return s[-1]

def q1_li(n):
  s = sort_li(n)
  if even(len(n)) == False:
  # odd num array
    o = s[slice(0,((len(s) // 2)))]
    q1 = mean_li(o)
  else:
  # even num array
    e = s[slice(0,int(len(s) / 2))]
    q1 = mean_li(e)
  return q1

def q3_li(n):
  s = sort_li(n)
  if even(len(n)) == False:
  # odd num array
    o = s[slice(((len(s) // 2) + 1),len(s))]
    q3 = mean_li(o)
  else:
  # even num array
    e = s[slice(int((len(s) / 2) + 1),len(s))]
    q3 = mean_li(e)
  return q3

def stats(n):
  print("Average = "+str(avg_li(n)))
  print("Sum = "+str(sum_li(n)))
  print("Square of Sum = "+str(sum_of_sqr(n)))
  print("SD of Population = "+str(sdp_li(n)))
  print("SD of Sample = "+str(sds_li(n)))
  print("n = "+str(len(n)))
  print("min = "+str(min_li(n)))
  print("Q1 = "+str(q1_li(n)))
  print("Mean = "+str(mean_li(n)))
  print("Q3 = "+str(q3_li(n)))
  print("max = "+str(max_li(n)))
  
li = [3.32,2.53,3.45,2.38,3.01]
stats(li)

# Output
#
# Data = [2.38, 2.53, 3.01, 3.32, 3.45]
# Average = 2.938
# Sum = 14.690000000000001
# Square of Sum = 44.0503
# SD of Population = 0.47880058479496457
# SD of Sample = 0.42825226210727724
# n = 5
# min = 2.38
# Q1 = 2.455
# Mean = 3.01
# Q3 = 3.385
# max = 3.45
#