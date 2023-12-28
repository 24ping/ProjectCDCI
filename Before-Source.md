# Main Idea
This file servers as a documentation for the `Dev` branch. This documentation includes:
- Why `Dev` branch was created.
- The mandatory files.
- The initialization of `pre-commit` checks.

# The Branch Dev
The `Dev` branch was created as an initial stage that allows the developer to relocate his code from the a machine to the remote infrastructure `Github`. Moreover it's the first step in a CI/CD pipeline.

# Implementation Files
To start a project, such as a pipeline, the needed files for this phase `Before-source` is :
  - `Readme.md` documents the whole aspect of this project.
  - `Before-Source.md` documents the aspects of the creation of this branch.
  - `CodeExample.py` serves as an example code. A code that can be used to test new notions.
  - `.pre-commit-config.yaml` is a checking mechanism that will be used throughout the initialization of this project. This mechanism makes sure that there are no white space or new lines.
  > - The hooks used are:
  >> -  `end-of-file-fixer`
  >> - `trailing-whitespace`
  > - The full documentation:
  >> - https://pre-commit.com/#pre-commit-configyaml---hooks
