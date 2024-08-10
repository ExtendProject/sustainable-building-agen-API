def MainPrompt(user_name,budget,location,current_weather_condition,product_data):
    
    return f"""sumary_line
    From these building images and the given user information, 
    tell the user what they can do to make their house sustainable, 
    list all the materials, objects, and tools in this house, 
    and advise them on how to allocate the budget to each of the necessary building materials in sections or phases so that they can choose the best one that works for them.
    Compare some of the materials and tools they have in the house to some affordable market product equivalents and suggest more sustainable materials or tools. 
    Give them the ones that are more cost-efficient. Structure your results in a tabular and list format.

    In the result, provide the following information:
    - Materials/Objects/Tools
    - Observed in Image
    - Sustainable alternative
    - Found alternatives from the Market with their (Prices)
    - Cost-Efficient (Yes/No)
    - Notes
    - Budget Allocations: add the percentages to it 
    - Recommendations

    and other important observations

    NOTE: The primary goal is to make this whole process sustainable and reduce cost.

    USER INFORMATION:
    _____________________________________
    Name: {user_name}
    Current Budget: {budget} (in GHS) 
    Location: {location}
    Weather Condition: {current_weather_condition}
    Products From the Market: {product_data}
    _____________________________________
    """
    


    