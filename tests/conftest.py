"""
Pytest configuration and shared fixtures for DragonCrawl tests.
"""

import pytest
import asyncio
from typing import Generator, Any
from unittest.mock import Mock

from dragoncrawl.core.language_model import LanguageModel
from dragoncrawl.core.mobile_interface import MobileInterface
from dragoncrawl.core.test_generator import TestGenerator


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def language_model() -> LanguageModel:
    """Create a language model instance for testing."""
    return LanguageModel(model_name="test-model")


@pytest.fixture
async def mock_mobile_interface() -> Mock:
    """Create a mock mobile interface for testing."""
    mock_interface = Mock(spec=MobileInterface)
    mock_interface.platform = "test"
    mock_interface.device_config = {"device": "test_device"}
    
    # Configure async methods
    mock_interface.get_screen_context.return_value = {
        "elements": [],
        "screen_size": {"width": 1080, "height": 1920}
    }
    mock_interface.execute_action.return_value = True
    mock_interface.capture_screen.return_value = "/tmp/test_screen.png"
    
    return mock_interface


@pytest.fixture
async def test_generator(
    language_model: LanguageModel, 
    mock_mobile_interface: Mock
) -> TestGenerator:
    """Create a test generator instance for testing."""
    return TestGenerator(language_model, mock_mobile_interface)


@pytest.fixture
def sample_test_goals() -> list[str]:
    """Sample test goals for testing."""
    return [
        "Login with valid credentials",
        "Navigate to user profile",
        "Update profile information",
        "Logout successfully"
    ]