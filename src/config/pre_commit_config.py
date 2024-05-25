pre_commit_config = """\
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
    - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.4.5
    hooks:
        # Run the linter.
        - id: ruff
        args: [ --fix ]
        # Run the formatter.
        - id: ruff-format
"""