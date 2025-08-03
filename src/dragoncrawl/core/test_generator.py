"""
Test Generator for DragonCrawl.

Orchestrates the language model and mobile interface to generate
and execute intelligent mobile test sequences.
"""

from typing import List, Dict, Optional, Any
import logging

from .language_model import LanguageModel
from .mobile_interface import MobileInterface

logger = logging.getLogger(__name__)


class TestGenerator:
    """
    Main test generation orchestrator for DragonCrawl.
    
    Combines language model capabilities with mobile interface
    to generate and execute adaptive test sequences.
    """
    
    def __init__(
        self, 
        language_model: LanguageModel,
        mobile_interface: MobileInterface
    ) -> None:
        """
        Initialize test generator.
        
        Args:
            language_model: Language model instance
            mobile_interface: Mobile interface instance
        """
        self.language_model = language_model
        self.mobile_interface = mobile_interface
        logger.info("Initialized TestGenerator")
    
    async def generate_test_plan(
        self, 
        test_goals: List[str],
        max_steps: int = 50
    ) -> Dict[str, Any]:
        """
        Generate comprehensive test plan from goals.
        
        Args:
            test_goals: List of natural language test objectives
            max_steps: Maximum number of test steps to generate
            
        Returns:
            Generated test plan with execution steps
        """
        logger.info(f"Generating test plan for {len(test_goals)} goals")
        
        # Get current screen context
        screen_context = await self.mobile_interface.get_screen_context()
        
        test_plan = {
            "goals": test_goals,
            "steps": [],
            "metadata": {
                "max_steps": max_steps,
                "screen_context": screen_context
            }
        }
        
        # Generate steps for each goal
        for goal in test_goals:
            steps = await self.language_model.generate_test_sequence(
                str(screen_context), goal
            )
            test_plan["steps"].extend(steps)
        
        return test_plan
    
    async def execute_test_plan(self, test_plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute generated test plan on mobile device.
        
        Args:
            test_plan: Test plan to execute
            
        Returns:
            Execution results with success metrics
        """
        logger.info("Executing test plan")
        
        results = {
            "success": False,
            "steps_executed": 0,
            "steps_total": len(test_plan["steps"]),
            "errors": []
        }
        
        for step in test_plan["steps"]:
            try:
                success = await self.mobile_interface.execute_action(step)
                if success:
                    results["steps_executed"] += 1
                else:
                    results["errors"].append(f"Failed to execute step: {step}")
            except Exception as e:
                results["errors"].append(f"Error executing step: {e}")
        
        results["success"] = results["steps_executed"] == results["steps_total"]
        return results