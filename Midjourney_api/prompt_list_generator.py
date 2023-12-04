def prompt_list_generator(prompt_list, company_name):
    updated_list = [prompt.replace("{company_type}", company_name) for prompt in prompt_list]
    return updated_list

