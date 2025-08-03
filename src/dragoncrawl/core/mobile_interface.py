"""
Mobile Interface for DragonCrawl.

Handles integration with mobile testing frameworks including
Appium, Espresso, and XCUITest for cross-platform testing.
"""

from typing import List, Dict, Optional, Any
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class MobileInterface(ABC):
    """
    Abstract base class for mobile testing interface implementations.
    
    Supports integration with multiple mobile testing frameworks
    for cross-platform compatibility.
    """
    
    def __init__(self, platform: str, device_config: Dict[str, Any]) -> None:
        """
        Initialize mobile interface.
        
        Args:
            platform: Mobile platform (iOS/Android)
            device_config: Device configuration parameters
        """
        self.platform = platform
        self.device_config = device_config
        logger.info(f"Initialized MobileInterface for {platform}")
    
    @abstractmethod
    async def get_screen_context(self) -> Dict[str, Any]:
        """
        Extract current screen context and UI elements.
        
        Returns:
            Screen context with UI element information
        """
        pass
    
    @abstractmethod
    async def execute_action(self, action: Dict[str, Any]) -> bool:
        """
        Execute a mobile testing action.
        
        Args:
            action: Action specification to execute
            
        Returns:
            Success status of action execution
        """
        pass
    
    async def capture_screen(self) -> str:
        """
        Capture screen for debugging and analysis.
        
        Returns:
            Path to captured screen image
        """
        # Placeholder implementation
        return "/tmp/screen_capture.png"