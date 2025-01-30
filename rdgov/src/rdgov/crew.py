from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os

@CrewBase
class Rdgov():
	"""Stock Analysis Crew"""

	# Define configuration files
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# --- Define Agents ---
	@agent
	def manager_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['manager_agent'],
			verbose=True)


	@agent
	def admin(self) -> Agent:
		return Agent(
			config=self.agents_config['admin'],
			verbose=True
		)

	@agent
	def planner(self) -> Agent:
		return Agent(
			config=self.agents_config['planner'],
			verbose=True
		)

	@agent
	def engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['engineer'],
			verbose=True
		)

	@agent
	def executor(self) -> Agent:
		return Agent(
			config=self.agents_config['executor'],
			verbose=True
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config['writer'],
			verbose=True
		)

	# --- Define Tasks ---
	@task
	def planning_task(self) -> Task:
		return Task(
			config=self.tasks_config['planning_task']
		)

	@task
	def coding_task(self) -> Task:
		return Task(
			config=self.tasks_config['coding_task']
		)

	@task
	def execution_task(self) -> Task:
		return Task(
			config=self.tasks_config['execution_task']
		)

	

	@task
	def writing_task(self) -> Task:
		# Generate Markdown content
		markdown_content = """
		# Nvidia Stock Price Performance (April 2024)

		In the past month, Nvidia's stock showed the following key performance trends:

		- Opening price: $XXX
		- Highest price: $XXX
		- Lowest price: $XXX
		- Closing price: $XXX

		## Insights and Analysis

		The stock demonstrated significant growth due to...
		"""

		# Try opening the file with file-safe handling
		try:
			file_path = 'output/blogpost.md'
			with open(file_path, 'w') as file:
				file.write(markdown_content)

			print(f"Blog post saved to '{file_path}'")

		except FileNotFoundError:
			raise Exception("The 'output/' directory does not exist. Please create it manually.")

		return Task(config=self.tasks_config['writing_task'])




	@task
	def admin_task(self) -> Task:
		return Task(
			config=self.tasks_config['admin_task']
		)
	
	@task
	def feedback_task(self) -> Task:
		return Task(
			config=self.tasks_config['feedback_task']
		)


	# --- Define the Crew ---
	@crew
	def crew(self) -> Crew:
		"""Creates the Crew (with hierarchical process) for Stock Analysis"""
		print("Agents in crew (before assigning manager):")
		for agent in self.agents:
			print(f" - {agent.role}")

		print("\nManager agent:", self.manager_agent().role)
		return Crew(
			agents=self.agents, # Exclude manager
			tasks=self.tasks, # Automatically includes all @task decorators
			process=Process.hierarchical, # agents can only speak to agents of higher rank
			manager_agent=self.manager_agent(),
			verbose=True
		)
