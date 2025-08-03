"""
Tests for DragonCrawl core language model functionality.
"""

import pytest
from unittest.mock import Mock, patch

from dragoncrawl.core.language_model import LanguageModel


class TestLanguageModel:
    """Test cases for LanguageModel class."""
    
    def test_init(self):
        """Test LanguageModel initialization."""
        model = LanguageModel()
        assert model.model_name == "all-mpnet-base-v2"
        assert model._model is None
    
    def test_init_with_custom_model(self):
        """Test LanguageModel initialization with custom model."""
        custom_model = "custom-model-v1"
        model = LanguageModel(model_name=custom_model)
        assert model.model_name == custom_model
    
    @pytest.mark.asyncio
    async def test_generate_embeddings(self):
        """Test embeddings generation."""
        model = LanguageModel()
        embeddings = await model.generate_embeddings("test input")
        
        # Verify embeddings are 768-dimensional
        assert len(embeddings) == 768
        assert all(isinstance(x, float) for x in embeddings)
    
    @pytest.mark.asyncio
    async def test_generate_test_sequence(self):
        """Test test sequence generation."""
        model = LanguageModel()
        sequence = await model.generate_test_sequence(
            "login screen with username and password fields",
            "login with valid credentials"
        )
        
        # Verify sequence is returned as list
        assert isinstance(sequence, list)
        # Placeholder implementation returns empty list
        assert len(sequence) == 0