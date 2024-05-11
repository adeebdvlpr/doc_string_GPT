# custom_crew.py
from multiprocessing import Pool, cpu_count, Process
from crewai import Crew
from tasks import AgentTasks
from agents import DocumentationGeneratingAgents
from Capabilities.file_reading_tool import FileManagementTools
# from app import App
import re

class CustomCrew:
    def __init__(self, example_file_path):
        self.example_file_path = example_file_path
    @staticmethod
    def process_file(file_path):
        # Run create_file_content_string function on the file path
        file_content = FileManagementTools.create_file_content_string(file_path)

        # Initialize tasks and agents
        tasks = AgentTasks()
        agents = DocumentationGeneratingAgents()

        # Create Agents
        senior_engineer_agent = agents.senior_engineer_agent()
        qa_engineer_agent = agents.qa_engineer_agent()
        chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

        # Create Tasks
        generate_JSDoc_documentation = tasks.generate_JSDoc_documentation(senior_engineer_agent, file_content)
        review_JSDoc_documentation = tasks.review_JSDoc_documentation(qa_engineer_agent)
        approve_results = tasks.evaluate_JSDoc_documentation(chief_qa_engineer_agent, file_content)

        # Run the crew process
        crew = Crew(
            agents=[
                senior_engineer_agent,
                qa_engineer_agent,
                chief_qa_engineer_agent
            ],
            tasks=[
                generate_JSDoc_documentation,
                review_JSDoc_documentation,
                approve_results
            ],
            verbose=True
        )

        result = crew.kickoff()

        # Remove "```typescript" or "```javascript" from the beginning of the code  ###Added javascript because LLM seems to infrequently make the mistake of taggin the file with JS instead of TS
        result_without_code_block_start = re.sub(r"^```(?:typescript|javascript|ts)?\s*", "", result)

        # Remove "```" from the end of the code
        result_without_code_block_end = re.sub(r"```$", "", result_without_code_block_start)

        # Write the result back to the same file path
        with open(file_path, 'w') as output_file:
            output_file.write(result_without_code_block_end)

    @staticmethod
    def process_files(file_queue, num_processes=12):
        if num_processes is None:
            num_processes = (cpu_count() - 2)  # Use the number of CPU cores by default
        
        with Pool(processes=num_processes) as pool:
            # Convert the Queue object to a list
            file_paths = list(file_queue.queue)

            # Use pool.map with the list of file paths
            pool.map(CustomCrew.process_file, file_paths)
