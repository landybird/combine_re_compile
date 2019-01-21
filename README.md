# 任意组合 re.compile 

[![PyPI version](https://badge.fury.io/py/combine-re-compile.svg)](https://pypi.org/project/combine-re-compile/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


例如: 


匹配 `一个数字`的` re.compile` 表达式

```python

DIGIT_PATTERN = re.compile(r"""
    (?P<my_digit_pattern>        # start named group
      \d                         # 1  integer
    )                            # close named group
    """, re.VERBOSE)

```

匹配`一个字符`的 `re.compile `表达式

```python


CHAR_PATTERN = re.compile(r"""
    (?P<my_char_pattern>         # start named group
      [a-z]                      # a character
    )                            # close named group
    """, re.VERBOSE)


```

组合到一起:

```python

#  pip install combine_re_compile

from combine_re_compile import CombinationPattern

c = CombinationPattern(DIGIT_PATTERN,CHAR_PATTERN,CHAR_PATTERN,DIGIT_PATTERN, new_pattern_name="new_pattern_name" )
new_pattern = c.get_new_pattern

match_result = new_pattern.search("3d311dd1dsad3").group("new_pattern_name")
print(match_result)
# >> 1dd1


```







> 兼容环境

`Windows`/`Linux`/`MacOs`

<br>

### 1 安装

> pip 安装
```
$ pip install combine_re_compile
```

> 源码安装
```
 $ git clone https://github.com/landybird/combine_re_compile.git
 $ cd combine_re_compile
 $ python setup.py install
 ```

<br>

### 2 使用


```python


DIGIT_PATTERN = re.compile(r"""
    (?P<my_digit_pattern>        # start named group
      \d+                        # 1 or more integers
    )                            # close named group
    """, re.VERBOSE)



CHAR_PATTERN = re.compile(r"""
    (?P<my_char_pattern>         # start named group
      [a-z]                      # a character
    )                            # close named group
    """, re.VERBOSE)


CHARS_PATTERN = re.compile(r"""
    (?P<my_char_pattern>         # start named group
      [a-z]+                     # a character
    )                            # close named group
    """, re.VERBOSE)


r = CombinationPattern(DIGIT_PATTERN, CHAR_PATTERN, new_pattren_name="my_new_pattern").get_new_pattern

s = "213213as2312"
print(r.search(s).group('my_new_pattern')) # 分组名称

>> 213213a

```



### License

MIT [©landybird](https://github.com/landybird)
