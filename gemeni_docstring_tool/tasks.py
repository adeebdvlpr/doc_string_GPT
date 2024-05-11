from crewai import Task
from textwrap import dedent

class AgentTasks:

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    # code_to_modify --> 'string' = contents of code file that the agent will be working on
    def generate_JSDoc_documentation(self, agent, code_to_modify):
        return Task(
            description=dedent(
                f"""
                **Objective:**
                Your task is to Add comprehensive docstring comments to the provided TypeScript or pure JavaScript file: {code_to_modify}
                You will return the file with the complete docstring comments as required for the file.
                You will not change any of the code that is already present in the file. 
                **Instructions:**
                1. **Analyze the File:**
                Carefully examine the provided NestJS file to understand its purpose, functionality, and components (classes, interfaces, functions, etc.).
                * **@file (synonyms: @fileoverview, @overview):** Use this tag to describe the file's purpose and contents.
                2. **File-Level Comments:**
                Add a comment block at the beginning of the file using the following JSDoc tags:
                * **@file:** Specify the filename for easy identification and navigation.
                * **@description:** Provide a clear and concise overview of the file's purpose and contents.
                * **@requires:** List any external dependencies used within the file, including modules, libraries, and other files.
                * **@module:** If the file defines a module, use this tag to document it.
                * **@property:** If the file defines a module, use this tag to document it.
                * **@module: {type}** properties with the included type for the file.
                * **@example** Provide an example of how the file is used.
                3. **Class-Level Comments:**
                For each class defined in the file, add a comment block above the class declaration using the following JSDoc tags:
                * **@class (synonyms: @constructor):** Identify the class name and its purpose.
                * **@description:** Briefly explain the class's role and responsibilities within the application.
                * **@see: reference to resource that helps to explain the operation of the class
                * **@extends (synonyms: @augments):** If the class inherits from another class, use this tag to specify the parent class.
                * **@implements:** If the class implements one or more interfaces, use this tag to list them.
                * **@abstract (synonyms: @virtual):** If the class is abstract and meant to be extended, use this tag.
                * **@example:** Provide an example of how the class is used.
                4. **Method-Level Comments:**
                For each method within a class, add a comment block above the method declaration using the following JSDoc tags:
                * **@method (synonyms: @func):** Identify the method name and its purpose.
                * **@description:** Explain the method's functionality and what it achieves.
                * **@param (synonyms: @arg, @argument):** Describe each parameter, including its type and purpose.
                * **@returns (synonyms: @return):** Specify the return type and description of the returned value.
                * **@throws (synonyms: @exception):** Document any potential exceptions the method might throw.
                * **@async:** If the method is asynchronous, use this tag.
                * **@access:** Specify the access level of this method (private, package-private, public, or protected).
                * **@deprecated:** If the method is deprecated and should no longer be used, use this tag.
                * **@example:** Provide an example of how the method is used.
                5. **Additional Considerations:**
                * **Consistency:** Maintain a consistent style and format for your docstring comments throughout the entire project.
                * **Clarity:** Write clear, concise, and easy-to-understand descriptions.
                * **Completeness:** Ensure you cover all essential aspects of the file, including its purpose, functionality, and dependencies.
                * **JSDoc Tags:** Utilize other relevant JSDoc tags like @see, @link, @typedef, etc., to provide further information where necessary.
                **Outcome:**
                By following these instructions and adding proper docstring comments to the provided file, you will enable Compodoc to generate comprehensive and informative documentation, including:
                * File list with descriptions and links
                * Module dependencies visualization
                * Class and interface documentation with members and inheritance
                * Function and method documentation with descriptions, parameters, return types, and examples.

                
                When you are finished pass the modified code file as the final output to the next agent for review.         
                """
            ),
            expected_output=" Final output must be the full code file, modified with the addition of the accurate JSDoc comments and nothing else.",
            agent=agent,
        )
    
    def review_JSDoc_documentation(self, agent):
        return Task(
            description=dedent(
                f"""
                Your task is to meticulously review the JSDoc documentation in the provided code file and ensure its accuracy and completeness. 
                If needed identify any missing or incorrect JSDoc comments and make necessary corrections or additions to accurately reflect the functionality of the code.
                Validate that the documentation enhances code clarity and maintainability by providing clear and concise descriptions of each function, class, file, etc. 
                Make sure the @example tag is always used to demonstrate how each function is used, regardless if it is a async function or not.
                You will not change any of the functional code that is already present in the file.
                These are the instructions:

                1. **File-Level Comments:**
                Ensure there is a proper comment block at the beginning of the file (before any import statements) using the following JSDoc tags:
                * **@file:** Specify the filename for easy identification and navigation.
                * **@description:** Provide a clear and concise overview of the file's purpose and contents.
                * **@requires:** List any external dependencies used within the file, including modules, libraries, and other files.
                * **@module:** If the file defines a module, use this tag to document it.
                * **@property:** If the file defines a module, use this tag to document it.
                * **@module: {type}** properties with the included type for the file.
                * **@example** Provide an example of how the file is used.
                2. **Class-Level Comments:**
                For each class defined in the file,ensure there is a proper comment block above the class declaration using the following JSDoc tags:
                * **@class (synonyms: @constructor):** Identify the class name and its purpose.
                * **@description:** Briefly explain the class's role and responsibilities within the application.
                * **@see: reference to resource that helps to explain the operation of the class
                * **@extends (synonyms: @augments):** If the class inherits from another class, use this tag to specify the parent class.
                * **@implements:** If the class implements one or more interfaces, use this tag to list them.
                * **@abstract (synonyms: @virtual):** If the class is abstract and meant to be extended, use this tag.
                * **@example:** Provide an example of how the class is used.
                3. **Method-Level Comments:**
                For each method within a class, ensure there is a comment block above the method declaration using the following JSDoc tags:
                * **@method (synonyms: @func):** Identify the method name and its purpose.
                * **@description:** Explain the method's functionality and what it achieves.
                * **@param (synonyms: @arg, @argument):** Describe each parameter, including its type and purpose.
                * **@returns (synonyms: @return):** Specify the return type and description of the returned value.
                * **@throws (synonyms: @exception):** Document any potential exceptions the method might throw.
                * **@async:** If the method is asynchronous, use this tag.
                * **@access:** Specify the access level of this method (private, package-private, public, or protected).
                * **@deprecated:** If the method is deprecated and should no longer be used, use this tag.
                * **@example:** Provide an example of how the method is used.
                4. **Additional Considerations:**
                * **Consistency:** Ensure there is a consistent style and format for your docstring comments throughout the entire project.
                * **Clarity:** Ensure that there is writen clear, concise, and easy-to-understand descriptions.
                * **Completeness:** Ensure the documentation covers all essential aspects of the file, including its purpose, functionality, and dependencies.
                * **JSDoc Tags:** Utilize other relevant JSDoc tags like @see, @link, @typedef, etc., to provide further information where necessary.
                **Outcome:**
                Once task is complete, pass the modified code file as the final output to the next agent for a final evaluation.                    
                """
            ),
            expected_output="Your review should result in a code file with accurate and comprehensive JSDoc comments for each file-level element, class-level element, and function-level element.",
            # context = [self.generate_JSDoc_documentation],
            agent=agent,
        )
    
    def evaluate_JSDoc_documentation(self, agent, code_to_modify):
        return Task(
            description=dedent(
                f"""
                Your task is to verify that the newly generated code output from the 'review_JSDoc_documentation' task maintains the same functionality as the original code input without JSDoc documentation in the given file: {code_to_modify}. 
                To assist in verifying that no alterations were made to any of the functions, the original code file without documentation will also be provided to you.
                You will prioritize thorough testing and validation procedures to guarantee that every function behaves consistently and reliably, even after the addition of documentation.
                Ensure that you do not remove any of the newly added JSDoc comments, as they are essential for documentation purposes.
                Ensure that no additional code changes are made to the file, and the only modifications should be the addition of JSDoc comments.
                """
            ),
            #for testing purpose made out put string, will need to chage to file/file path for eventual task of writing file to local repo
            expected_output="Your evaluation should result in a code file with garunteed accurate and comprehensive JSDoc comments for each function, and verefied no change to the functionlity of methods.",
            # context = [self.review_JSDoc_documentation],
            agent=agent,
        )