# VSCode Setting for Black and Flake8 Linting and Formatting

Add the following code to .vscode/settings.json

```sh
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
```

Please note that the code above is now out-of-date with vscode. I will update the code to the new standards in the next while.
