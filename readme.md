# Introduction

This repository aims to allow collaboration work on lightweight code-based graphical tool PlantUML.

For documentations: https://plantuml.com/

# Requirements

This is maintained via VSCode Extension: 
- jebbs.plantuml

Need to install this extension to properly work.

## Default config
```
"plantuml.diagramsRoot": "docs/diagrams/src",
"plantuml.exportOutDir": "docs/diagrams/out"
```

# Folder Structure

`src` : Contains plantuml source code.
`out` : Contains generated diagram in desired format.


# Building The Diagrams

Use VSCode built in command pallete
- `CMD+Shift+P`
    - `PlantUML: Export Workspace Diagrams`

## Example

when exporting via CMD+Shift+P below will occur

```
Project Folder/
  docs/
    diagrams/
      src/
        architecture_overview.wsd
      out/
        architecture_overview/
          architecture_overview.png
  ...rest_of_your_project_folders/
  ...rest_of_your_project_files 
```
