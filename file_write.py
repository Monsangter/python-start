Last login: Sun Jan 16 22:03:11 on ttys000
(base) monsangter@monsangterui-MacBookPro ~ % python3
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import re, glob
>>> p = re.comile('.*p.*n.*')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 're' has no attribute 'comile'
>>> p = re.compile('.*p.*.n.*')
>>> for i in glob.glob('*'):
...     m = p.match(i)
...     if m:
...             print m.group()
  File "<stdin>", line 4
    print m.group()
          ^
SyntaxError: invalid syntax
>>> quit()
(base) monsangter@monsangterui-MacBookPro ~ % python3
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
(base) monsangter@monsangterui-MacBookPro ~ % conda install -c anaconda tk
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/anaconda3

  added / updated specs:
    - tk


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-4.11.0               |   py39hecd8cb5_0        14.4 MB
    ------------------------------------------------------------
                                           Total:        14.4 MB

The following packages will be UPDATED:

  conda                               4.10.3-py39hecd8cb5_0 --> 4.11.0-py39hecd8cb5_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-4.11.0         | 14.4 MB   | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(base) monsangter@monsangterui-MacBookPro ~ % 
  [Restored Jan 17, 2022 12:43:12 PM]
Last login: Mon Jan 17 12:43:09 on console
Restored session: Sun Jan 16 22:53:56 KST 2022
(base) monsangter@monsangterui-MacBookPro ~ % python3
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/Users/monsangter'
>>> os.listdir()
['c++ project', '.config', 'Music', '.DS_Store', '.CFUserTextEncoding', '.xonshrc', '.zshrc', 'Pictures', '.zsh_history', 'Desktop', 'Library', '.matplotlib', '.android', 'PycharmProjects', 'Public', '.tcshrc', 'Movies', '.Trash', 'Documents', '.vscode', '.bash_profile', 'Downloads', '.python_history', '.gitconfig', '.zsh_sessions', '.conda']
>>> os.chdir('Library')
>>> os.listdir()
['Application Support', 'Maps', 'Assistant', 'com.apple.appleaccountd', 'Autosave Information', 'Saved Application State', 'IdentityServices', 'WebKit', 'Calendars', 'Preferences', 'studentd', 'Staging', 'Messages', 'HomeKit', 'DES', 'Keychains', 'Sharing', 'ColorPickers', 'com.apple.WatchListKit', 'Application Scripts', 'Assistants', 'Translation', '.localized', 'Mail', 'Trial', 'Compositions', 'GameKit', 'LanguageModeling', 'Favorites', 'Contacts', 'Passes', 'com.apple.icloud.searchpartyd', 'SafariSandboxBroker', 'FontCollections', 'Sounds', 'DuetExpertCenter', 'HTTPStorages', 'com.apple.internal.ck', 'Printers', 'SyncedPreferences', 'Audio', 'Keyboard Layouts', 'DataDeliveryServices', 'Logs', 'Internet Plug-Ins', 'FrontBoard', 'Accounts', 'Safari', 'Colors', 'Biome', 'PreferencePanes', 'Shortcuts', 'Mobile Documents', 'Suggestions', 'Weather', 'Group Containers', 'Containers', 'ContainerManager', 'PersonalizationPortrait', 'Photos', 'Fonts', 'KeyboardServices', 'Metadata', 'Screen Savers', 'CallServices', 'Spelling', 'SafariSafeBrowsing', 'Reminders', 'Input Methods', 'Cookies', 'Services', 'GroupContainersAlias', 'com.apple.bluetooth.services.cloud', 'Keyboard', 'CoreFollowUp', 'StatusKit', 'DoNotDisturb', 'Caches', 'PythonWrapper']
>>> os.chdir('Python')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'Python'
>>> import sys
>>> print(os.path.dirname(sys.executable))
/opt/anaconda3/bin
>>> chdir('opt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chdir' is not defined
>>> quit()
(base) monsangter@monsangterui-MacBookPro ~ % python3
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> dirlist()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dirlist' is not defined
>>> import os
>>> os.listdir()
['c++ project', '.config', 'Music', '.DS_Store', '.CFUserTextEncoding', '.xonshrc', '.zshrc', 'Pictures', '.zsh_history', 'Desktop', 'Library', '.matplotlib', '.android', 'PycharmProjects', 'Public', '.tcshrc', 'Movies', '.Trash', 'Documents', '.vscode', '.bash_profile', 'Downloads', '.python_history', '.gitconfig', '.zsh_sessions', '.conda']
>>> os.chdir('PycharmProjects')
>>> os.listdir
<built-in function listdir>
>>> os.listdir()
['.DS_Store', 'python-start', 'pythonProject']
>>> os.chdir('python-start')
>>> os.listdir()
['for_squarelist.py', 'module_random.py', 'listrange.py', 'while_ball.py', 'datatype_bool.py', 'letter.rtf', 'module_math.py', 'file_write.py', 'file_letterwrite.py', 'str_split.py', 'tuple.py', 'module_tkinter.py', 'def_printlist.py', 'ret_f2.py', '.DS_Store', 'ret_koreannumber.py', 'list.py', 'if_remainder.py', 'ret_koreanage.py', 'str_find.py', 'file_letterawrite.py', 'module_re.py', 'module.righttriangle.py', 'while_input.py', 'rev.py', 'def_compare.py', 'ret_comintamount.py', 'file_text^^.py', 'tuple_tomorrow_.py', 'ret_triple.py', 'datatype_palindrome.py', 'lambda.py', 'module_calendar.py', 'virable.py', 'ret_judge.py', 'dict_keyread.py', 'lam_filter.py', 'module_webbrowser.py', 'def_turtle.py', 'strlist_change.py', 'def_noneparameter.py', 'if_number.py', 'module_import.py', 'if_break.py', 'tkinterwindows.py', 'listbb.py', 'datatype_palindromev2.py', 'datatype_dict.py', 'for_rangelist.py', 'datatype_set.py', 'list_reportcard.py', 'var_global.py', 'ret_siminterest.py', 'for_repeat.py', 'lam_map.py', 'if_plus.py', 'module_calendartkinter.py', 'module_os.py', 'if_leapyear.py', 'elif.py', 'set_dice.py', 'strlist_leafbranch.py', 'dict_mentaldisorderx.py', 'module_usage.py', 'tkinterlabelusage.py', 'str_add.py', 'ret_f1.py', 'dict.py', 'datatype.py', 'strlist_sumofdigitsnonrecursive.py', 'tkinterprac.py', 'venv', 'square.py', '.git', 'tkinterpractice.py', 'tkinterwidget.py', 'lam_reduce.py', 'set.py', 'for_chemLab.py', 'ret_tri.py', 'list_char.py', 'for_leng.py', 'def_gugu.py', 'strlist_sumofdigits.py', 'ret_simintamount.py', 'strlist_primenumber.py', 'module_sys.py', 'python_for_Fun.rtf', 'while_square.py', 'var_local.py', '.idea', 'if.py', 'stringslice.py']
>>> os.chdir('venv')
>>> os.listdir('lib')
['.DS_Store', 'python3.8']
>>> os.chdir('lib')
>>> os.chdir('python3.8')
>>> os.listdir()
['.DS_Store', 'site-packages']
>>> os.chdir('site-packages')
>>> os.listdir()
['wheel-0.36.2.dist-info', '.DS_Store', 'setuptools-57.0.0.virtualenv', 'wheel', 'pip-21.1.2.virtualenv', 'pip', '_virtualenv.py', 'distutils-precedence.pth', '_virtualenv.pth', 'wheel-0.36.2.virtualenv', 'setuptools', 'pkg_resources', 'setuptools-57.0.0.dist-info', '_distutils_hack', 'pip-21.1.2.dist-info']
>>> os.chdir('wheel-0.36.2.dist-info')
>>> f = open('LICENSE.txt')
>>> f.readline()
'"wheel" copyright (c) 2012-2014 Daniel Holth <dholth@fastmail.fm> and\n'
>>> f.readline()
'contributors.\n'
>>> for x in range(5):
...     f.readline()
... 
'\n'
'The MIT License\n'
'\n'
'Permission is hereby granted, free of charge, to any person obtaining a\n'
'copy of this software and associated documentation files (the "Software"),\n'
>>> f = open('LICENSE.txt')
>>> lines = f.readlines()
>>> lines[:2]
['"wheel" copyright (c) 2012-2014 Daniel Holth <dholth@fastmail.fm> and\n', 'contributors.\n']
>>> lines[-10:-1]
['in all copies or substantial portions of the Software.\n', '\n', 'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n', 'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n', 'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\n', 'THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR\n', 'OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\n', 'ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR\n', 'OTHER DEALINGS IN THE SOFTWARE.\n']
>>> lines[-1:-10
... 
... 
... lines[-1:-10]
  File "<stdin>", line 4
    lines[-1:-10]
    ^
SyntaxError: invalid syntax
>>> lines[-1:-10]
[]
>>> 