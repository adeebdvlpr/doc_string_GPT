from dotenv import load_dotenv
import os
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process

load_dotenv()




class DocumentationGeneratingAgents:
    def __init__(self):
        os.environ["GOOGLE_API_KEY"]="AIzaSyA-fgCMFDMI5LYdJNXtXG0r6yMaMi3UIDk"

        # Set gemini pro as llm
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro", 
            verbose=True, 
            temperature=0.9, 
            google_api_key=os.environ["GOOGLE_API_KEY"]
        )


    # Set up the agents to perform file loading / writing agents
    def file_loader_agent(self):
        return Agent(
            role='File Loader',
            goal='Read a code file from a specified file path, take the returned contents and transform them into a text block format return, pass it to the next agent for processing',
            backstory=dedent("""\
                You are a File Loader responsible for loading the code file from the specified file path.
                Your role is crucial in ensuring that the code file is correctly loaded and passed to the next agent for processing.
                As a diligent professional, you understand the importance of accurately handling the code file and ensuring its integrity throughout the documentation generation process.
                Your expertise in file management and data handling allows you to efficiently retrieve the code file and prepare it for further processing."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    # Set up the agents to perform the documentation task
    def senior_engineer_agent(self):
        return Agent(
            role='Senior Software Engineer',
            goal='Take an input of a code file. Create JSDoc comments for each function as needed',
            backstory=dedent("""\
                You are a Senior Software Engineer at a leading tech think tank.
                Your expertise is programming in JavaScript and TypeScript. You always do your best to
                understand each function in the code and produce perfect JSDoc comments."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def qa_engineer_agent(self):
        return Agent(
            role='Software Quality Control Engineer',
            goal='create code documentation by meticulously reviewing the code provided, identifying any missing or incorrect JSDoc comments, and ensuring that the documentation accurately reflects the functionality of the code.',
            backstory=dedent("""\
                You are a Software Quality Control Engineer working at a leading software development firm known for its high standards in code quality. 
                Your role is crucial in maintaining the integrity and clarity of the codebase by ensuring that the documentation is comprehensive and accurate.
                As a meticulous professional, you take pride in your work and understand the importance of clear and concise documentation. 
                Your expertise in software engineering allows you to thoroughly analyze code for errors and inconsistencies, and you have a keen eye for detail when it comes to spotting areas that require improvement.
                You strive for excellence in your work and are committed to upholding the highest standards of quality assurance in software development."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    
    def chief_qa_engineer_agent(self):
        return Agent(
            role='Chief Software Quality Control Engineer',
            goal='Verify that the newly generated code, containing JSDoc documentation, maintains the same functionality as the original code file input without JSDoc documentation. You prioritize thorough testing and validation procedures to guarantee that every function behaves consistently and reliably, even after the addition of documentation.',
            backstory=dedent("""\
                You are a seasoned Chief Software Quality Control Engineer with extensive experience in overseeing the quality assurance processes of complex software projects. 
                Your role is pivotal in ensuring the reliability and functionality of the codebase, particularly during the integration of JSDoc documentation.
                As the chief authority in software quality control, you understand the critical importance of preserving the functionality of the code while enhancing its documentation. 
                Your expertise lies in meticulously assessing each function to ensure that it performs its intended task accurately and efficiently.
                With your leadership and expertise, you strive to maintain the highest standards of quality assurance, ensuring that the codebase remains robust and dependable throughout the documentation enhancement process."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    
# will i need somrthing that extracts the file path from the original file input and passes the file path to the agent?
    def llm_response_handler_agent(self):
        return Agent(
            role='LLM Response Handler',
            goal='Take the response from the LLM verified by the Chief Software Quality Control Engineer, then add it to the local repository, replacing the current file at the file path.',     
            backstory=dedent("""\
                You are an LLM Response Handler responsible for integrating responses generated by the Language Model into the local codebase.
                Your role is crucial in ensuring that the codebase remains up-to-date and well-documented.
                As the final step in the documentation generation process, you take the verified response from the Chief Software Quality Control Engineer and seamlessly integrate it into the local repository.
                Your expertise in version control systems and code management ensures a smooth and efficient integration process.
                You prioritize accuracy and reliability, ensuring that the updated code maintains its functionality and adheres to the established coding standards."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )



