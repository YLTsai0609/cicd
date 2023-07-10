# Ref

[circleci](https://circleci.com/docs/concepts/#workflows)

# configuration as code

CI/CD process is orchestrated through a single file called `config.yml` 

1. steps - run commands (such as installing dependencies or running tests) and shell scropts to do the work required for your project.

2. jobs - running a series of steps that perform commands.

3. workflow - orchestrating multiple jobs

4. pipeline - the entirety of your configuration.

5. contexts - shared envirable of projects

6. data persistence
  * artifacts
  * caches
  * workspaces

