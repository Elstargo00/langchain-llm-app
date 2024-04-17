from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


def generate_pet_name(animal_type, pet_color):
    llm = ChatOpenAI(temperature=0.8)

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template = "I have a {animal_type} pet and I want a cool name for it. It is {pet_color}. Suggest me five cool names for my pet"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")


    response = name_chain.invoke({"animal_type": animal_type, "pet_color": pet_color})


    return response


def langchain_agent():
    llm = ChatOpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agents = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agents.run(
        "What is the average age of a dog? Multiply the age by 3"
    )

    print(result)



if __name__ == "__main__":
    # print(generate_pet_name("buffalo", "red"))
    langchain_agent()