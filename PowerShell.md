# PowerShell in a Nutshell

## Commandlets [(1)][1]

Commandlets or Cmdlt are basically commands you can use in your PowerShell scripts. All of them are orgasmed in a certain standardized fashion `<verb>-<noun>` and have detailed help files you can read using this cmdlt `get-help <commandlet-name>`, for example:

```PowerShell
get-help *  # shows help about specified topic or cmdlt

update-help  # updates local help files from the Internet

test-connection 192.168.1.1  # test connection to specified computer using ICMP echo request packets
```

More formal definition:
> A cmdlet is a lightweight command that is used in the Windows PowerShell environment. The Windows PowerShell runtime invokes these cmdlets within the context of automation scripts that are provided at the command line. The Windows PowerShell runtime also invokes them programmatically through Windows PowerShell APIs.

Cmdlets perform an action and typically return a `Microsoft .NET Framework` object to the next command in the pipeline. 

## Everything is an Object [(3)][3]

PowerShell uses Objects as its output rather than text like `bash` in Linux or legacy command prompt. This is a **big deal** because you are no longer have to parse the output of the command and use regular expressions.

Every object has properties and methods. You can see an object's properties and methods by passing it to the `Get-Member` cmdlet.

The objects that a PowerShell cmdlet outputs are largely underlying types from the .Net framework, but you can create your own objects if you need to use a language like C# or use the PSObject type.

### The Pipeline

There are plenty of Linux shells with a pipeline, allowing you to send the text that one command outputs as input to the next command in the pipeline. PowerShell takes this to the next level by allowing you to take the objects that one cmdlet outputs and pass them as input to the next cmdlet in the pipeline. 

The trick is knowing what type of object a cmdlet returns, which is really easy when using the `Get-Member` cmdlet.

```PowerShell
Get-Service | Get-Member
```

`Get-Member` cmdlet also returns another important piece of information, the underlying object type, for example: `System.ServiceProcess.ServiceController`

Since PowerShell deals with objects and not text,  not all cmdlets can be linked together using the pipeline. That means we need to find a cmdlet that’s looking to accept a `System.ServiceProcess.ServiceController` object from the pipeline with the following command:

```PowerShell
Get-Command -ParameterType System.ServiceProcess.ServiceController
```
Use `Get-Help -Name <Cdlt-name> –Full` to get more information about the cmdlt and how you can use it.

## Formatting, Filtering and Comparing objects [(4)][4]

### Default formatting

PowerSheel may not show every property of an object by default because it may be overwhelming to see all the details. Instead, it uses the following file `C:\Windows\System32\WindowsPowerShell\v1.0\DotNetTypes.format.ps1xml` as formatting information.

But what if the object type you are dealing with doesn't have an entry in that file, or any other format file for that matter? Well then, it's quite simple actually. If the object coming out of the pipeline has 5 or more properties, PowerShell displays all of the object's properties in a list; if it has less than 5 properties, it displays them in a table.

### Formatting Your Data
If you are not happy with the default formatting of an object or type, you can roll your own formatting. There are three cmdlets you need to know to do this:

- **Format-List** `Get-Process | Format-List –Property *` - shows properties of an object as a list
- **Format-Table ** `Get-Process | Format-Table name,id –AutoSize` - takes data and turns it into a table
- **Format-Wide** `Get-Service | Format-Wide -Property DisplayName -Column 1` - simply takes a collection of objects and displays a single property of each object

### Filtering and Comparing

One of the best things about using an object-based pipeline is that you can filter objects out of the pipeline at any stage using the Where-Object cmdlet.

```PowerShell
Get-Service | Where-Object {$_.Status -eq “Running”}
```
Using where object is actually very simple. `$_` represents the current pipeline object, from which you can choose a property that you want to filter on. Here, were are only keeping objects where the Status property equals Running. `-eq` is a comparison operator in PowerShell

## Syntax

### Variables [(5)][5]

Here is how to create a variable called “FirstName” and give it the value “John”.
```PowerShell
$FirstName = "John"
```

Variables in PowerShell are weakly typed by default meaning they can contain any kind of data

In PowerShell, you can see all the variables you have created in the variable PSDrive.
```PowerShell
gci variable:
```

Which means you can delete a variable from the shell at anytime too:
```PowerShell
Remove-Item Variable:\FirstName
```

Variables don’t have to contain a single object either; you can just as easily store multiple objects in a variable. For example, if you wanted to store a list of running processes in a variable, you can just assign it the output of `Get-Process`:
```PowerShell
$Proc = Get-Process
```

The trick to understanding this is to remember that the right hand side of the equals sign is always evaluated first. This means that you can have an entire pipeline on the right hand side if you want to.
```PowerShell
$CPUHogs = Get-Process | Sort CPU -Descending | select -First 3
```
The CPUHogs variable will now contain the three running processes using the most CPU.

When you do have a variable holding a collection of objects, there are some things to be aware of. For example, calling a method on the variable will cause it to be called on each object in the collection.
```PowerShell
$CPUHogs.Kill()
```
Which would kill all three process in the collection. If you want to access a single object in the variable, you need to treat it like an array.
```PowerShell
$CPUHogs[0]
```

### Comparison operators

There are a few comparison operators you can use in the filtering script block:

- `eq` (Equal To)
- `neq` (Not Equal To)
- `gt` (Greater Than)
- `ge` (Greater Than or Equal To)
- `lt` (Less Than)
- `le` (Less Than or Equal To)
- `like` (Wildcard String Match)

A full list and more information can be viewed in the about_comparison conceptual help file:

```PowerShell
 get-help about_Comparison_Operators -showWindow
```

### Input and Output

You can prompt users for information using it is really simple:
```PowerShell
$FirstName = Read-Host –Prompt ‘Enter your first name’
```

Writing output is just as easy with the Write-Output cmdlet.
```PowerShell
Write-Output “How-To Geek Rocks!”
```

## Writing Scripts [(2)][2]

The most of your work in Windows PowerShell will be done by writing and running scripts rather than using interactive console entering one commandlet at a time. I recommend using PowerShell Integrated Scripting Environment (ISE) which is shipped with PowerSheel, it makes the process of writing and testing scripts much easier.

Windows PowerShell scripts have `.ps1` extension

### Help information

It's always a good idea to put help information in your scripts. It can be accessed by `get-help YourScript.ps1`. Here is how you can add it

```PowerShell
<#
.SYNOPSIS
  Measures an average response time to a remote hosts and forms the resulting table
.DESCRIPTION
  The script uses Test-Connection Cmdlt which sends Internet Control Message Protocol (ICMP) echo request packets ("pings"), calculates the average response time in turn and forms the resulting table showing the host with the lowest value at the top.
.PARAMETER hosts
  The list of hosts you want to test
.PARAMETER count
  The number of pings send to a remote host, 100 by default
.EXAMPLE
  Get-AvgPingResponseTime -hosts 8.8.8.8, 8.8.4.4 -count 10
.LINK
  https://github.com/m-a-ge/utilities
#>
```

### Parameters 

```PowerShell
param(
  [string]$count = 100,
  [Parameter(Mandatory=$true)][string]$hosts
)
```

### Conditions

```PowerShell
If ($this -eq $that) {
  # commands
} elseif ($those -ne $them) {
  # commands
} elseif ($we -gt $they) {
  # commands
} else {
  # commands
}
```

### Loops

```PowerShell
Do {
  # commands
} While ($this -eq $that)

While (Test-Path $path) {
  # commands
}

$services = Get-Service
ForEach ($service in $services) {
  $service.Stop()
}
```

### Functions

```PowerShell
function Mine {
  Get-Service
  Get-Process
}
Mine

function Get-LetterCount {

 Param ([string]$string)

 Write-Host -ForegroundColor Cyan “string length is” $string.Length

 $string | clip.exe

} # End Function Get-LetterCount
```

### Other constructs

```PowerShell
1..10 | ForEach-Object -process {
  # code here will repeat 10 times
  # use $_ to access the current iteration
  # number
}
```

## PowerShell Execution Permissions

Due to security risks Windows PowerShell may not run scripts by default. 

> If the execution policy in all scopes is Undefined, the effective execution policy is Restricted, which is the default execution policy.

For more details read the help file:
```PowerShell
get-help about_Execution_Policies -showWindow
```

You can change the settings using the following cmdlts:
```PowerShell
# get the current execution policy
Get-ExecutionPolicy  

# setting a new execution policy which allows you to run scripts only from a trusted publisher
Set-ExecutionPolicy -ExecutionPolicy AllSigned
```

## References
1. [Cmdlet Overview][1]
2. [Geek School: Writing Your First Full PowerShell Script][2]
3. [Geek School: Learning How to Use Objects in PowerShell][3]
4. [Geek School: Learning Formatting, Filtering and Comparing in PowerShell][4]
5. [Geek School: Learning PowerShell Variables, Input and Output][5]


[1]: https://msdn.microsoft.com/en-us/library/ms714395(v=vs.85).aspx
[2]: http://www.howtogeek.com/141495/geek-school-writing-your-first-full-powershell-script/
[3]: http://www.howtogeek.com/138121/geek-school-learning-powershell-objects/
[4]: http://www.howtogeek.com/138324/geek-school-learning-formatting-filtering-and-comparing-in-powershell/
[5]: http://www.howtogeek.com/141099/geek-school-learning-powershell-variables-input-and-output/