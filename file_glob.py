Last login: Tue Jan 18 09:08:01 on console
Restored session: Mon Jan 17 22:26:53 KST 2022
(base) monsangter@monsangterui-MacBookPro ~ % import os
zsh: command not found: import
(base) monsangter@monsangterui-MacBookPro ~ % os.path.exists('users')
zsh: unknown username 'er'
(base) monsangter@monsangterui-MacBookPro ~ % python3
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.path.exists('users')
False
>>> cd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cd' is not defined
>>> cwd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cwd' is not defined
>>> quit()
(base) monsangter@monsangterui-MacBookPro ~ % python3
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> cwd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cwd' is not defined
>>> import os
>>> os.getcwd()
'/Users/monsangter'
>>> os.listdir()
['c++ project', '.config', 'Music', '.DS_Store', '.CFUserTextEncoding', '.xonshrc', '.zshrc', 'Pictures', '.zsh_history', 'Desktop', 'Library', '.matplotlib', '.android', 'PycharmProjects', 'Public', '.tcshrc', 'Movies', '.Trash', 'Documents', '.vscode', '.bash_profile', 'Downloads', '.python_history', '.gitconfig', '.zsh_sessions', '.conda']
>>> os.chdir('PycharmProjects')
>>> os.listdir()
['.DS_Store', 'python-start', 'pythonProject']
>>> os.chdir('python-start')
>>> os.listdir()
['for_squarelist.py', 'module_random.py', 'listrange.py', 'while_ball.py', 'datatype_bool.py', 'letter.rtf', 'module_math.py', 'file_write.py', 'file_letterwrite.py', 'str_split.py', 'tuple.py', 'module_tkinter.py', 'def_printlist.py', 'ret_f2.py', 'file_englishquiz.py', '.DS_Store', 'ret_koreannumber.py', 'list.py', 'if_remainder.py', 'ret_koreanage.py', 'str_find.py', 'file_letterawrite.py', 'module_re.py', 'module.righttriangle.py', 'while_input.py', 'rev.py', 'def_compare.py', 'ret_comintamount.py', 'file_text^^.py', 'tuple_tomorrow_.py', 'ret_triple.py', 'datatype_palindrome.py', 'lambda.py', 'module_calendar.py', 'virable.py', 'ret_judge.py', 'dict_keyread.py', 'file_secretmessage.py', 'lam_filter.py', 'module_webbrowser.py', 'def_turtle.py', 'strlist_change.py', 'def_noneparameter.py', 'if_number.py', 'file_pickle.py', 'module_import.py', 'if_break.py', 'tkinterwindows.py', 'listbb.py', 'datatype_palindromev2.py', 'datatype_dict.py', 'for_rangelist.py', 'datatype_set.py', 'list_reportcard.py', 'ko_en.txt', 'var_global.py', 'ret_siminterest.py', 'for_repeat.py', 'lam_map.py', 'if_plus.py', 'module_calendartkinter.py', 'module_os.py', 'if_leapyear.py', 'users', 'elif.py', 'file_glob.py', 'set_dice.py', 'strlist_leafbranch.py', 'dict_mentaldisorderx.py', 'module_usage.py', 'tkinterlabelusage.py', 'str_add.py', 'ret_f1.py', 'dict.py', 'datatype.py', 'strlist_sumofdigitsnonrecursive.py', 'tkinterprac.py', 'venv', 'square.py', '.git', 'tkinterpractice.py', 'tkinterwidget.py', 'lam_reduce.py', 'set.py', 'file_textdevide.py', 'for_chemLab.py', 'ret_tri.py', 'list_char.py', 'for_leng.py', 'def_gugu.py', 'strlist_sumofdigits.py', 'ret_simintamount.py', 'strlist_primenumber.py', 'module_sys.py', 'python_for_Fun.rtf', 'while_square.py', 'var_local.py', '.idea', 'if.py', 'stringslice.py']
>>> from glob import glob
>>> glob('*.exe')
[]
>>> glob('*.py')
['for_squarelist.py', 'module_random.py', 'listrange.py', 'while_ball.py', 'datatype_bool.py', 'module_math.py', 'file_write.py', 'file_letterwrite.py', 'str_split.py', 'tuple.py', 'module_tkinter.py', 'def_printlist.py', 'ret_f2.py', 'file_englishquiz.py', 'ret_koreannumber.py', 'list.py', 'if_remainder.py', 'ret_koreanage.py', 'str_find.py', 'file_letterawrite.py', 'module_re.py', 'module.righttriangle.py', 'while_input.py', 'rev.py', 'def_compare.py', 'ret_comintamount.py', 'file_text^^.py', 'tuple_tomorrow_.py', 'ret_triple.py', 'datatype_palindrome.py', 'lambda.py', 'module_calendar.py', 'virable.py', 'ret_judge.py', 'dict_keyread.py', 'file_secretmessage.py', 'lam_filter.py', 'module_webbrowser.py', 'def_turtle.py', 'strlist_change.py', 'def_noneparameter.py', 'if_number.py', 'file_pickle.py', 'module_import.py', 'if_break.py', 'tkinterwindows.py', 'listbb.py', 'datatype_palindromev2.py', 'datatype_dict.py', 'for_rangelist.py', 'datatype_set.py', 'list_reportcard.py', 'var_global.py', 'ret_siminterest.py', 'for_repeat.py', 'lam_map.py', 'if_plus.py', 'module_calendartkinter.py', 'module_os.py', 'if_leapyear.py', 'elif.py', 'file_glob.py', 'set_dice.py', 'strlist_leafbranch.py', 'dict_mentaldisorderx.py', 'module_usage.py', 'tkinterlabelusage.py', 'str_add.py', 'ret_f1.py', 'dict.py', 'datatype.py', 'strlist_sumofdigitsnonrecursive.py', 'tkinterprac.py', 'square.py', 'tkinterpractice.py', 'tkinterwidget.py', 'lam_reduce.py', 'set.py', 'file_textdevide.py', 'for_chemLab.py', 'ret_tri.py', 'list_char.py', 'for_leng.py', 'def_gugu.py', 'strlist_sumofdigits.py', 'ret_simintamount.py', 'strlist_primenumber.py', 'module_sys.py', 'while_square.py', 'var_local.py', 'if.py', 'stringslice.py']
>>> glob(r'\U*')
[]
>>> from os.path import isdir
>>> for x in glob('*')
  File "<stdin>", line 1
    for x in glob('*')
                      ^
SyntaxError: invalid syntax
>>> for x in glob('*'):
...     if isdir(x):
...             print(x, '<DIR>')
...     else:
...             print(x)
... 
for_squarelist.py
module_random.py
listrange.py
while_ball.py
datatype_bool.py
letter.rtf
module_math.py
file_write.py
file_letterwrite.py
str_split.py
tuple.py
module_tkinter.py
def_printlist.py
ret_f2.py
file_englishquiz.py
ret_koreannumber.py
list.py
if_remainder.py
ret_koreanage.py
str_find.py
file_letterawrite.py
module_re.py
module.righttriangle.py
while_input.py
rev.py
def_compare.py
ret_comintamount.py
file_text^^.py
tuple_tomorrow_.py
ret_triple.py
datatype_palindrome.py
lambda.py
module_calendar.py
virable.py
ret_judge.py
dict_keyread.py
file_secretmessage.py
lam_filter.py
module_webbrowser.py
def_turtle.py
strlist_change.py
def_noneparameter.py
if_number.py
file_pickle.py
module_import.py
if_break.py
tkinterwindows.py
listbb.py
datatype_palindromev2.py
datatype_dict.py
for_rangelist.py
datatype_set.py
list_reportcard.py
ko_en.txt
var_global.py
ret_siminterest.py
for_repeat.py
lam_map.py
if_plus.py
module_calendartkinter.py
module_os.py
if_leapyear.py
users
elif.py
file_glob.py
set_dice.py
strlist_leafbranch.py
dict_mentaldisorderx.py
module_usage.py
tkinterlabelusage.py
str_add.py
ret_f1.py
dict.py
datatype.py
strlist_sumofdigitsnonrecursive.py
tkinterprac.py
venv <DIR>
square.py
tkinterpractice.py
tkinterwidget.py
lam_reduce.py
set.py
file_textdevide.py
for_chemLab.py
ret_tri.py
list_char.py
for_leng.py
def_gugu.py
strlist_sumofdigits.py
ret_simintamount.py
strlist_primenumber.py
module_sys.py
python_for_Fun.rtf
while_square.py
var_local.py
if.py
stringslice.py
>>> 