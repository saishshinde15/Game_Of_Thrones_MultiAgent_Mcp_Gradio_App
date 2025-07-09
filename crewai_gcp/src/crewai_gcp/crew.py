from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class GotCharacterMatcher():
    """Game of Thrones Character and Dragon Matcher Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def questioner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['questioner_agent'],
            verbose=True
        )

    @agent
    def character_matcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['character_matcher_agent'],
            verbose=True
        )

    @agent
    def dragon_matcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['dragon_matcher_agent'],
            verbose=True
        )

    @task
    def ask_personality_questions(self) -> Task:
        return Task(
            config=self.tasks_config['ask_personality_questions'],
            agent=self.questioner_agent()
        )

    @task
    def analyze_character_match(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_character_match'],
            agent=self.character_matcher_agent()
        )

    @task
    def analyze_dragon_match(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_dragon_match'],
            agent=self.dragon_matcher_agent()
        )

    @task
    def present_results(self) -> Task:
        return Task(
            config=self.tasks_config['present_results'],
            agent=self.character_matcher_agent()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
