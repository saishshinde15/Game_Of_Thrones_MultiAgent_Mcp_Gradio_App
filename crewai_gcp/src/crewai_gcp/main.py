#!/usr/bin/env python
import sys
from datetime import datetime
from typing import Dict, Any, List

from crewai_gcp.crew import GotCharacterMatcher

class GameOfThronesMatcher:
    """Main class to run the Game of Thrones character and dragon matching system."""
    
    def __init__(self):
        self.user_responses: Dict[str, str] = {}
        self.questions: List[str] = [
            "How would you describe your leadership style? (e.g., commanding, diplomatic, strategic)",
            "What's most important to you: power, family, honor, or knowledge?",
            "How do you handle conflicts or challenges? (e.g., head-on, strategically, diplomatically)",
            "What's your approach to loyalty and trust?",
            "How do you make important decisions? (e.g., logic, emotions, intuition)"
        ]
    
    def get_user_info(self) -> Dict[str, str]:
        """Get basic information from the user."""
        print("\n=== Game of Thrones Character & Dragon Matcher ===\n")
        
        while True:
            user_name = input("What's your name? ").strip()
            if user_name:
                break
            print("Please enter a valid name.")
        
        while True:
            try:
                user_age = int(input("How old are you? ").strip())
                if user_age > 0:
                    break
                print("Please enter a valid age.")
            except ValueError:
                print("Please enter a valid number for age.")
        
        return {
            "user_name": user_name,
            "user_age": user_age
        }
    
    def run_questionnaire(self) -> None:
        """Run the personality questionnaire."""
        print("\n" + "="*50)
        print("🎭  GAME OF THRONES CHARACTER MATCH  🐉")
        print("-" * 50)
        print("\nLet's find out which Game of Thrones character and dragon you are!")
        print("Please answer the following questions honestly.\n")
        
        # Clear any previous responses
        self.user_responses = {}
        
        # Define all questions with clear instructions
        questions = [
            {
                "question": "How would you describe your leadership style? (e.g., commanding, diplomatic, strategic)",
                "key": "leadership_style"
            },
            {
                "question": "What's most important to you: power, family, honor, or knowledge?",
                "key": "core_value"
            },
            {
                "question": "How do you handle conflicts or challenges? (e.g., head-on, strategically, diplomatically)",
                "key": "conflict_approach"
            },
            {
                "question": "What's your approach to loyalty and trust?",
                "key": "loyalty_approach"
            },
            {
                "question": "How do you make important decisions? (e.g., logic, emotions, intuition)",
                "key": "decision_style"
            },
            {
                "question": "In a world where power is everything, are you driven primarily by the pursuit of influence and control, or by the desire for security and a peaceful life?",
                "key": "core_motivation"
            }
        ]
        
        # Ask all questions
        for i, q in enumerate(questions, 1):
            while True:
                try:
                    print(f"\nQuestion {i}/{len(questions)}")
                    print("-" * 50)
                    response = input(f"{q['question']}\n> ").strip()
                    
                    if not response:
                        print("\n⚠️  Please provide an answer to continue.")
                        continue
                        
                    # Store the response with a meaningful key
                    self.user_responses[q['key']] = response
                    break
                    
                except KeyboardInterrupt:
                    print("\n\nQuestionnaire cancelled by user.")
                    raise
                except Exception as e:
                    print(f"\n⚠️  An error occurred: {str(e)}")
                    print("Please try again.\n")
        
        print("\n" + "="*50)
        print("\n🔮 Thank you for your answers! Analyzing your responses...")
        print("This may take a moment as we consult the ancient tomes of Westeros...\n")
    
    def record_response(self, question_num: int, response: str) -> None:
        """Record user's response to a question."""
        self.user_responses[f"q{question_num}"] = response
    
    def display_results(self, results: Any) -> None:
        """Display the matching results to the user."""
        print("\n" + "="*50)
        print("\n🎭  GAME OF THRONES CHARACTER MATCH  🐉")
        print("-" * 38)
        
        try:
            # If results is a string, just print it
            if isinstance(results, str):
                print("\n" + results)
                return
                
            # If results is a dictionary, try to extract character and dragon info
            if isinstance(results, dict):
                # Try to get character and dragon info
                character = results.get("character", {})
                dragon = results.get("dragon", {})
                
                # If we have character and dragon info, display them
                if character or dragon:
                    if character:
                        print(f"\n👑 Character Match: {character.get('name', 'Unknown')}")
                        if 'description' in character:
                            print(f"   {character['description']}")
                        if 'house' in character:
                            print(f"   House: {character['house']}")
                        if 'traits' in character and isinstance(character['traits'], list):
                            print(f"   Key Traits: {', '.join(character['traits'])}")
                    
                    if dragon:
                        print(f"\n🐉 Dragon Match: {dragon.get('name', 'Unknown')}")
                        if 'description' in dragon:
                            print(f"   {dragon['description']}")
                        if 'rider' in dragon:
                            print(f"   Rider: {dragon['rider']}")
                        if 'traits' in dragon and isinstance(dragon['traits'], list):
                            print(f"   Key Traits: {', '.join(dragon['traits'])}")
                    
                    return
                
                # If no character/dragon keys, try to find them in the root
                if 'name' in results and ('house' in results or 'rider' in results):
                    # This might be a combined result
                    if 'house' in results:
                        print(f"\n👑 Character Match: {results.get('name', 'Unknown')}")
                        print(f"   House: {results.get('house', 'Unknown')}")
                        if 'description' in results:
                            print(f"   {results['description']}")
                    
                    if 'rider' in results:
                        print(f"\n🐉 Dragon Match: {results.get('name', 'Unknown')}")
                        print(f"   Rider: {results.get('rider', 'Unknown')}")
                        if 'description' in results:
                            print(f"   {results['description']}")
                    
                    return
            
            # If we get here, try to handle CrewOutput or other objects
            if hasattr(results, 'raw_output') and results.raw_output:
                self.display_results(results.raw_output)
                return
                
            if hasattr(results, 'output') and results.output:
                self.display_results(results.output)
                return
            
            # Last resort: print the raw results
            print("\n🔍 Analysis Results:")
            print("-" * 20)
            print(str(results)[:1000])  # Limit output length
                
        except Exception as e:
            print(f"\n⚠️  An error occurred while displaying results: {str(e)}")
            print("\nRaw results for debugging:")
            print("-" * 20)
            print(str(results)[:2000])  # Limit output length
            
        print("\n" + "="*50)
    
    def run(self) -> None:
        """Run the Game of Thrones character and dragon matcher."""
        try:
            # Get user information
            user_info = self.get_user_info()
            
            # Run the questionnaire
            self.run_questionnaire()
            
            # Prepare the context with all collected information
            try:
                timestamp = str(datetime.now().isoformat())
            except Exception:
                timestamp = ""
                
            context = {
                "user_info": {
                    "name": user_info["user_name"],
                    "age": user_info["user_age"]
                },
                "questionnaire_responses": self.user_responses,
                "timestamp": timestamp
            }
            
            print("\n" + "="*50)
            print("\n🔮 Analyzing your responses...")
            print("Consulting the ancient tomes of Westeros...\n")
            
            # Initialize the crew with the prepared context
            crew = GotCharacterMatcher()
            crew_instance = crew.crew()
            
            try:
                # Run the crew with the context
                result = crew_instance.kickoff(inputs=context)
                
                # Process the result
                self.display_final_result(result, context)
                
            except Exception as e:
                print("\n" + "="*50)
                print("\n⚠️  An error occurred during analysis:")
                print(f"   {str(e)}")
                print("\nPlease try again or contact support if the issue persists.")
                print("\n" + "="*50)
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Exiting...")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again or contact support if the issue persists.")
    
    def display_final_result(self, result: Any, context: Dict[str, Any]) -> None:
        """Display the final result to the user."""
        print("\n" + "="*50)
        print("\n🎭  GAME OF THRONES CHARACTER MATCH  🐉")
        print("-" * 50)
        
        try:
            # Extract the actual content from the result
            if hasattr(result, 'raw_output') and result.raw_output:
                content = result.raw_output
            elif hasattr(result, 'output') and result.output:
                content = result.output
            else:
                content = str(result)
            
            # Clean up the content
            content = content.strip()
            
            # Remove any markdown code blocks
            content = content.replace('```', '').strip()
            
            # Remove any leading/trailing quotes
            content = content.strip('"\'')
            
            # Print the cleaned content with a dramatic separator
            print("\n" + "~*~" * 16)
            print("\n" + content + "\n")
            print("~*~" * 16 + "\n")

            # Add a more dramatic thank you message
            print("\nThank you for playing!\nMay your path be ever guided by the Old Gods and the New, and may your dragon soar high above the clouds of Westeros! 🏰🐉\nWinter is coming, but your legend has just begun...\n")
            
        except Exception as e:
            print("\n⚠️  Could not format the final result. Here's the raw output:")
            print("\n" + "-" * 50)
            print(str(result)[:2000])  # Limit output length
            print("\n" + "-" * 50)
            print(f"\nError details: {str(e)}")
            
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again or contact support if the issue persists.")
            sys.exit(1)

def run() -> None:
    """Run the Game of Thrones matcher crew."""
    try:
        matcher = GameOfThronesMatcher()
        matcher.run()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def main() -> None:
    """Main entry point for the application."""
    try:
        matcher = GameOfThronesMatcher()
        matcher.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
