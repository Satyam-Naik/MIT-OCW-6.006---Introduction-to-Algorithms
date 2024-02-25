def count_long_subarray(A):
  '''
  Input:  A     | Python Tuple of positive integers
  Output: count | number of longest increasing subarrays of A
  '''
  res = 1
  res_len = 1
  freq = 1
  for i in range(1,len(A)):
    if A[i] > A[i-1]:
      freq += 1
      continue
    if freq > res_len:
      res = 1
      res_len = freq
    elif freq == res_len:
      res += 1
    freq = 1
  if freq > res_len:
    return 1
  elif freq == res_len:
    return res + 1
  else:
    return res
