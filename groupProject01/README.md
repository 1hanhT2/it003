# Group Project 01 – Basic C++ Exercises

![Bui Tan Thanh – Personal Card](../personalCard.png)

C++ basic exercises (`ex1`–`ex4`) + Python test harness.

> Part of [IT003 – Nhập Môn Lập Trình](../README.md) homework repo.

## Contents

- `ex1.cpp` – Arithmetic mean `(a+b+c)/3` and geometric mean `cbrt(a*b*c)`
- `ex2.cpp` – Largest of three numbers
- `ex3.cpp` – Number classification: zero / positive-negative, even-odd
- `ex4.cpp` – Evaluate `ax^2 + bx + c`
- `test_taskC.py` – Builds with `g++` and checks all 4 exercises

## Build & Run

```bash
g++ -O2 -o ex1.exe ex1.cpp
g++ -O2 -o ex2.exe ex2.cpp
g++ -O2 -o ex3.exe ex3.cpp
g++ -O2 -o ex4.exe ex4.cpp

echo "3 4 5" | ./ex1.exe
echo "3 1 2" | ./ex2.exe
echo "7" | ./ex3.exe
printf "1 2 1\n2" | ./ex4.exe
```

Run all tests:

```bash
python test_taskC.py
```

## Author

**Bui Tan Thanh**
- 26531852@gm.uit.edu.vn
- https://buitanhthanh.uk
