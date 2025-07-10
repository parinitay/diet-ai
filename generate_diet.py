from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

def generate_diet(
    age: int,
    gender: str,
    body_comp: str,
    activity_level: str
) -> str:
    """
    Generate a personalized diet recommendation based on user input.

    Parameters:
    - age (int): The user's age
    - gender (str): 'Male' or 'Female'
    - body_comp (str): Body composition category
    - activity_level (str): Physical activity level

    Returns:
    - A string with personalized diet advice.
    """

    template = """
    You are a nutrition expert tasked with recommending the most relevant aspects of a person's diet 
    based on their core attributes. Given the following details:

    Age: {age}
    Sex/Gender: {gender}
    Body Composition: {body_comp}
    Activity Level: {activity_level}

    Output a list of key diet aspects this person should focus on. Cover:

    - Macronutrient balance
    - Caloric needs
    - Timing/frequency of meals
    - Foods to prioritize or avoid
    - Supplement needs (if applicable)
    - Any special recommendations

    Keep the recommendations concise, practical, and personalized.
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["age", "gender", "body_comp", "activity_level"]
    )

    llm = ChatOllama(model="llama3")
    diet_chain = prompt | llm

    res = diet_chain.invoke({
        "age": age,
        "gender": gender,
        "body_comp": body_comp,
        "activity_level": activity_level
    })

    return res.content


# Optional: CLI test
if __name__ == "__main__":
    result = generate_diet(
        age=22,
        gender="Female",
        body_comp="Average",
        activity_level="Moderate"
    )
    print(result)
