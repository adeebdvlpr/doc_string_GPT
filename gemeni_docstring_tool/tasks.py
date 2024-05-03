from crewai import Task
from textwrap import dedent
from langchain_community.agent_toolkits import FileManagementToolkit


class AgentTasks:

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    # task for local file loading
    def read_file_contents_with_toolkit(self, file_path):
        read_tool = FileManagementToolkit( selected_tools=["read_file"]).get_tools()  # Initialize toolkit
        
        response = read_tool.invoke({"file_path": file_path})  # Invoke read file tool
        #contents = response.get("content")
        return response

    
    # code_file is the code file that the agent will be working on
    # Still need to figure out how to pass the code file to the agent
    # OR pass string = code_file contents 
    def generate_JSDoc_documentation(self, agent, code_to_modify):
        return Task(
            description=dedent(
                f"""
                Your task is to create JSDoc documentation for an entire Typescript code file, these are the instructions:
                Take an input, the contents of a code file as string in block text format.
                Identify each function in the code file and create JSDoc comments for each function as needed in the given file: {code_to_modify}.
            
                Ensure that each function is accurately documented to enhance code clarity and maintainability. Use the most recent data available.
                
                When you are finished, the code file should contain JSDoc comments for each function, describing its purpose, parameters, and return value.
                Once the task is complete, pass the modified code file as the final output to the next agent for review.         
                """
            ),
            expected_output=" Final output must be the full code file, modified with the addition of the accurate JSDoc comments and nothing else.",
            agent=agent,
        )

    def review_JSDoc_documentation(self, agent):
        return Task(
            description=dedent(
                f"""
                Your task is to meticulously review the JSDoc documentation in a provided code file and ensure its accuracy and completeness, these are the instructions:
                Review each function in the code file and verify that it has an appropriate JSDoc comment describing its purpose, parameters, and return value.
                Identify any missing or incorrect JSDoc comments and make necessary corrections or additions to accurately reflect the functionality of the code.
                Ensure that the JSDoc comments adhere to the established coding standards and conventions.
                Validate that the documentation enhances code clarity and maintainability by providing clear and concise descriptions of each function. 
                Once task is complete, pass the modified code file as the final output to the next agent for a final evaluation.                    
                """
            ),
            expected_output="Your review should result in a code file with accurate and comprehensive JSDoc comments for each function.",
            # context = [self.generate_JSDoc_documentation],
            agent=agent,
        )
    
    def evaluate_JSDoc_documentation(self, agent, code_to_modify):
        return Task(
            description=dedent(
                f"""
                Your task is to verify that the newly generated code output from the 'review_JSDoc_documentation' task contains appropriate JSDoc documentation 
                and maintains the same functionality as the original code input without JSDoc documentation in the given file: {code_to_modify}. 
                To assist in verifying that no alterations were made to any of the functions, the original code file without documentation that the prior task function 'generate_JSDoc_documentation' was passed as an argument will also be provided.
                You will prioritize thorough testing and validation procedures to guarantee that every function behaves consistently and reliably, even after the addition of documentation.
                Once the task is complete, pass the final evaluation to the next agent for the final step in the process.         
                """
            ),
            #for testing purpose made out put string, will need to chage to file/file path for eventual task of writing file to local repo
            expected_output="Your evaluation should result in a code file with garunteed accurate and comprehensive JSDoc comments for each function, and verefied no change to the functionlity of methods.",
            # context = [self.review_JSDoc_documentation],
            agent=agent,
        )