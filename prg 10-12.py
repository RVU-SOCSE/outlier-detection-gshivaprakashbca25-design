Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
========== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 10.py ==========
Traceback (most recent call last):
  File "C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 10.py", line 5, in <module>
    enc = OneHotEncoder()
NameError: name 'OneHotEncoder' is not defined
>>> 
========== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 10.py ==========
Traceback (most recent call last):
  File "C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 10.py", line 17, in <module>
    le = LabelEncoder()
NameError: name 'LabelEncoder' is not defined
>>> 
========== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 10.py ==========
>>> 
========== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 10.py ==========
>>> 
========== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 10.py ==========
Original Data:
   Manufacturer   Model_Name  ... Weight_kg        Price
0        Apple  MacBook Pro  ...      1.37  11912523.48
1        Apple  Macbook Air  ...      1.34   7993374.48
2           HP       250 G6  ...      1.86   5112900.00
3        Apple  MacBook Pro  ...      1.83  22563005.40
4        Apple  MacBook Pro  ...      1.37  16037611.20

[5 rows x 13 columns]

RAM Classes: ['12GB' '16GB' '24GB' '2GB' '32GB' '4GB' '6GB' '8GB']

Final Data:
     Manufacturer       Model_Name  ...  Ultrabook Workstation
0          Apple      MacBook Pro  ...        1.0         0.0
1          Apple      Macbook Air  ...        1.0         0.0
2             HP           250 G6  ...        0.0         0.0
3          Apple      MacBook Pro  ...        1.0         0.0
4          Apple      MacBook Pro  ...        1.0         0.0
..           ...              ...  ...        ...         ...
972         Dell     Alienware 17  ...        0.0         0.0
973      Toshiba  Tecra A40-C-1DF  ...        0.0         0.0
974         Asus        Rog Strix  ...        0.0         0.0
975           HP      Probook 450  ...        0.0         0.0
976       Lenovo    ThinkPad T460  ...        0.0         0.0

[977 rows x 18 columns]

========== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 11.py ==========

========== RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 11.py ==========
    YearsExperience    Salary
0         -1.510053 -1.360113
1         -1.438373 -1.105527
2         -1.366693 -1.419919
3         -1.187494 -1.204957
4         -1.115814 -1.339781
5         -0.864935 -0.718307
6         -0.829096 -0.588158
7         -0.757416 -0.799817
8         -0.757416 -0.428810
9         -0.578216 -0.698013
10        -0.506537 -0.474333
11        -0.470697 -0.749769
12        -0.470697 -0.706620
13        -0.434857 -0.702020
14        -0.291498 -0.552504
15        -0.148138 -0.299217
16        -0.076458 -0.370043
17        -0.004779  0.262859
18         0.210261  0.198860
19         0.246100  0.665476
20         0.532819  0.583780
21         0.640339  0.826233
22         0.927058  0.938611
23         1.034577  1.402741
24         1.213777  1.240203
25         1.321296  1.097402
26         1.500496  1.519868
27         1.536336  1.359074
28         1.787215  1.721028
29         1.858894  1.701773

========= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 12(a).py ========
Traceback (most recent call last):
  File "C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 12(a).py", line 3, in <module>
    df2 = pd.read_csv("4laptops.csv")
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\G SHIVAPRAKASH\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '4laptops.csv'

========= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 12(a).py ========

========= RESTART: C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/prg 12(b).py ========
    Manufacturer       Model_Name  ... Weight_kg        Price
0          Apple      MacBook Pro  ...      1.37  11912523.48
1          Apple      Macbook Air  ...      1.34   7993374.48
2             HP           250 G6  ...      1.86   5112900.00
3          Apple      MacBook Pro  ...      1.83  22563005.40
4          Apple      MacBook Pro  ...      1.37  16037611.20
..           ...              ...  ...       ...          ...
972         Dell     Alienware 17  ...      4.42  24897600.00
973      Toshiba  Tecra A40-C-1DF  ...      1.95  10492560.00
974         Asus        Rog Strix  ...      2.73  18227710.80
975           HP      Probook 450  ...      2.04   8705268.00
976       Lenovo    ThinkPad T460  ...      1.70   8909784.00

[977 rows x 13 columns]
lower bound, upper bound and iqr values are:  0.30000000000000027 3.4999999999999996 0.7999999999999998
No.of outliers are:  33
