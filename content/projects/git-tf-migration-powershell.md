Title: Git-TF Migration PowerShell
Date: 2014-02-03 21:36
Modified: 2014-03-25 12:31
Tags: tfs,git-tf,powershell
Slug: git-tf-migration-powershell
Summary: PowerShell script to assist migrating TFVC projects across TFS Collections (or servers) using Git

* [Source Code](https://github.com/mitch-b/git-tf-migration-powershell)

PowerShell script to migrate source code across TFS collections. This can serve as an alternative to the [TFS Integration Tool](http://tfsintegration.codeplex.com) which relies on SQL Server database and some complex configuration.

If you are using Team Foundation Server (or Visual Studio Online) for source control, and need to migrate to another TFVC system or Git, you can use this PowerShell script to migrate your project (including changeset or commit history). An entire novel can be found at the source code link for implementation details.
