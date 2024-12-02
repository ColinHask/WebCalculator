# WebCalculator
Web calculator for SWE 3643

> Instruction Repo link: https://github.com/jeff-adkisson/swe-3643-fall-2024/blob/main/project/README.md




# Readme Instructions:

preq-DOCUMENTATION-2

Your project's README.md file will contain the following sections:

- Introduction
- Table of Contents
- Team Members
- Architecture
- Environment
- Executing the Web Application
- Executing Unit Tests
- Reviewing Unit Test Coverage
- Executing End-To-End Tests
- Final Video Presentation
- Order your README.md file according to the section order shown above.

preq-DOCUMENTATION-3: Introduction

Your Introduction section will be titled "KSU SWE 3643 Software Testing and Quality Assurance Semester Project: Web-Based Calculator" rather than "Introduction". Set this section to an H1 (# KSU SWE...).

Following the title, write a short (2-3 sentence) description of what the repository contains.

preq-DOCUMENTATION-4: Table of Contents

Create an H2 section named Table of Contents (## Table of... ). List the sections starting with Environment as bullets.

List all of the sections in your document execept the introduction and Table of Contents. Create a hyperlink to each section. Your hyperlink will look like the following example:

## Table of Contents

- [Environment](#environment)
- [Executing the Web Application](#executing-the-web-application)
All of your links will be relative. If you find yourself writing links that include GitHub's address, you are likely not writing relative links. Clone this repository if you need an example: the relationship of README.md to requirements.md demonstrates relative linking.

To create an anchor link (a link that jumps somewhere within the current document), prefix the section's title with a # symbol, then write the title lowercase and place a dash in place of all spaces. Always test your anchor links after checking your work into GitHub to verify that they work correctly (particularly if you use Typora, which is more forgiving than GitHub)

preq-DOCUMENTATION-5: Team Members

List your team members. You do not need to include any contact information (your repository is public).

preq-DOCUMENTATION-6: Architecture

Briefly describe the architecture of your project. Reference the architecture diagram from this document. Make the diagram an image - not a link.

You are encouraged to update the architecture diagram to better match your project structure. The original diagram is generic and may not properly describe your specific implementation. The original diagram uses PlantUML. You can use any diagramming tool you like (so long as the results look professional), but give PlantUML a try.

@startuml
allowmixing

package "Calculator Logic Module" #lightblue
{
    class DescriptiveStatistics {
        + ValidationFunctions
        + LogicFunctions
    }

    class LinearRegression {
        + ValidationFunctions
        + LogicFunctions
    }

}

package "Calculator Logic Unit Tests via JUnit, NUnit, or Pytest" #lightyellow
{
  class LogicUnitTests {
    + DescriptiveStatistics_AcceptsValueMeanStdDev_ReturnsZScore()
    + LinearRegression_EmptyList_ReturnsError()
  }

  LogicUnitTests --> DescriptiveStatistics
  LogicUnitTests --> LinearRegression

}

package "Calculator Web Server App" #lightblue
{
   class Models
   class Views
   class Controllers

   Controllers --> Views
   Controllers --> Models
   Controllers --> DescriptiveStatistics
   Controllers --> LinearRegression
}

package "Calculator End-To-End Tests via Playwright" #lightyellow {
  class CalculatorEndToEndTests {
     + CalculatorUI_ListofValues_CalculatesMean()
     + CalcuatlorUI_EmptyListOfValues_DisplaysError()
     + CalculatorUI_InvalidListOfValues_DisplaysError()
  }

    CalculatorEndToEndTests --> Controllers : HTTP Call via\n Headless Browser
}

cloud #yellow {
  hide circle
  class Browser
  Browser <--> Controllers : HTTP Call
}
@enduml
preq-DOCUMENTATION-7: Environment

Explain how to configure the environment to execute your web application, unit tests, and end-to-end tests. For example:

This is a cross-platform application and should work in Windows 10+, Mac OSx Ventura+, and Linux environments. Note that the application has only been carefully tested in Windows 11.

To prepare your environment to execute this application:
 1. [Install the latest Java runtime for your system.](https://www.java.com/en/download/manual.jsp)
 2. ...

To configure Playwright for end-to-end testing:
  1. ...
If you are writing something that should be cross-platform, but you have only tested on a single platform (such as Windows or Linux), note where you have tested it specifically.

If your environment setup includes terminal commands, use single primes for inline commands (such as git ) or triple primes for blocks:

This is a code block.
It can contain multiple lines.
preq-DOCUMENTATION-8: Executing the Web Application

Create an H2 section called Executing the Web Application.

Describe the detailed steps to build and execute your web application from the command line (terminal / console). Your user may not have an IDE installed.

Your last step will describe how to connect to the running web application from a browser on the same machine. This often requires a port. For example, 6. After the application starts, launch a browser and connect to http://localhost:60012.

Include sample output from building and executing the web application. For example:

$ dotnet run
info: Extensions.Hosting.AsyncInitialization.RootInitializer[0]
      Starting async initialization
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: https://localhost:60012
If you find certain errors popping up when you run the application (such as port in use), note these common problems and how to fix them. You want your user to have little or no trouble getting your application running. For example:

If you see the following error, something is already running on the application's HTTP port. Free up the port, then try again:
Unhandled IO exception: Failed to bind to https://127.0.0.1:60012: address already in use.
preq-DOCUMENTATION-9: Executing Unit Tests

Create an H2 section called Executing Unit Tests.

Describe the detailed steps to build and execute all of your unit tests from the command line (terminal / console). Your user may not have an IDE installed.

Finally, include sample output in a code block. For example:

$ dotnet test

Starting test execution, please wait...
A total of 1 test files matched the specified pattern.
Starting test execution, please wait...
A total of 1 test files matched the specified pattern.

Passed!  - Failed:     0, Passed:   132, Skipped:     0, Total:   132, Duration: 39 ms - HighMatch.Compass.UnitTest.Extensions.dll (net7.0)
preq-DOCUMENTATION-11: Reviewing Unit Test Coverage

Create an H2 section called Reviewing Unit Test Coverage.

Note the coverage achieved in your Calculator Logic module and include a screenshot of your coverage graphic from your JetBrains IDE. Your calculator logic must achieve 100% test coverage of all statements and paths.

Coverage statistics look similar to the following example:

image-20240204220021325

preq-DOCUMENTATION-12: Executing End-To-End Tests

Create an H2 section called Executing End-To-End Tests.

Describe the detailed steps to build and execute all of your end-to-end unit tests from the command line (terminal / console). Your user may not have an IDE installed.

Finally, include sample output in a code block. For example:

# From /Users/jeff/projects/swe-3643-spring-2024-project/src/Calculator/CalculatorEndToEndTests

❯ dotnet test
  Determining projects to restore...
  All projects are up-to-date for restore.
  CalculatorEndToEndTests -> /Users/jeff/projects/swe-3643-spring-2024-project/src/Calculator/CalculatorEndToEndTests/bin/Debug/net8.0/CalculatorEndToEndTests.dll
Test run for /Users/jeff/projects/swe-3643-spring-2024-project/src/Calculator/CalculatorEndToEndTests/bin/Debug/net8.0/CalculatorEndToEndTests.dll (.NETCoreApp,Version=v8.0)
Microsoft (R) Test Execution Command Line Tool Version 17.8.0 (arm64)
Copyright (c) Microsoft Corporation.  All rights reserved.

Starting test execution, please wait...
A total of 1 test files matched the specified pattern.

Passed!  - Failed:     0, Passed:     1, Skipped:     0, Total:     1, Duration: 2 s - CalculatorEndToEndTests.dll (net8.0)
preq-DOCUMENTATION-13: Final Video Presentation

Create an H2 section called Final Video Presentation.

Include a link to your final video presentation. If the file is checked into your Team Repository, this will be a relative link. Otherwise, it will be a fully-qualified link to YouTube or Vimeo. For example:

Please view our project's presentation here on YouTube.
