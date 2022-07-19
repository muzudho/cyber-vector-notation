# cyber-number-notation

For those who use computers  

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

# Explanation

## Addition of the last two rules

* Ends with 1

```plaintext
O0      # Bad
O0o1    # Ok

O1      # Ok
O2      # Bad
O2o1    # Ok
```

* o1 cannot be placed after 1

```plaintext
O1o1          # Bad
O1o1o1        # Of course it's bad
O1o2o1        # OK
O1o11o1       # Of course it's OK

O1o2o1o2o1    # OK
O1o1o1o2o1    # Of course it's bad
```

## Let's give an example

```plaintext
O0o1
O1
O1o2o1
O2o1
O2o2o1
O3o1
O4o1
O4o2o1
O5o1
O5o2o1
O6o1
O7o1
O8o1
O9o1
OA10o1
OA11o1
OA12o1
OA13o1
OA50o1
OA97o1
OA98o1
OA99o1
OAA100o1
OAA100o2o1
OAA100o3o1
OAA100o8o1
OAA100o9o1
OAA100oA10o1
```

Now you have mastered cyber notation  

## Translation method

Add 1.1 to i.  
Add 1.1.1 to i.j.  
Add 1.1.1.1 to i.j.k.  

You may be disliked because the number changes  

### Example O2o1 For Chapters

```plaintext
# Real world
1.1 Fruits
1.1.1 Apple
1.2.1 Banana
1.11.1 Kiwi
1.2.1.2.1　Super banana
1.1.1.2.1 Super apple

# Cyber world
O2o2o1 Fruits
O2o2o2o1 Apple
O2o3o2o1 Banana
O2o12o2o1 Kiwi
O2o3o2o3o2o1 Super banana
O2o2o2o3o2o1 Super apple
```

### Example O3o1 For Version

```plaintext
# When the user sees
http://example.com/tic-tac-toe/v2.3/match-application/
                               ----
                               1
1. Version

# Local PC
C://This/Is/A/Path/tic_tac_toe/o3o4o1/views/match_application/__init__.py
                               ------
                               1
1. Version by Cyber number
```

👇 Conversion

```plaintext
  v2.3
+  1.1.1
--------
  o3o4o1
```

👇 Reverse conversion

```plaintext
  o3o4o1
-  1.1.1
--------
  v2.3
```
