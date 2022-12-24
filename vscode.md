# VSCode Setting for Black and Flake8 Linting and Formatting

Add the following code to .vscode/settings.json

{
"editor.formatOnSave": true,
"python.formatting.provider": "black",
"python.formatting.blackArgs": ["--line-length", "88"],
"python.linting.enabled": true,
"python.linting.lintOnSave": true,
"python.linting.flake8Enabled": true,
"python.linting.flake8Args": ["--max-line-length", "88"],
"[python]": {
"editor.codeActionsOnSave": {
"source.organizeImports": true
}
}
}
