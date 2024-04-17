from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



from langchain.chains import LLMChain
# from dotenv import load_dotenv
# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.agents import AgentType


def generate_pet_name(animal_type, pet_color):

    llm = ChatOpenAI(api_key="...", temperature=0.8)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are professional helper for naming pets"),
        ("user", "I have a {animal_type} pet and I want a cool name for it. It is {pet_color}. Suggest me give cool 3 names for my pet")
    ])


    chain = LLMChain(llm=llm, prompt=prompt, output_key="pet_name")


    response = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})

    return response


# def langchain_agent():
#     llm = ChatOpenAI(temperature=0.5)

#     tools = load_tools(["wikipedia", "llm-math"], llm = llm)

#     agents = initialize_agent(
#         tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
#     )

#     result = agents.run(
#         "What is the average age of a dog? Multiply the age by 3"
#     )

#     print(result)



if __name__ == "__main__":
    print(generate_pet_name("buffalo", "red"))
    # langchain_agent()
