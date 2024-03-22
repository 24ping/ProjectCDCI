# CI/CD concept
In this project, the main idea is to develop a modern CI/CD concept. The idea will starts by a developer who tries to go through the CI/CD steps.
## Assumption
- The developer and the boss are the same the person.
- The boss has two branches : {main, Dev}.
- The developer has access to both branches.
## Steps
- [x] Before `source` stage
- [ ] `Source` stage
- [ ] `Build` stage
- [ ] `Test` stage
- [ ] `Release` stage


# Before-Source stage :computer:
## Main idea
This is the first phase where the developer in the `Dev` branches tries to push his code to the boss repo. However he must follow some steps.

Please refer to [Before-Source-Branch-Documentation](/docs/Branches/Before-Source.md) for more information.
## Steps
- [x] Create `Readme` file or any file.
- [x] Install `Pre-commits` check within the IDE.
- [x] Push your code to `Dev` branch.
- [x] Create Branch protection rule
- [x] Merge your code with the `main` branch.

# Source-Stage:

## Main idea
This is the step where the actual code resides for development following best practices. Moreover, during this phase these were the <a href="## Actions ">actions </a>  implemented and linked to the new branch `source`.

Please refer to [Source-Branch-Documentation](/docs/Branches/Source-Stage.md) for more information.

## Actions
- [ ] Create new branch for code development.
- [ ] Initialize a file structure for the code.
- [ ] Include the project code following OOP best practices.
- [ ] Implement GitHub Actions
- [ ] Implement new linting mechanisms
- [ ] Implement new branch protection rules
- [ ] Document the actions token for this branch in a `Source-Stage.md`
- [ ] Merge the `source` branch with the `main` branch
