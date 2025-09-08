#!/usr/bin/env python3
"""
Game of Thrones Character Matcher - Demo Script

This script demonstrates the core functionality of the GoT Character Matcher
with example responses and detailed output analysis.
"""

import sys
import os
from datetime import datetime

# Add src to Python path for imports
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'crewai_gcp', 'src')
sys.path.insert(0, src_path)

try:
    from crewai_gcp.crew import GotCharacterMatcher
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("🔧 Make sure to set PYTHONPATH correctly:")
    print("   export PYTHONPATH=/path/to/crewai_gcp/src")
    sys.exit(1)

def demo_character_analysis():
    """Demonstrate character analysis with sample responses."""
    
    print("🏰 Game of Thrones Character & Dragon Matcher Demo")
    print("=" * 60)
    
    # Sample user profiles for demonstration
    sample_profiles = [
        {
            "name": "Strategic Leader",
            "user_info": {
                "name": "Alex Strategist",
                "age": 30
            },
            "questionnaire_responses": {
                "leadership_style": "Strategic and calculated, preferring to plan several moves ahead",
                "core_value": "Knowledge and strategic advantage over raw power",
                "conflict_approach": "Strategically, using intelligence and planning to outmaneuver opponents",
                "loyalty_approach": "Earned through mutual respect and proven competence",
                "decision_style": "Logic combined with long-term strategic thinking",
                "core_motivation": "Pursuit of influence through knowledge and strategic positioning"
            }
        },
        {
            "name": "Honor-Bound Warrior",
            "user_info": {
                "name": "Jordan Noble",
                "age": 28
            },
            "questionnaire_responses": {
                "leadership_style": "Leading by example with unwavering moral principles",
                "core_value": "Honor and doing what is right, regardless of personal cost",
                "conflict_approach": "Head-on with courage, but always maintaining honor",
                "loyalty_approach": "Absolute loyalty to those who prove themselves worthy",
                "decision_style": "Following moral principles and gut instincts about right and wrong",
                "core_motivation": "Desire for security and protecting those who cannot protect themselves"
            }
        },
        {
            "name": "Family-First Diplomat",
            "user_info": {
                "name": "Sam Guardian",
                "age": 35
            },
            "questionnaire_responses": {
                "leadership_style": "Diplomatic and collaborative, building consensus and alliances",
                "core_value": "Family and the bonds that tie people together",
                "conflict_approach": "Diplomatically, seeking peaceful solutions and compromises",
                "loyalty_approach": "Family comes first, but loyalty extends to close allies",
                "decision_style": "Emotions and consideration for how decisions affect loved ones",
                "core_motivation": "Desire for security and a peaceful life for family"
            }
        }
    ]
    
    for i, profile in enumerate(sample_profiles, 1):
        print(f"\n🎭 Demo Profile {i}: {profile['name']}")
        print("-" * 40)
        
        # Add timestamp to context
        context = {
            **profile,
            "timestamp": str(datetime.now().isoformat())
        }
        
        print("📋 Input Profile:")
        print(f"   Name: {context['user_info']['name']}")
        print(f"   Age: {context['user_info']['age']}")
        print(f"   Leadership: {context['questionnaire_responses']['leadership_style']}")
        print(f"   Core Value: {context['questionnaire_responses']['core_value']}")
        print(f"   Conflict Style: {context['questionnaire_responses']['conflict_approach']}")
        
        try:
            print("\n🔮 Analyzing with CrewAI Multi-Agent System...")
            print("   ⏳ This may take 1-2 minutes...")
            
            # Initialize and run CrewAI
            crew = GotCharacterMatcher()
            crew_instance = crew.crew()
            result = crew_instance.kickoff(inputs=context)
            
            # Process result
            if hasattr(result, 'raw_output') and result.raw_output:
                content = result.raw_output
            elif hasattr(result, 'output') and result.output:
                content = result.output
            else:
                content = str(result)
            
            # Clean up formatting
            content = content.replace('```', '').strip('"\'\n ')
            
            print("\n🎉 Analysis Complete!")
            print("=" * 60)
            print(content)
            print("=" * 60)
            
        except Exception as e:
            print(f"\n❌ Error during analysis: {e}")
            print("🔧 Possible solutions:")
            print("   - Check Google Cloud authentication")
            print("   - Verify internet connection")
            print("   - Ensure all dependencies are installed")
        
        if i < len(sample_profiles):
            input("\nPress Enter to continue to next demo profile...")

def test_mcp_integration():
    """Test MCP server functionality."""
    
    print("\n🔧 MCP Integration Test")
    print("-" * 30)
    
    try:
        # Import MCP components
        from mcp.server.fastmcp import FastMCP
        
        print("✅ MCP imports successful")
        
        # Test MCP server creation
        mcp = FastMCP("got_matcher_test")
        print("✅ MCP server creation successful")
        
        # Test tool registration
        @mcp.tool()
        def test_tool(test_input: str) -> str:
            """Test tool for MCP functionality."""
            return f"Test successful: {test_input}"
        
        print("✅ MCP tool registration successful")
        
        print("\n🎯 MCP Integration appears to be working correctly!")
        print("To run the MCP server:")
        print("   cd crewai_gcp")
        print("   PYTHONPATH=./src python mcp_server.py")
        
    except ImportError as e:
        print(f"❌ MCP Import Error: {e}")
        print("🔧 Install FastMCP: pip install fastmcp")
    except Exception as e:
        print(f"❌ MCP Test Error: {e}")

def test_interfaces():
    """Test interface configurations."""
    
    print("\n🌐 Interface Configuration Test")
    print("-" * 35)
    
    # Test Gradio
    try:
        import gradio as gr
        print("✅ Gradio import successful")
        
        # Test basic interface creation
        def dummy_function(text):
            return f"Processed: {text}"
        
        iface = gr.Interface(
            fn=dummy_function,
            inputs=gr.Textbox(label="Test Input"),
            outputs=gr.Textbox(label="Test Output"),
            title="Test Interface"
        )
        print("✅ Gradio interface creation successful")
        
    except ImportError as e:
        print(f"❌ Gradio Import Error: {e}")
    
    # Test Streamlit
    try:
        import streamlit as st
        print("✅ Streamlit import successful")
        
    except ImportError as e:
        print(f"❌ Streamlit Import Error: {e}")

def main():
    """Main demo function."""
    
    print("🐉 Welcome to the Game of Thrones Character Matcher Demo!")
    print("This demo will show you how the multi-agent system works.")
    print("\n" + "=" * 70)
    
    while True:
        print("\n🎯 Demo Options:")
        print("1. Run Character Analysis Demo (with sample profiles)")
        print("2. Test MCP Integration")
        print("3. Test Interface Configurations")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            demo_character_analysis()
        elif choice == "2":
            test_mcp_integration()
        elif choice == "3":
            test_interfaces()
        elif choice == "4":
            print("\n🏰 May your dragon soar high above the clouds of Westeros!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()