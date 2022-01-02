## プログラミングコンテストチャレンジブック（第2版)

### Test sample

```shell
$ diff -Zu  <(python main.py < test-1.in) <(cat ./test-1.out)
--- /dev/fd/63  2021-12-05 08:34:58.818064233 +0900
+++ /dev/fd/62  2021-12-05 08:34:58.818064233 +0900
@@ -1 +1 @@
-3
+2
\ No newline at end of file
```

### Dependency

[AtCoderのPython, NumPy, SciPyのバージョンと注意点（2020年5月）](https://note.nkmk.me/atcoder-python-numpy-scipy-version/) より requirements.txt で numpy などのバージョンを指定している。  
ただし atcoder において pypy3 (7.3.0) では numpy, scipy などは利用できないので注意。