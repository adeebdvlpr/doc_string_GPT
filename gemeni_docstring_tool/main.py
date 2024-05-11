# main.py - Main logic excluding GUI
import logging
from textwrap import dedent
import re
from multiprocessing import Pool, cpu_count, Process
from Capabilities.file_reading_tool import FileManagementTools
from Capabilities.file_collecting import collect_ts_files, queue_ts_files
# from custom_crew import CustomCrew
from app import App



# class CustomCrew:
#     def __init__(self, example_file_path):
#         self.example_file_path = example_file_path
        
    # def process_file(file_path):
    #     # Run create_file_content_string function on the file path
    #     file_content = FileManagementTools.create_file_content_string(file_path)

    #     # Initialize tasks and agents
    #     tasks = AgentTasks()
    #     agents = DocumentationGeneratingAgents()

    #     # Create Agents
    #     senior_engineer_agent = agents.senior_engineer_agent()
    #     qa_engineer_agent = agents.qa_engineer_agent()
    #     chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

    #     # Create Tasks
    #     generate_JSDoc_documentation = tasks.generate_JSDoc_documentation(senior_engineer_agent, file_content)
    #     review_JSDoc_documentation = tasks.review_JSDoc_documentation(qa_engineer_agent)
    #     approve_results = tasks.evaluate_JSDoc_documentation(chief_qa_engineer_agent, file_content)

    #     # Run the crew process
    #     crew = Crew(
    #         agents=[
    #             senior_engineer_agent,
    #             qa_engineer_agent,
    #             chief_qa_engineer_agent
    #         ],
    #         tasks=[
    #             generate_JSDoc_documentation,
    #             review_JSDoc_documentation,
    #             approve_results
    #         ],
    #         verbose=True
    #     )

    #     result = crew.kickoff()

    #     # Remove "```typescript" or "```javascript" from the beginning of the code  ###Added javascript because LLM seems to infrequently make the mistake of taggin the file with JS instead of TS
    #     result_without_code_block_start = re.sub(r"^```(?:typescript|javascript|ts)?\s*", "", result)

    #     # Remove "```" from the end of the code
    #     result_without_code_block_end = re.sub(r"```$", "", result_without_code_block_start)

    #     # Write the result back to the same file path
    #     with open(file_path, 'w') as output_file:
    #         output_file.write(result_without_code_block_end)

    
    # @staticmethod
    # def process_files(file_queue, num_processes=5):
        # if num_processes is None:
        #     num_processes = cpu_count()  # Use the number of CPU cores by default
        
        # # Start the GUI process
        # gui_process = Process(target=App.run_gui)
        # gui_process.start()

        # with Pool(processes=num_processes) as pool:
        #     # Convert the Queue object to a list
        #     file_paths = list(file_queue.queue)

        #     # Use pool.map with the list of file paths
        #     pool.map(CustomCrew.process_file, file_paths)

if __name__ == "__main__":
    print("## Welcome to Crew AI Documentation Generating Crew")
    print("-------------------------------")
    App.run_gui()
    print("-------------------------------")

    print("\n\n########################")
    print("## The application has completed. Your code file now contains proper documentation! ")
    print("########################\n")
    

