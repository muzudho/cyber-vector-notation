# cyber-number-notation

This is a **"NOTATION"** for those who use computers  

Commentary by author:  

📖 [電脳記数法 (Cyber Number Notation)](https://crieit.net/posts/Cyber-Number-Notation)  

# Two prior knowledge

📖 [dictionary-ordinal-number-notation](https://github.com/muzudho/dictionary-ordinal-number-notation)  
📖 [beads-vector-notation](https://github.com/muzudho/beads-vector-notation)  

# Install

```shell
# pip install dicordnum
# pip install beadsvec
pip install cybernum
```

# Methods

## be_accurate() operation

👇 Append `,0`  

```plaintext
cn = CyberNum.be_accurate((1, 2))
print(f"{cn.elements}")                # (1, 2, 0)

cn = CyberNum.be_accurate(3)
print(f"{cn.elements}")                # (3, 0)
```

👇 Same  

```plaintext
cn = CyberNum((1, 2, 0))
print(f"{cn.elements}")                # (1, 2, 0)

cn = CyberNum((3, 0))
print(f"{cn.elements}")                # (3, 0)
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

# **TODO** Cyber Flat by "x1x"
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
