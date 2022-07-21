# cyber-number-notation

This is a **"NOTATION"** for those who use computers  

Commentary by author:  

📖 [電脳記数法 (Cyber Number Notation)](https://crieit.net/posts/Cyber-Number-Notation)  

# Two prior knowledge

📖 [dictionary-ordinal-number-notation](https://github.com/muzudho/dictionary-ordinal-number-notation)  
📖 [beads-nested-number-notation](https://github.com/muzudho/beads-nested-number-notation)  

# Install

```shell
# pip install dicordnum
# pip install beadsnum
pip install cybernum
```

# Methods

## seed operation

👇 Append prefix "O" and suffix "o0"  

```plaintext
cn = CyberNum.seed(1)
print(f"{cn}")             # "O1o0"

cn = CyberNum.seed(2)
print(f"{cn}")             # "O2o0"
```

👇 Same  

```plaintext
seed("O1o2") == "OO1o2o0"
seed("O1o2o3") == "OO1o2o3o0"
```

## reap operation

👇 Remove prefix "O" and suffix "o0"  

```plaintext
reap("OO1o2o0") == "O1o2"
reap("OO1o2o3o0") == "O1o2o3"
```

👇 Fail  

```plaintext
reap("1o2o0")   # Not prefix "O"
reap("O1o2")    # Not suffix "o0"
```

## Let's give an example

👇 For Version number  

```plaintext
# Normal
Version 1.0.1

# Cyber
Version O1o0o1o0
```

👇 For IPv4  

```plaintext
# Normal
128.0.0.1

# Cyber
OAA128o0o0o1o0
```

👇 Folder

```plaintext
# Normal
📂 00
└── 📂 01
  └── 📂 99

# Normal Flat by "/"
00/01/99

# Cyber
📂 O0o0          # Not O00o0
└── 📂 O1o0
  └── 📂 OA99o0

# Cyber Flat by "x1x"
O0o0x1xO1o0x1xOA99o0
```

👇 Chapter

```plaintext
# Normal
1. Food
1.1. Fruits
1.1.1. Apple
1.1.2. Banana
1.1.11. Kiwi

# Cyber
O1o0. Food
O1o1o0. Fruits
O1o1o1o0. Apple
O1o1o2o0. Banana
O1o1oA11o0. Kiwi
```

👇 Negative number included  

```plaintext
# Normal
20, 18, -1, -14, 5

# Cyber
OA20oA18o_9o__86o5
```

Now you have mastered cyber notation  
