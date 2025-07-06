# Receipt Scanner Spike

A Python application for scanning receipts, built with modern Python tooling.

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager and project manager

### Installation

1. **Clone the repository** (if not already done):

   ```bash
   git clone <repository-url>
   cd receipt-scanner-spike
   ```

2. **Install dependencies** using uv:

   ```bash
   uv sync
   ```

   This will:
   - Create a virtual environment in `.venv/`
   - Install all project dependencies
   - Install development dependencies (Black, pytest)

3. **Activate the virtual environment** (optional, uv handles this automatically):

   ```bash
   source .venv/bin/activate
   ```

## 🏃‍♂️ Running the Application

### Using the console script

```bash
uv run receipt-scanner
```

### Running the module directly

```bash
uv run python -m receipt_scanner.main
```

## 🧪 Testing

Run the test suite with pytest:

```bash
uv run pytest tests/
```

Run tests with verbose output:

```bash
uv run pytest tests/ -v
```

## 🎨 Code Formatting

This project uses [Black](https://github.com/psf/black) for code formatting.

### Format code

```bash
uv run black src/ tests/
```

### Check formatting without making changes

```bash
uv run black --check src/ tests/
```

## 📦 Dependency Management

### Add a new dependency

```bash
uv add <package-name>
```

### Add a development dependency

```bash
uv add --dev <package-name>
```

### Update dependencies

```bash
uv sync
```

### Remove a dependency

```bash
uv remove <package-name>
```

## 🏗️ Project Structure

```text
receipt-scanner-spike/
├── src/receipt_scanner/      # Main package
│   ├── __init__.py          # Package initialization
│   └── main.py              # Application entry point
├── tests/                   # Test directory
│   ├── __init__.py
│   └── test_main.py         # Basic tests
├── docs/                    # Documentation
├── .vscode/                 # VSCode configuration
│   └── settings.json        # Editor settings
├── .venv/                   # Virtual environment (auto-created)
├── .gitignore              # Git ignore patterns
├── .python-version         # Python version specification
├── pyproject.toml          # Project configuration
├── uv.lock                 # Dependency lock file
└── README.md               # This file
```

## ⚙️ Development Setup

### VSCode Configuration

The project includes VSCode settings in `.vscode/settings.json` that:

- Use the uv virtual environment (`.venv/bin/python`)
- Configure Black as the default Python formatter
- Enable format-on-save
- Optimize Pylance settings for better performance

### Required VSCode Extensions

- **Black Formatter** (`ms-python.black-formatter`) - For Python code formatting
- **Markdownlint** (`DavidAnson.vscode-markdownlint`) - For Markdown linting

## 🔧 Configuration

### Python Configuration (`pyproject.toml`)

The project uses `pyproject.toml` for configuration:

- **Dependencies**: Managed in `[project.dependencies]`
- **Dev Dependencies**: Managed in `[dependency-groups.dev]`
- **Black Settings**: Configured in `[tool.black]`
- **Build Settings**: Configured with Hatchling

### Key Tools

- **Package Manager**: [uv](https://docs.astral.sh/uv/)
- **Code Formatter**: [Black](https://github.com/psf/black)
- **Testing Framework**: [pytest](https://pytest.org/)
- **Build Backend**: [Hatchling](https://hatch.pypa.io/)

## 📝 Common Commands

```bash
# Development workflow
uv sync                          # Install/update dependencies
uv run receipt-scanner           # Run the application
uv run pytest tests/            # Run tests
uv run black src/ tests/        # Format code

# Dependency management
uv add requests                  # Add runtime dependency
uv add --dev mypy               # Add development dependency
uv remove requests              # Remove dependency

# Project information
uv show                         # Show project info
uv tree                         # Show dependency tree
```

## 🤝 Contributing

1. Ensure all tests pass: `uv run pytest tests/`
2. Format code with Black: `uv run black src/ tests/`
3. Follow the existing code style and project structure

## 📄 License

[Add your license information here]