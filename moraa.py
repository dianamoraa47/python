Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> code="abc123"
>>> name="moraa"
>>> balance="2500"
>>> 
>>> print("{}confirmed\n,it is {}\n,your balance is{}\n,thank you."format(code,name,balance))
SyntaxError: invalid syntax
>>> print("{}confirmed\n, it is{}\n, your balance is{}\n, thank you.".format(code,name,balance))
abc123confirmed
, it ismoraa
, your balance is2500
, thank you.
>>> s="akirachix"
>>> s(0)

>>> s{0}

>>> s[0]
'a'
>>> s[1]
'k'
>>> s[2]
'i'
>>> s[3]
'r'
>>> s[4]
'a'
>>> s[a;2]
SyntaxError: invalid syntax
>>> s[a:2]

>>> s[2:6]
'irac'
>>> s[7:8]
'i'
>>> s[8:8]
''
>>> s[3:8]
'rachi'
>>> s[0:8]
'akirachi'
>>> s[3:]
'rachix'
>>> s[:6]
'akirac'
>>> s[0:6]
'akirac'
>>> s[0:]
'akirachix'
>>> s[0:10]
'akirachix'
>>> s[-9]
'a'
>>> s[0]
'a'
>>> s[-8]
'k'
>>> s[-9:-7]
'ak'
>>> s[-7:-1]
'irachi'
>>> s[-9:-1]
'akirachi'
>>> s[-9:]
'akirachix'
>>> s[-4:]
'chix'
>>> s[:-1]
'akirachi'
>>> s.index("k")
1
>>> s.index("i")
2
>>> s.index("rachix")
3
>>> sms="abcd123. confirmed! hi moraa, your balance is 2500"
>>> sms[0:6]
'abcd12'
>>> sms[0:7]
'abcd123'
>>> sms[0:1]
'a'
>>> sms=[7:10]

>>> sms[0:7]
'abcd123'
>>> sms[19:25]
' hi mo'
>>> sms[20:24]
'hi m'
>>> sms[20:28]
'hi moraa'
>>> sms[39:45]
'nce is'
>>> sms[45:50]
' 2500'
>>> sms[0:7]
'abcd123'
>>> sms[7:17]
'. confirme'
>>> code[0:7]
'abc123'
>>> name[28:32]
''
>>> name
'moraa'
>>> balance[45:50]
''
>>> balance
'2500'
>>> sms=upper[0:7]

>>> 
>>> sms.upper()
'ABCD123. CONFIRMED! HI MORAA, YOUR BALANCE IS 2500'
>>> sms.lower()
'abcd123. confirmed! hi moraa, your balance is 2500'
>>> sms.endswith"x"
SyntaxError: invalid syntax
>>> sms.endswith"0"

>>> sms.endswith 0

>>> sms.endswith("0")
True
>>> len(sms)
50
>>> len(akirachix)

>>> len(s)
9
>>> sms.split
<built-in method split of str object at 0x03573CF0>
>>> sms.split()
['abcd123.', 'confirmed!', 'hi', 'moraa,', 'your', 'balance', 'is', '2500']
>>> akirachix.split()

>>> s.split()
['akirachix']
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> "modules"

Please wait a moment while I gather a list of all available modules...

__future__          atexit              http                sched
__main__            audioop             hyperparser         scrolledlist
_abc                autocomplete        idle                search
_ast                autocomplete_w      idle_test           searchbase
_asyncio            autoexpand          idlelib             searchengine
_bisect             base64              imaplib             secrets
_blake2             bdb                 imghdr              select
_bootlocale         binascii            imp                 selectors
_bz2                binhex              importlib           setuptools
_codecs             bisect              inspect             shelve
_codecs_cn          browser             io                  shlex
_codecs_hk          builtins            iomenu              shutil
_codecs_iso2022     bz2                 ipaddress           signal
_codecs_jp          cProfile            itertools           site
_codecs_kr          calendar            json                smtpd
_codecs_tw          calltip             keyword             smtplib
_collections        calltip_w           lib2to3             sndhdr
_collections_abc    cgi                 linecache           socket
_compat_pickle      cgitb               locale              socketserver
_compression        chunk               logging             sqlite3
_contextvars        cmath               lzma                squeezer
_csv                cmd                 macosx              sre_compile
_ctypes             code                macpath             sre_constants
_ctypes_test        codecontext         mailbox             sre_parse
_datetime           codecs              mailcap             ssl
_decimal            codeop              mainmenu            stackviewer
_dummy_thread       collections         marshal             stat
_elementtree        colorizer           math                statistics
_functools          colorsys            mimetypes           statusbar
_hashlib            compileall          mmap                string
_heapq              concurrent          modulefinder        stringprep
_imp                config              msilib              struct
_io                 config_key          msvcrt              subprocess
_json               configdialog        multicall           sunau
_locale             configparser        multiprocessing     symbol
_lsprof             contextlib          netrc               symtable
_lzma               contextvars         nntplib             sys
_markupbase         copy                nt                  sysconfig
_md5                copyreg             ntpath              tabnanny
_msi                crypt               nturl2path          tarfile
_multibytecodec     csv                 numbers             telnetlib
_multiprocessing    ctypes              opcode              tempfile
_opcode             curses              operator            test
_operator           dataclasses         optparse            textview
_osx_support        datetime            os                  textwrap
_overlapped         dbm                 outwin              this
_pickle             debugger            paragraph           thono
_py_abc             debugger_r          parenmatch          threading
_pydecimal          debugobj            parser              time
_pyio               debugobj_r          pathbrowser         timeit
_queue              decimal             pathlib             tkinter
_random             delegator           pdb                 token
_sha1               difflib             percolator          tokenize
_sha256             dis                 pickle              tooltip
_sha3               distutils           pickletools         trace
_sha512             doctest             pip                 traceback
_signal             dummy_threading     pipes               tracemalloc
_sitebuiltins       dynoption           pkg_resources       tree
_socket             easy_install        pkgutil             tty
_sqlite3            editor              platform            turtle
_sre                email               plistlib            turtledemo
_ssl                encodings           poplib              types
_stat               ensurepip           posixpath           typing
_string             enum                pprint              undo
_strptime           errno               profile             unicodedata
_struct             faulthandler        pstats              unittest
_symtable           filecmp             pty                 urllib
_testbuffer         fileinput           py_compile          uu
_testcapi           filelist            pyclbr              uuid
_testconsole        fnmatch             pydoc               venv
_testimportmultiple formatter           pydoc_data          warnings
_testmultiphase     fractions           pyexpat             wave
_thread             ftplib              pyparse             weakref
_threading_local    functools           pyshell             webbrowser
_tkinter            gc                  pytho               window
_tracemalloc        genericpath         query               winreg
_warnings           getopt              queue               winsound
_weakref            getpass             quopri              wsgiref
_weakrefset         gettext             random              xdrlib
_winapi             glob                re                  xml
abc                 grep                redirector          xmlrpc
aifc                gzip                replace             xxsubtype
antigravity         hashlib             reprlib             zipapp
argparse            heapq               rlcompleter         zipfile
array               help                rpc                 zipimport
ast                 help_about          rstrip              zlib
asynchat            history             run                 zoomheight
asyncio             hmac                runpy               zzdummy
asyncore            html                runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 
