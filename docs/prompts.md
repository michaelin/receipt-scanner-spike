# Documentation of the development process

This file will contain all prompts used in the generation of the project.
The `prompts.md` file is updated in the commit that the prompt has generated.
I will try to add any manual updates as well.

## Prompts

```text
#new python application project in the current folder. Use uv for dependency and venv management. Keep all initial configuration files minimal. Only add what is essential to get started. For all uv related files, use relevant uv commands to generate them. Run everything within a venv. Use Black for Python linting. Use the Markdownlint VSCode plugin by David Anson for Markdown linting. Do not install Markdownlint separately; I do not want to deal with Tests using PyTest. Use the current folder. It is already initialize as a Git repo.
```

```text
#codebase Pylance is not able to find the pytest module. This may be a problem with VSCode configuration. Please ensure that Black is used instead of Pylance for linting and formatting in VSCode.
```

Manually updated `.gitignore` to ensure relevant files in `.vscode` folder are included.

```text
A lot of the settings in are registered as unknown configuration settings by VSCode. Please analyze and fix.
```

```text
Finally add a basic README.md with instruction on who to get started with the project. Remember that we're using uv.
```
