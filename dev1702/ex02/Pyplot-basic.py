# https://wikidocs.net/1922

import matplotlib.pyplot as plt
#plt.plot([1,2,3,4], [1,2,3,4], 'r--')
#plt.plot([1,2,3,4], [1,2,3,4], 'bo', [1,2,3,4], [1,4,9,16], 'rs')
#plt.show()

d1 = [1,2,3,4]
plt.plot(d1, d1)
plt.xlabel('data X')
plt.ylabel('data Y')
plt.show()

# 에러 발생 수정 (ValueError: _getfullpathname: embedded null character)
# http://stackoverflow.com/questions/34004063/error-on-import-matplotlib-pyplot-on-anaconda3-for-windows-10-home-64-bit-pc

