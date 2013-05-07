jsrevival support for Sublime Text 2 by using node
========================

sublime-jsrevival is based on a fork of https://github.com/fbzhong/sublime-jslint

Sublime Text 2 (http://www.sublimetext.com/2) is a text editor.

jsrevival (https://github.com/sdolard/node-jsrevival) is a another nodejs wrapper around the jslint tool by Douglas Crockford, [jslint](http://jslint.com). It provides an interface for detecting potential problems in JavaScript code.

This project provide a plugin to add jsrevival support for Sublime Text 2.

Features
-------------

- jsrevival: run jsrevival (ctrl+j), or run jsrevival on save

- jsrevival: show jsrevival Result

- Highlight error line by click on the result view

- Cross platform: support Windows, Linux and Mac OS X

Requirements
-------------

- node, and make sure node has been added to PATH
- jsrevival npm package, and make sure jsrevival has been added to PATH

Installation
-------------

- Using Package Control http://wbond.net/sublime_packages/package_control

    > Install Package: sublime-jsrevival

- Download and extract to Sublime Text 2 Packages folder

    > Windows:  %APPDATA%\Sublime Text 2\Packages

    > Mac OS X: ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/

    > Linux:    ~/.config/sublime-text-2/Packages

How to use?
-------------

- Using the Command Palette (Windows and Linux: Ctrl+Shift+P, OSX: Command+Shift+P) then search for:

    - jsrevival: run jsrevival (ctrl+j)
    - jsrevival: show jsrevival Result

Open up a .js file and hit ctrl+j to run jsrevival. An new output panel will appear giving you the jsrevival results.

Screenshots
-------------

![](https://raw.github.com/sdolard/sublime-jsrevival/master/images/screenshot.png)

Settings
-------------

Settings can be opened via the Command Palette, or the Preferences > Package Settings > jsrevival > Settings – User menu entry.

    {
        // A list of comma separated strings, the names of predefined global variables,
        // or an object whose keys are global variable names,
        // and whose values are booleans that determine if each variable is assignable (also see global).
        // predef is used with the option object, but not with the /*jslint*/ directive.
        // You can also use the var statement to declare global variables in a script file.
        "predef": "",

        // A list of comma separated strings with this format: "token: value"
        // JSLint default options:
        //  ass: true # if assignment expressions should be allowed
        //  bitwise: true # if bitwise operators should be allowed
        //  browser: true # if the standard browser globals should be predefined
        //  closure: true # if Google Closure idioms should be tolerated
        //  continue: true # if the continuation statement should be tolerated
        //  couch: true # no help
        //  debug: true # if debugger statements should be allowed
        //  devel: true # if logging should be allowed (console, alert, etc.)
        //  eqeq: true # if == should be allowed
        //  es5: true # if ES5 syntax should be allowed
        //  evil: true # if eval should be allowed
        //  forin: true # if for in statements need not filter
        //  indent: 10 # the indentation factor
        //  maxerr: 1000 # the maximum number of errors to allow
        //  maxlen: 256 # the maximum length of a source line
        //  newcap: true # if constructor names capitalization is ignored
        //  node: true # if Node.js globals should be predefined
        //  nomen: true # if names may have dangling _
        //  passfail: true # if the scan should stop on first error
        //  plusplus: true # if increment/decrement should be allowed
        //  properties: true # if all property names must be declared with /*properties*/
        //  regexp: true # if the . should be allowed in regexp literals
        //  rhino: true # if the Rhino environment globals should be predefined
        //  unparam: true # if unused parameters should be tolerated
        //  sloppy: true # if the 'use strict'; pragma is optional
        //  stupid: true # if really stupid practices are tolerated
        //  sub: true # if all forms of subscript notation are tolerated
        //  todo: true # if TODO comments are tolerated
        //  vars: true # if multiple var statements per function should be allowed
        //  white: true # if sloppy whitespace is tolerated
        //  windows: true # if MS Windows-specific globals should be predefined
        "options": "es5: false, properties: false, maxlen: 0, debug: false, newcap: false, unparam: false, sub: false, vars: false, passfail: false"
    }

New BSD License
-------------

Copyright (c) 2013, Sébastien Dolard <sdolard@gmail.com>
Copyright (c) 2011, Robin Zhong <fbzhong@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Robin Zhong nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
