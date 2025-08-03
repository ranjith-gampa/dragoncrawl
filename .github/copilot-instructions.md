# DragonCrawl Repository Guidelines for GitHub Copilot

## Project Overview
DragonCrawl is an AI-powered mobile testing framework that uses language generation models (specifically MPNet-based transformers) to create adaptive, intelligent test automation with 99%+ production stability. The project is inspired by Uber's breakthrough research in AI-powered mobile testing.

## Architecture & Technology Stack

### Core Technologies
- **Python 3.8+** with comprehensive type hints
- **FastAPI** for API framework with async/await patterns
- **PyTorch & Transformers** for MPNet-based language models
- **Sentence Transformers** for 768-dimensional embeddings
- **Appium/Selenium** for mobile testing framework integration
- **Vector Databases** (FAISS, Pinecone) for embedding storage and retrieval

### Project Structure
```
dragoncrawl/
├── src/dragoncrawl/           # Main package
│   ├── core/                  # Core AI/ML modules
│   │   ├── language_model.py  # MPNet implementation
│   │   ├── mobile_interface.py # Mobile testing integration
│   │   └── test_generator.py  # Test orchestration
│   ├── api/                   # FastAPI endpoints (future)
│   ├── models/                # ML model definitions (future)
│   └── utils/                 # Utilities (future)
├── tests/                     # Comprehensive test suite
├── docs/                      # Documentation (future)
└── docker/                    # Container configurations (future)
```

## Development Guidelines for Copilot

### Code Style & Standards
- **Always use type hints** for function parameters and return values
- **Async/await patterns** for I/O operations and ML inference
- **Comprehensive docstrings** with Args, Returns, and Examples
- **Error handling** with custom exceptions and logging
- **90%+ test coverage** requirement with pytest

### AI/ML Development Patterns
When working with AI/ML components:

1. **Embeddings Operations**
   ```python
   async def generate_embeddings(self, text: str) -> List[float]:
       """Generate 768-dimensional embeddings using MPNet."""
       # Implementation should return exactly 768 dimensions
   ```

2. **Mobile Testing Integration**
   ```python
   async def execute_action(self, action: Dict[str, Any]) -> bool:
       """Execute mobile action with error handling."""
       # Always include comprehensive error handling
   ```

3. **Language Model Patterns**
   ```python
   async def generate_test_sequence(
       self, 
       screen_context: str, 
       test_goal: str
   ) -> List[Dict[str, Any]]:
       """Generate test sequence from natural language goals."""
   ```

### Testing Patterns
- **Async test fixtures** using pytest-asyncio
- **Mock external dependencies** (models, mobile devices)
- **Property-based testing** for AI model outputs
- **Integration tests** for mobile framework compatibility

### Security & Performance
- **No hardcoded credentials** or API keys
- **Validate all inputs** especially for AI model inference
- **Efficient batching** for model operations
- **Memory management** for large embeddings and models
- **Rate limiting** for external API calls

### Mobile Testing Context
When generating mobile testing code:
- Support **cross-platform** (iOS/Android) patterns
- Include **accessibility** considerations
- Handle **different screen sizes** and orientations
- Implement **wait strategies** and retry logic
- Generate **human-readable** test reports

### AI Model Integration
When working with language models:
- Use **sentence-transformers** for embeddings
- Implement **retrieval-augmented generation** (RAG) patterns
- Include **model versioning** and caching strategies
- Handle **GPU/CPU** execution environments
- Implement **batch processing** for efficiency

## Common Patterns & Examples

### Language Model Usage
```python
from sentence_transformers import SentenceTransformer
import torch

class LanguageModel:
    def __init__(self, model_name: str = "all-mpnet-base-v2"):
        self.model = SentenceTransformer(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
```

### Mobile Interface Pattern
```python
from appium import webdriver
from typing import Protocol

class MobileDriver(Protocol):
    async def find_element(self, locator: str) -> Any: ...
    async def tap(self, x: int, y: int) -> None: ...
```

### Test Generation Pattern
```python
async def generate_test_from_goal(
    goal: str, 
    screen_context: Dict[str, Any]
) -> List[TestAction]:
    """Convert natural language goal to executable test steps."""
    # Use language model to generate sequence
    # Validate against mobile interface capabilities
    # Return structured test actions
```

### Error Handling Pattern
```python
class DragonCrawlError(Exception):
    """Base exception for DragonCrawl operations."""

class ModelInferenceError(DragonCrawlError):
    """Error during ML model inference."""

class MobileInterfaceError(DragonCrawlError):
    """Error during mobile device interaction."""
```

## Dependencies & Integrations

### Required Dependencies
- `torch>=2.1.0` - Deep learning framework
- `transformers>=4.36.0` - Transformer models
- `sentence-transformers>=2.2.0` - Embedding models
- `fastapi>=0.104.0` - Web framework
- `appium-python-client>=3.1.0` - Mobile testing
- `pytest>=7.4.0` - Testing framework

### Optional Dependencies
- `faiss-gpu` - GPU-accelerated vector search
- `pinecone-client` - Managed vector database
- `opencv-python` - Computer vision operations
- `pillow` - Image processing

## Performance Considerations
- **Batch embeddings** when possible (batch_size=32 recommended)
- **Cache model outputs** for repeated inputs
- **Use async patterns** for I/O operations
- **Monitor memory usage** with large models
- **Implement timeouts** for mobile operations

## Testing Strategy
- **Unit tests** for individual components
- **Integration tests** for AI/mobile interaction
- **Performance tests** for model inference speed
- **End-to-end tests** for complete test generation workflows
- **Property tests** for AI model output validation

## Future Development Areas
When Copilot suggests new features, prioritize:
1. **Vector database integration** for test pattern storage
2. **RAG implementation** for intelligent test generation
3. **Multi-modal models** for visual screen understanding
4. **Real-time learning** from test execution feedback
5. **Cloud deployment** patterns with model serving

This framework provides the foundation for building an industry-leading AI-powered mobile testing solution inspired by Uber's DragonCrawl research.