# Contributing to DragonCrawl

Welcome! Thank you for your interest in contributing to DragonCrawl, an AI-powered mobile testing framework. This document provides guidelines and information for contributors.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contribution Types](#contribution-types)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing Guidelines](#testing-guidelines)
- [AI/ML Contribution Guidelines](#aiml-contribution-guidelines)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

### Our Pledge
We pledge to make participation in DragonCrawl a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards
Examples of behavior that contributes to creating a positive environment include:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Unacceptable Behavior
Examples of unacceptable behavior include:
- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

### Enforcement
Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Docker (optional but recommended)
- CUDA-capable GPU (optional, for ML model training)

### Fork and Clone
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/dragoncrawl.git
   cd dragoncrawl
   ```

## Development Setup

### Using Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .

# Install pre-commit hooks
pre-commit install
```

### Using Docker (Recommended)
```bash
# Start development environment
docker-compose up -d

# Access the development container
docker-compose exec dragoncrawl bash

# Run tests
docker-compose exec dragoncrawl pytest
```

### Verify Setup
```bash
# Run basic tests
pytest tests/

# Check code formatting
black --check src/ tests/
isort --check-only src/ tests/
flake8 src/ tests/

# Type checking
mypy src/
```

## Contribution Types

### 🐛 Bug Fixes
- Fix existing functionality
- Add regression tests
- Update documentation if needed

### ✨ New Features
- Add new capabilities
- Include comprehensive tests
- Update documentation
- Consider backward compatibility

### 🤖 AI/ML Improvements
- Model architecture enhancements
- Performance optimizations
- New embedding strategies
- Vector database integrations

### 📱 Mobile Testing Enhancements
- Platform support extensions
- Framework integrations
- Device compatibility improvements
- Test generation algorithms

### 📚 Documentation
- API documentation
- Tutorials and examples
- Architecture guides
- Performance optimization guides

## Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
# or
git checkout -b ml/model-improvement
```

### 2. Make Changes
- Write code following our standards
- Add or update tests
- Update documentation
- Run pre-commit hooks

### 3. Test Your Changes
```bash
# Run all tests
pytest tests/ -v

# Run specific test categories
pytest tests/test_language_model.py
pytest tests/test_mobile_interface.py

# Check coverage
pytest --cov=src/dragoncrawl --cov-report=html
```

### 4. Commit Changes
```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add MPNet embedding optimization

- Implement batch processing for embeddings
- Add GPU memory management
- Include performance benchmarks
- Update documentation

Fixes #123"
```

### 5. Push and Create PR
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Standards

### Python Code Style
- Follow PEP 8 style guidelines
- Use Black for code formatting (line length: 88)
- Use isort for import sorting
- Follow type hints throughout

### Code Quality Tools
- **Black**: Automatic code formatting
- **isort**: Import sorting and organization
- **flake8**: Linting and style checking
- **mypy**: Static type checking
- **bandit**: Security vulnerability scanning

### Naming Conventions
```python
# Classes: PascalCase
class LanguageModel:
    pass

# Functions and variables: snake_case
def generate_embeddings(input_text: str) -> List[float]:
    model_output = []
    return model_output

# Constants: UPPER_SNAKE_CASE
MAX_BATCH_SIZE = 32
DEFAULT_MODEL_NAME = "all-mpnet-base-v2"

# Private methods: _leading_underscore
def _internal_method(self) -> None:
    pass
```

### Documentation Standards
```python
def generate_test_sequence(
    self, 
    screen_context: str, 
    test_goal: str
) -> List[Dict[str, Any]]:
    """
    Generate mobile test interaction sequence from natural language goal.
    
    This method uses the MPNet language model to convert natural language
    test objectives into executable mobile testing actions.
    
    Args:
        screen_context: Current mobile screen context with UI elements
        test_goal: Natural language description of test objective
        
    Returns:
        List of structured test actions to execute
        
    Raises:
        ModelInferenceError: If language model inference fails
        ValidationError: If screen context is invalid
        
    Example:
        >>> generator = TestGenerator(model, interface)
        >>> sequence = await generator.generate_test_sequence(
        ...     "login screen with username field",
        ...     "enter valid credentials and login"
        ... )
        >>> print(len(sequence))
        3
    """
```

## Testing Guidelines

### Test Structure
```
tests/
├── conftest.py              # Shared fixtures
├── test_language_model.py   # Language model tests
├── test_mobile_interface.py # Mobile interface tests
├── test_test_generator.py   # Test generator tests
├── integration/             # Integration tests
└── performance/             # Performance benchmarks
```

### Writing Tests
```python
import pytest
from unittest.mock import Mock, AsyncMock

class TestLanguageModel:
    """Test cases for LanguageModel functionality."""
    
    @pytest.mark.asyncio
    async def test_generate_embeddings_valid_input(self):
        """Test embedding generation with valid input."""
        model = LanguageModel()
        embeddings = await model.generate_embeddings("test input")
        
        assert len(embeddings) == 768
        assert all(isinstance(x, float) for x in embeddings)
    
    @pytest.mark.asyncio
    async def test_generate_embeddings_empty_input(self):
        """Test embedding generation with empty input."""
        model = LanguageModel()
        
        with pytest.raises(ValueError, match="Input text cannot be empty"):
            await model.generate_embeddings("")
```

### Test Categories
- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **Performance Tests**: Benchmark AI model inference speed
- **End-to-End Tests**: Test complete workflows

### Coverage Requirements
- Minimum 90% code coverage
- All public methods must have tests
- Edge cases and error conditions covered
- Performance tests for AI/ML components

## AI/ML Contribution Guidelines

### Model Development
```python
# Use proper type hints for tensor operations
import torch
from typing import Tensor, Optional

def forward(
    self, 
    input_ids: Tensor, 
    attention_mask: Optional[Tensor] = None
) -> Tensor:
    """Forward pass through the model."""
    pass
```

### Performance Considerations
- Implement efficient batching for model inference
- Use GPU acceleration when available
- Cache model outputs for repeated inputs
- Monitor memory usage with large models

### Model Evaluation
- Include performance benchmarks
- Test on multiple hardware configurations
- Validate output quality metrics
- Compare against baseline models

### Vector Database Integration
```python
# Example of proper vector database usage
async def store_embeddings(
    self,
    embeddings: List[List[float]],
    metadata: List[Dict[str, Any]]
) -> List[str]:
    """Store embeddings with metadata in vector database."""
    # Implementation with proper error handling
    pass
```

## Submitting Changes

### Pull Request Process
1. **Create descriptive PR title**: `feat: add MPNet batch processing`
2. **Fill out PR template**: Include all requested information
3. **Link related issues**: Use "Fixes #123" or "Relates to #456"
4. **Request reviews**: Tag relevant maintainers
5. **Address feedback**: Respond to review comments promptly

### PR Requirements
- [ ] All tests pass
- [ ] Code coverage maintained (≥90%)
- [ ] Documentation updated
- [ ] Pre-commit hooks pass
- [ ] No merge conflicts
- [ ] Backward compatibility maintained

### Review Process
1. **Automated Checks**: CI/CD pipeline runs
2. **Maintainer Review**: Code quality and design review
3. **AI/ML Review**: Model-specific review (if applicable)
4. **Security Review**: Security implications assessment
5. **Final Approval**: Maintainer approval and merge

### Merge Criteria
- Minimum 2 approvals from maintainers
- All automated checks pass
- Documentation is complete and accurate
- No unresolved review comments

## Getting Help

### Communication Channels
- **Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Discord**: Real-time community chat (link in README)

### Asking Questions
- Search existing issues and discussions first
- Provide minimal reproducible examples
- Include relevant environment information
- Be specific about expected vs. actual behavior

### Mentorship
New contributors are welcome! We provide:
- **Good First Issues**: Labeled for newcomers
- **Mentorship Program**: Pairing with experienced contributors
- **Documentation**: Comprehensive guides and examples
- **Code Reviews**: Constructive feedback for learning

## Recognition

Contributors are recognized through:
- **Contributors File**: Listed in CONTRIBUTORS.md
- **Release Notes**: Highlighted in changelog
- **GitHub Stats**: Contributor badges and statistics
- **Community Highlights**: Featured in community updates

## License

By contributing to DragonCrawl, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to DragonCrawl! Together, we're building the future of AI-powered mobile testing. 🚀🤖📱