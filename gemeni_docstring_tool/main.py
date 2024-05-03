import logging
import vertexai
from vertexai.preview import reasoning_engines
from config import model, model_kwargs
#from Capabilities.docstring_util import add_docstrings_to_js
from textwrap import dedent
from tasks import AgentTasks

from crewai import Crew, Process

from agents import DocumentationGeneratingAgents

import sys


class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1

    def run(self): 

        tasks = AgentTasks()
        agents = DocumentationGeneratingAgents()



        # Create Agents
        senior_engineer_agent = agents.senior_engineer_agent()
        qa_engineer_agent = agents.qa_engineer_agent()
        chief_qa_engineer_agent = agents.chief_qa_engineer_agent()
        # Create Tasks
        ##########
        # Need to figure out how to pass the code file to the agent
        generate_JSDoc_documentation = tasks.generate_JSDoc_documentation(senior_engineer_agent, self.var1)
        review_JSDoc_documentation = tasks.review_JSDoc_documentation(qa_engineer_agent)
        approve_results = tasks.evaluate_JSDoc_documentation(chief_qa_engineer_agent, self.var1)

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
        return result

if __name__ == "__main__":
    print("## Welcome to Crew AI Documentation Generating Crew")
    print("-------------------------------")
    var1 = """
    \[CODE_BLOCK: example.ts\]

    function factorial(num: number): number {
        if (num === 0 || num === 1) {
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }


    function isPrime(num: number): boolean {
        if (num <= 1) {
            return false;
        }
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                return false;
            }
        }
        return true;
    }

    console.log(factorial(5)); 
    console.log(isPrime(11));
    \[/CODE_BLOCK: example.ts\]
    """

    documentation_crew = CustomCrew(var1)
    result = documentation_crew.run()

    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)

    #variable to hold code file contents as string in block text format
    #     code_to_modify = """
    # [CODE_BLOCK: example.ts]

    # function factorial(num: number): number {
    #     if (num === 0 || num === 1) {
    #         return 1;
    #     } else {
    #         return num * factorial(num - 1);
    #     }
    # }


    # function isPrime(num: number): boolean {
    #     if (num <= 1) {
    #         return false;
    #     }
    #     for (let i = 2; i <= Math.sqrt(num); i++) {
    #         if (num % i === 0) {
    #             return false;
    #         }
    #     }
    #     return true;
    # }

    # console.log(factorial(5)); 
    # console.log(isPrime(11));
    # [/CODE_BLOCK: example.ts]
    # """


