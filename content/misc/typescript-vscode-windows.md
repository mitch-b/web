Title: Using TypeScript in Visual Studio Code on Windows
Date: 2015-08-03 21:05
Modified: 2015-08-03 21:05
Tags: typescript,vscode,blog
Slug: typescript-vscode-windows
Summary: Trying out TypeScript on the Mac was a fantastic experience. Transferring that over to Windows brought up a weird roadblock that has a simple fix.
About_author: Software Developer, Person

>This experience is from TypeScript 1.5 beta, and very well may change in the future 

If you are trying to get [TypeScript](http://www.typescriptlang.org/) to build to JavaScript "out-of-the-box" in [Visual Studio Code](https://code.visualstudio.com/), it seems to work just fine (relatively) on Mac/Linux. However, to get the `tsc` command to properly transpile your `*.ts` files, you have to use the *right* command.

Here's an example of the `.settings/tasks.json` file I was working with.

    :::json
    {
		"version": "0.1.0",
		
		// The command is tsc. Assumes that tsc has been installed using npm install -g typescript
		"command": "tsc",
		
		// The command is a shell script
		"isShellCommand": true,
	
		// Show the output window only if unrecognized errors occur. 
		"showOutput": "silent",
		
		// args is the HelloWorld program to compile.
		"args": [],
		
		// use the standard tsc problem matcher to find compile problems
		// in the output.
		"problemMatcher": "$tsc"
	}
	
This worked *great* on my Mac, but seemed to only show me the `tsc` help page in my output window in Visual Studio Code on Windows. With a lot of digging and chasing tails, I found a post by [Michael Crump](http://michaelcrump.net/using-typescript-with-code/).

	:::json
	"windows": {
		"command": "tsc.cmd"
	}
	
This snippet needed to be added into my task runner to properly run on Windows. Hope this helps someone else out (until it changes in a future release...). 

:)

* [TypeScript/Angular2 Playground](https://github.com/mitch-b/angular2-playground)