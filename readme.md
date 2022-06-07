# Introduction

This repository aims to allow collaboration work on lightweight code-based graphical tool PlantUML.

For documentations: https://plantuml.com/

# Requirements

This is maintained via VSCode Extension: 
- jebbs.plantuml

Need to install this extension to properly work.

## Set Default VSCode Plantuml Config

1. click the GEAR icon
2. click Settings (or hotkey: `CMD` + `,`)
3. search for
   1. plantuml.diagramsRoot
      1. set as src
   2. plantuml.exportOutDir
      1. set as out

### The intended config:
```
"plantuml.diagramsRoot": "src",
"plantuml.exportOutDir": "out"
```

# Folder Structure

`src` : Contains plantuml source code. You may nest folders as you see fit.
`out` : Contains generated diagram in desired format.


# Building The Diagrams

Use VSCode built in command pallete

To build ALL diagrams in src:
- `CMD+Shift+P`
    - `PlantUML: Export Workspace Diagrams`

To build only current diagram:
- `CMD+Shift+P`
    - `PlantUML: Export Current Diagram`

## Example

when exporting via CMD+Shift+P below will occur

```
src/
  architecture_overview
  ...rest_of_your_project_folders/
  ...rest_of_your_project_files/ 
out/
  architecture_overview/
    architecture_overview.png
  ...rest_of_your_project_folders/
  ...rest_of_your_project_files/ 
```

# Using your build image

## To use from web url

1. Go to github: https://github.com/thetomitomo/diagrams/tree/master/out
2. Find your image
3. Find the source URL of your image
   1. On github UI
   2. Right click
   3. Copy image address
4. Use this URL as your web url source

The next time you rebuild your image, as long as there are is name changes, it will overwrite the old image, updating the live audience with the new image.
