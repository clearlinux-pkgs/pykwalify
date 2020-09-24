#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pykwalify
Version  : 1.7.0
Release  : 6
URL      : https://github.com/Grokzen/pykwalify/releases/download/1.7.0/pykwalify-1.7.0.tar.gz
Source0  : https://github.com/Grokzen/pykwalify/releases/download/1.7.0/pykwalify-1.7.0.tar.gz
Summary  : Python lib/cli for JSON/YAML schema validation
Group    : Development/Tools
License  : MIT
Requires: pykwalify-bin = %{version}-%{release}
Requires: pykwalify-license = %{version}-%{release}
Requires: pykwalify-python = %{version}-%{release}
Requires: pykwalify-python3 = %{version}-%{release}
Requires: PyYAML
Requires: docopt
Requires: python-dateutil
Requires: ruamel.yaml
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : docopt
BuildRequires : python-dateutil
BuildRequires : ruamel.yaml

%description
# pyKwalify

YAML/JSON validation library

This framework is a port with a lot of added functionality of the Java version of the framework kwalify that can be found at http://www.kuwata-lab.com/kwalify/

The original source code can be found at http://sourceforge.net/projects/kwalify/files/kwalify-java/0.5.1/

The source code of the latest release that has been used can be found at https://github.com/sunaku/kwalify. Please note that source code is not the original authors code but a fork/upload of the last release available in Ruby.

The schema this library is based on and extended from: http://www.kuwata-lab.com/kwalify/ruby/users-guide.01.html#schema


# Usage

Create a data file. `Json` and `Yaml` formats are both supported.

```yaml
- foo
- bar
```

Create a schema file with validation rules.

```yaml
type: seq
sequence:
  - type: str
```

Run validation from cli.

```bash
pykwalify -d data.yaml -s schema.yaml
```


## Examples

The documentation describes in detail how each keyword and type works and what is possible in each case.

But there is a lot of real world examples that can be found in the test data/files. It shows a lot of examples of how all keywords and types work in practice and in combination with each other.

The files can be found here and show both schema/data combinations that will work and that will fail.

 - `tests/files/success/`
 - `tests/files/fail/`
 - `tests/files/partial_schemas/`


# PyYaml and ruamel.yaml

`PyYaml` is the default installed YAML parser and `ruamel.yaml` is possible to install at the same time with the following command

```bash
pip install 'pykwalify[ruamel]'

# or for development:

pip install -e '.[ruamel]'
```

`ruamel.yaml` will however be used if both are installed because it is more up to date and includes the YAML 1.2 specification that `PyYaml` does not support.

`PyYaml` will still be the default parser because it is used more and is still considered the default `YAML` parser in the Python world.

Depending on how both libraries are developed, this can change in the future in any major update.



## UTF-8 and data encoding

If you have problems with unicode values not working properly when running pykwalify on Python 2.7.x then try to add this environment variable to your execution:

```
PYTHONIOENCODING=UTF-8 pykwalify ...
```

and it might help to force UTF-8 encoding on all string objects. If this does not work please open up an issue with your schema and data that can be used to track down the problem in the source code.


# Project details

|   |   |
|---|---|
| python support         | 2.7, 3.5, 3.6, 3.7 |
| Source                 | https://github.com/Grokzen/pykwalify |
| Docs (Latest release)  | http://pykwalify.readthedocs.io/en/master/ |
| Docs (Unstable branch) | http://pykwalify.readthedocs.io/en/unstable/ |
| Gitter (Free Chat)     | [![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/Grokzen/pykwalify?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) |
| Changelog              | https://github.com/Grokzen/pykwalify/blob/unstable/docs/release-notes.rst |
| Upgrade instructions   | https://github.com/Grokzen/pykwalify/blob/unstable/docs/upgrade-instructions.rst |
| Issues                 | https://github.com/Grokzen/pykwalify/issues |
| Travis (master)        | [![Build Status](https://travis-ci.org/Grokzen/pykwalify.svg?branch=master)](https://travis-ci.org/Grokzen/pykwalify) https://travis-ci.org/Grokzen/pykwalify |
| Travis (unstable)      | [![Build Status](https://travis-ci.org/Grokzen/pykwalify.svg?branch=unstable)](https://travis-ci.org/Grokzen/pykwalify) https://travis-ci.org/Grokzen/pykwalify |
| Test coverage          | [![Coverage Status](https://coveralls.io/repos/Grokzen/pykwalify/badge.png?branch=master)](https://coveralls.io/r/Grokzen/pykwalify) https://coveralls.io/github/Grokzen/pykwalify |
| pypi                   | https://pypi.python.org/pypi/pykwalify/ |
| Open Hub               | https://www.openhub.net/p/pykwalify |
| License                | `MIT` https://github.com/Grokzen/pykwalify/blob/unstable/docs/license.rst |
| Copyright              | `Copyright (c) 2013-2017 Johan Andersson` |
| git repo               | `git clone git@github.com:Grokzen/pykwalify.git` |
| install stable         | `pip install pykwalify` |
| install dev            | `$ git clone git@github.com:Grokzen/pykwalify.git pykwalify`<br>`$ cd ./pykwalify`<br>`$ virtualenv .venv`<br>`$ source .venv/bin/activate`<br>`$ pip install -r dev-requirements.txt`<br>`$ pip install -e .` |
| required dependencies  | `docopt >= 0.6.2`<br> `python-dateutil >= 2.4.2` |
| supported yml parsers  | `PyYaml >= 3.11`<br>`ruamel.yaml >= 0.11.0` |


Release Notes
=============

1.7.0 (October 3, 2018)
-----------------------

**IMPORTANT** LICENSE UPDATE **IMPORTANT**

- In this release there was a line removed from the license file. It was modified in the following commit
  (cc4e31b39ff4cce2dfbc662baa6469470dd3c033 Wed Oct 3 16:20:59 2018 +0200) and will be the main reason for
  the 1.7.0 release. All commits and tags and releases (1.6.1 and all releases before it) prior to this commit will
  use the old license that includes the change done in the above mentioned commit. Only release 1.7.0 and commits past
  this point will use the new/updated license file. 

General changes:

- Dropped support for python 3.3 and 3.4


1.6.1 (March 13, 2018)
--------------------

New keywords:

- Added support for keyword *nullable*. It is now possible to allow for a key not to be empty, when *required* keyword is not used.
- Added support for keyword *class*. It will not cause any validation errors, but serves to make kwalify schemas compatible that uses that keywork.

Bug fixes:

- Improved compatibility with unicodes to validate as strings.

Changed behaviour:

- Propergate json and yaml loading errors when used from the cli to the user for easier debugging.

General changes:

- Allow ruamel.yaml versions up to 0.16
- License is now bundled with the built release.


1.6.0 (Jan 22, 2017)
--------------------

New keywords:

- Add support for keyword *example*. It does nothing and have no validation done on it.
- Add support for keyword *version*. It does nothing and have no validation done on it.
- Add support for keyword *date* and added support keyword *format*. This can be used to validate many different types of *datetime* objects.
- Add support for keyword *length*. It is very similar to *range* but works primarily string types.
- Add support for keyword *assert*. It works by running the python code *assert <assert-expr>* and check if any exception is raised.
  This feature is considered dangerouns becuase there is only simple logic to prevent escaping out from validation.

Bug fixes:

- Fixed a bug where regexes marked as 'required' in a map were matched as strings, rather than regexes.
- Fixed a bug where the type validation did not work when schema specefied a sequence of map objects. It now outputs a proper `...is not a dict...` error instead.
- Fixed a bug in *unique* validation when a key that it tried to lookup in the data would not exists.
  Now it just ignores that it did not find any value becuase a missing value do not impact validation.
- Fixed a bug with keyword *ident* when the rule value was verified to be a *boolean*. It now only accepts *boolean* values as expected.
- Fixed a bug where if *allowempty* was specefied in a mapping type inside a sequence type then it would not properly validate.
- Fixed a bug where loaded extensions would not allways work in complex & nested objects.
- Fixed a major bug in very nested *seq* schemas where if the schema expected another *seq* but the value was something else it would not raise it as a validation error.
  This has now been fixed and now raises the proper error.
- Fixed a bug where include directive would not work in all cases when used inside a key in a mapping block.

New features:

- It is now possible to specify a default rule when using a mapping.
  The rule will be used whenever no other key could be found.
  This is a port of a missing feature from original kwalify implementation.
- Added new helper method *keywords* to *Rule* class that can output all active keywords for any *Rule* object.
  This helps when debugging code to be able to easily dump what all active keywords for any *Rule* object.
- Added new cli flag *--strict-rule-validation* that will validate that all used keywords in all *Rule* objects only uses the rules that is supported by each defined type.
  If you only use a *Core* object then set *strict_rule_validation=True* when creating the *Core* object instance.
  This feature is opt-in in this releaes but will be mandatory in *releases >= 1.7.0*.
- Added new cli flag *--fix-ruby-style-regex* that will trim slashes from ruby style regex/patterns.
  When using this flag the first and last */* will be trimmed of the pattern before running validation.
  If you only use a *Core* object then set *fix_ruby_style_regex=True* when creating the *Core* object instance.
  Default behaviour will still be that you should use python style regex values but this flag can help in some cases when you can't change the schema.
- Added new cli flag *--allow-assertions* that will enable the otherwise blocked keyword *assert*.
  This flag was introduced so that pykwalify would not assert assertions without user controll.
  Default behaviour will be to raise a *CoreError* is assertion is used but not allowed explicitly.
  If you only use a *Core* object then set *allow_assertions=True* when creating the *Core* object instance.

Changed behaviour:

- Removed the force of *UTF-8* encoding when importing pykwalify package. It caused issues with *jypiter notebooks* on python 2.7.x
  Added documentation in Readme regarding the suggested solution to use *PYTHONIOENCODING=UTF-8* if the default solution do not work.
- Validation do no longer continue to process things like *pattern*, *regex*, *timestamp*, *range* and other additional checks 
  if the type check fails. This can cause problems where previous errors will now initially be silenced when the typecheck for
  that value fails, but reappear again when the type check is fixed. (sbrunner)
- Catches *TypeError* when doing regex validation. That happens when the value is not a parsable string type.
- Checking that the value is a valid dict object is now done even if the mapping keyword is not specefied in the schema.
  This makes that check more eager and errors can apear that previously was not there.
- Changed the sane default type if that key is not defined to be *str*. Before this, type had to be defined every time and the default type did not work as expected.
  This is a major change and can cause validation to either fail or to stop failing depending on the case.
- Changed validation for if a value is required and a value in a list for example is *None*. It now adds a normal validation errors instead of raising a *CoreError*.
- Value for keyword *desc* now *MUST* be a string or a *RuleError* will be raised.
- Value for keyword *example* now *MUST* be a string or a *RuleError* will be raised.
- Value for keyword *name* now *MUST* be a string or a *RuleError* will be raised.

General changes:

- Ported alot of testcases directly from *Kwalify* test data (*test-validator.yaml -> 30f.yaml & 43s.yaml*) so that this lib can have greater confidence that rules is implemented in the same way as *Kwalify*.
- Refactored *test_core_files* method to now accept test files with multiple of documents. The method now tries to read all documents from each test file and run each document seperatly.
  It now alos reports more detailed about what file and document that fails the test to make it easier to track down problems.
- Major refactoring of test files to now be grouped based on what they are testing instead of a increased counter that do not represent anything.
  It will be easier to find out what keywords lack tests and what keywords that have enough tests.


1.5.2 (Nov 12, 2016)
--------------------

- Convert all documentation to readthedocs
- True/False is no longer considered valid integer
- python3 'bytes' objects is now a valid strings and text type
- The regular PyYaml support is now deprecated in favor of ruamel.yaml, see the following link for more details about
  PyYaml being deprecated https://bitbucket.org/xi/pyyaml/issues/59/has-this-project-been-abandoned
  PyYaml will still be possible to use in the next major release version (1.6.0) but removed in release (1.7.0) and forward.
- ruamel.yaml is now possible to install with the following command for local development *pip install -e '.[ruamel]'*
  and for production, use *pip install 'pykwalify[ruamel]'*
- ruamel.yaml is now used before PyYaml if installed on your system
- Fixed a bug where scalar type was not validated correctly.
- Unpin all dependencies but still maintain a minimum versions of each lib
- Allowed mixing of regex and normal keywords when matching a string (jmacarthur)


1.5.1 (Mar 6, 2016)
----------------

- Improvements to documentation (scottclowe).
- Improved code linting by reworking private variables in Rule class to now be properties and updated
  all code that used the old way.
- Improved code linting by reworking all Log messages to render according to pep standard.
  (By using %s and passing in variables as positional arguments)
- Fix bug when validating sequence and value should only be unicode escaped when a string
- Improve validation of timestamps.
- Improve float validation to now accept strings that is valid ints that uses scientific notation, "1e-06" for example.
- Update travis to test against python 3.6


1.5.0 (Sep 30, 2015)
--------------------

- float / number type now support range restrictions
- ranges on non number types (e.g. seq, string) now need to be non negative.
- Fixed encoding bug triggered when both regex matching-rule 'any' and 'all' found keyword that
  failed regex match.  Added failure unit tests to cover regex matching-rule 'any' and 'all' during
  failed regex match.  Updated allowed rule list to include matching-rule 'all'.
- Changed _validate_mappings method from using re.match to re.search.  This fixes bug related to
  multiple keyword regex using matching-rule 'any'.  Added success unit tests to test default, 'any',
  and 'all' matching-rule.


1.4.1 (Aug 27, 2015)
--------------------

- Added tests to sdist to enable downstream packaging to run tests. No code changes in this release.


1.4.0 (Aug 4, 2015)
-------------------

- Dropped support for python 3.2 becuase of unicode literals do not exists in python 3.2.
- Fixed logging & raised exceptions when using unicode characters inside schemas/data/filenames.
- Reworked all RuleError exceptions to now have better exception messages.
- RuleError exceptions now have a unique 'error_key' that can make it easier to identify what error it is.
- Paths for RuleErrors have been moved inside the exception as a variable.
- Rewrote all SchemaConflict exceptions to be more human readable.


1.3.0 (Jul 14, 2015)
--------------------

- Rewrote most of the error messages to be more human readable. See `docs/Upgrade Instructions.md`
  for more details.
- It is now possible to use the exceptions that was raised for each validation error. It can be
  found in the variable `c.validation_errors_exceptions`. They contain more detailed information
  about the error.


1.2.0 (May 19, 2015)
--------------------

- This feature is NEW and EXPERIMENTAL.
  Implemented support for multiple values inside in a sequence.
  This will allow the defenition of different types that one sequence can contain. You can either require
  each value in the sequence to be valid against one to all of the different possibilities.
  Tests show that it still maintains backward compatibility with all old schemas but it can't be guarantee.
  If you find a regression in this release please file a bug report so it can be fixed ASAP.
- This feature is NEW and EXPERIMENTAL.
  Added ability to define python files that can be used to have custom python code/functions that can be
  called on all types so that custom/extra validation can be done on all data structures.
- Add new keyword 'func' that is a string and is used to point to a function loaded via the extension system.
- Add new keyword 'extensions' that can only be used on the top level of the schema. It is should be a list
  with strings of files that should be loaded by the extension system. Paths can be relative or absolute.
- New cli option '-e FILE' or '--extension FILE' that can be used to load extension files from cli.
- Fixed a bug where types did not raise exceptions properly. If schema said it should be a map but data was
  a sequence, no validation error was raised in earlier versions but now it raises a 'NotSequenceError' or 
  'NotMappingError'.


1.1.0 (Apr 4, 2015)
-------------------

- Rework cli string that docopt uses. Removed redundant flags that docopt provides [--version & --help]
- Add support for timestamp validation
- Add new runtime dependency 'python-dateutil' that is used to validate timestamps
- Change how 'any' keyword is implemented to now accept anything and not just the implemented types. (See Upgrade Instructions document for migration details)



1.0.1 (Mar 8, 2015)
-------------------

Switched back to semantic version numbering for this lib.

- After the release of `15.01` the version schema was changed back from the <year>.<month> style version schema back to semantic version names. One big problem with this change is that `pypi` can't handle the change back to semantic names very well and because of this I had to remove the old releases from pypi and replace it with a single version `1.0.1`.
- No matter what version you were using you should consider upgrading to `1.0.1`. The difference between the two versions is very small and contains mostly bugfixes and added improvements.
- The old releases can still be obtained from `github.com` and if you really need the old version you can add the download url to your `requirements.txt` file.


15.01 (Jan 17, 2015)
--------------------

- Fixed a bug in unique validation for mapping keys [See: PR-12] (Gonditeniz)



14.12 (Dec 24, 2014)
--------------------

- Fixed broken regex matching on map keys.
- Source files with file ending `.yml` can now be loaded
- Added aliases to some directives to make it easier/faster to write
   * `sequence` --> `seq` 
   * `mapping` --> `map` 
   * `required` --> `req`
   * `regex` --> `re`
- Reworked all testing files to reduce number of files



14.08 (Aug 24, 2014)
--------------------

- First version to be uploaded to pypi
- Keyword 'range' can now be applied to map & seq types.
- Added many more test files.
- Keyword 'length' was removed because 'range' can handle all cases now.
- Keyword 'range' now correctly checks the internal keys to be integers
- Major update to testing and increased coverage.



14.06.1 (Jun 24, 2014)
----------------------

- New feature "partial schema". Define a small schema with a ID that can be reused at other places in the schema. See readme for details.
- New directive "include" that is used to include a partial schema at the specefied location.
- Cli and Core() now can handle multiple schema files.
- Directive "pattern" can no longer be used with map to validate all keys against that regex. Use "regex;" inside "mapping:"
- 'none' can now be used as a type
- Many more tests added



14.06 (Jun 7, 2014)
-------------------

- New version scheme [YY.MM(.Minor-Release)]
- Added TravisCI support
- Update runtime dependency docopt to 0.6.1
- Update runtime dependency pyyaml to 3.11
- Huge refactoring of logging and how it works. Logging config files is now removed and everything is alot simpler
- Cleanup some checks that docopt now handles
- New keyword "regex;<regex-pattern>" that can be used as a key in map to give more flexibility when validating map keys
- New keyword "matching-rule" that can be used to control how keys should be matched
- Added python 3.4 & python 2.7 support (See TravisCI tests for status)
- Dropped python 3.1 support
- Alot of refactoring of testing code.
- Tests should now be runned with "nosetests" and not "python runtests.py"
- Refactored alot of exceptions to be more specific (SchemaError and RuleError for example) and not a generic Exception
- Parsed rules is now stored correctly in Core() so it can be tested from the outside



0.1.2 (Jan 26, 2013)
--------------------

- Added new and experimental validation rule allowempty. (See README for more info)
- Added TODO tracking file.
- Reworked the CLI to now use docopt and removede argparse.
- Implemented more typechecks, float, number, text, any
- Now suports python 3.3.x
- No longer support any python 2.x.y version
- Enabled pattern for map rule. It enables the validation of all keys in that map. (See README for more info)
- Alot more test files and now tests source_data and schema_data input arguments to core.py
- Alot of cleanup in the test suit



0.1.1 (Jan 21, 2013)
--------------------

- Reworked the structure of the project to be more clean and easy to find stuff.
- lib/ folder is now removed and all contents is placed in the root of the project
- All scripts is now moved to its own folder scripts/ (To use the script during dev the path to the root of the project must be in your python path somehow, recomended is to create a virtualenv and export the correct path when it activates)
- New make target 'cleanegg'
- Fixed path bugs in Makefile
- Fixed path bugs in Manifest



0.1.0 (Jan 20, 2013)
--------------------

- Initial stable release of pyKwalify.
- All functions is not currently implemented but the cli/lib can be used but probably with some bugs.
- This should be considered a Alpha release used for bug and stable testing and to be based on further new feature requests for the next version.
- Implemented most validation rules from the original Java version of kwalify. Some is currently not implemented and can be found via [NYI] tag in output, doc & code.
- Installable via pip (Not the official online pip repo but from the releases folder found in this repo)
- Supports YAML & JSON files from cli and any dict/list data structure if used in lib mode.
- Uses pythons internal logging functionality and default logging output can be changed by changing logging.ini (python 3.1.x) or logging.yaml (python 3.2.x) to change the default logging output, or use -v cli input argument to change the logging level. If in lib mode it uses your implemented python std logging.

%package bin
Summary: bin components for the pykwalify package.
Group: Binaries
Requires: pykwalify-license = %{version}-%{release}

%description bin
bin components for the pykwalify package.


%package license
Summary: license components for the pykwalify package.
Group: Default

%description license
license components for the pykwalify package.


%package python
Summary: python components for the pykwalify package.
Group: Default
Requires: pykwalify-python3 = %{version}-%{release}

%description python
python components for the pykwalify package.


%package python3
Summary: python3 components for the pykwalify package.
Group: Default
Requires: python3-core
Provides: pypi(pykwalify)

%description python3
python3 components for the pykwalify package.


%prep
%setup -q -n pykwalify-1.7.0
cd %{_builddir}/pykwalify-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583207452
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pykwalify
cp %{_builddir}/pykwalify-1.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pykwalify/bc41778f33239f21bb97dc2edf69d4b3fa26c06c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pykwalify

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pykwalify/bc41778f33239f21bb97dc2edf69d4b3fa26c06c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
