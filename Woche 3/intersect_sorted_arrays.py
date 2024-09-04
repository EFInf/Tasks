def intersect_two_sorted_arrays(A, B):
   iA, iB = 0, 0
   C = []
   while iA<len(A) and iB<len(B):
      if A[iA]<B[iB]:
         iA += 1
      elif A[iA]>B[iB]:
         iB += 1
      else: # A[iA]==B[iB]
         if len(C)==0 or C[-1]!=A[iA]:
            C.append(A[iA])
         iA += 1
         iB += 1
   return C

import bisect

def intersect_two_sorted_arrays_with_binary_search(A, B):
   # A ist viel grösser als B
   C = []
   for i in B:
      iA = bisect.bisect_left(A,i) # liefert den Index des ersten Elements von A zurück, das nicht kleiner als i ist
      if iA<len(A) and A[iA]==i:
        if len(C)==0 or C[-1]!=i:
            C.append(i)
   return C


A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
B = [5, 5, 6, 8, 8, 9, 10, 20]
print(intersect_two_sorted_arrays(A,B))
print(intersect_two_sorted_arrays_with_binary_search(A,B))
print(intersect_two_sorted_arrays_with_binary_search(B,A))
