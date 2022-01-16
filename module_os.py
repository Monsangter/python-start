Last login: Sat Jan 15 22:03:28 on ttys000
(base) monsangter@monsangterui-MacBookPro ~ % python3
Python 3.9.7 (default, Sep 16 2021, 08:50:36)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/Users/monsangter'
>>> os.listdir()
['c++ project', '.config', 'Music', '.DS_Store', '.CFUserTextEncoding', '.xonshrc', '.zshrc', 'Pictures', '.zsh_history', 'Desktop', 'Library', '.matplotlib', '.android', 'PycharmProjects', 'Public', '.tcshrc', 'Movies', '.Trash', 'Documents', '.vscode', '.bash_profile', 'Downloads', '.gitconfig', '.zsh_sessions', '.conda']
>>> os.chdir('libs')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'libs'
>>> os.chdir('Library')
>>> ods.getcwd()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ods' is not defined
>>> os.getcwd()
'/Users/monsangter/Library'
>>> os.listdir()
['Application Support', 'Maps', 'Assistant', 'com.apple.appleaccountd', 'Autosave Information', 'Saved Application State', 'IdentityServices', 'WebKit', 'Calendars', 'Preferences', 'studentd', 'Staging', 'Messages', 'HomeKit', 'DES', 'Keychains', 'Sharing', 'ColorPickers', 'com.apple.WatchListKit', 'Application Scripts', 'Assistants', 'Translation', '.localized', 'Mail', 'Trial', 'Compositions', 'GameKit', 'LanguageModeling', 'Favorites', 'Contacts', 'Passes', 'com.apple.icloud.searchpartyd', 'SafariSandboxBroker', 'FontCollections', 'Sounds', 'DuetExpertCenter', 'HTTPStorages', 'com.apple.internal.ck', 'Printers', 'SyncedPreferences', 'Audio', 'Keyboard Layouts', 'DataDeliveryServices', 'Logs', 'Internet Plug-Ins', 'FrontBoard', 'Accounts', 'Safari', 'Colors', 'Biome', 'PreferencePanes', 'Shortcuts', 'Mobile Documents', 'Suggestions', 'Weather', 'Group Containers', 'Containers', 'ContainerManager', 'PersonalizationPortrait', 'Photos', 'Fonts', 'KeyboardServices', 'Metadata', 'Screen Savers', 'CallServices', 'Spelling', 'SafariSafeBrowsing', 'Reminders', 'Input Methods', 'Cookies', 'Services', 'GroupContainersAlias', 'com.apple.bluetooth.services.cloud', 'Keyboard', 'CoreFollowUp', 'StatusKit', 'DoNotDisturb', 'Caches', 'PythonWrapper']
>>> os.chdir('..')
>>> os.getcwd()
'/Users/monsangter'
>>>
