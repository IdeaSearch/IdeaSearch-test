# pip install IdeaSearch
from IdeaSearch import IdeaSearcher
from user_code.prompt import prologue_section as TemplateProgram_prologue_section
from user_code.prompt import epilogue_section as TemplateProgram_epilogue_section
from user_code.evaluation import evaluate as TemplateProgram_evaluate
from user_code.initial_ideas import initial_ideas as TemplateProgram_initial_ideas
from user_code.generate_prompt import generate_prompt_func as TemplateProgram_generate_prompt_func


def main():
    
    ideasearcher = IdeaSearcher()
    
    # set language (default: zh; available: zh, en)
    ideasearcher.set_language("zh")
    
    # set your api keys
    ideasearcher.set_api_keys_path("api_keys.json")
    
    # set minimum required parameters
    ideasearcher.set_program_name("TemplateProgram")
    ideasearcher.set_database_path("database")
    
    ideasearcher.set_evaluate_func(TemplateProgram_evaluate)
    
    additional_freedom_needed = True
    
    if additional_freedom_needed:
        
        # experimental and less recommended
        ideasearcher.set_generate_prompt_func(TemplateProgram_generate_prompt_func)
        
    else:
        
        ideasearcher.set_prologue_section(TemplateProgram_prologue_section)
        ideasearcher.set_epilogue_section(TemplateProgram_epilogue_section)
        
    ideasearcher.set_models([
        "Deepseek_V3",
    ])
    
    
    # set optional parameters
    ideasearcher.set_model_temperatures([
        1.2,
    ])
    ideasearcher.set_record_prompt_in_diary(True)

    # add initial ideas if you don't want to dive into file system
    ideasearcher.add_initial_ideas(TemplateProgram_initial_ideas)
    
    # set running settings
    # total_interaction_num = island_num * cycle_num * unit_interaction_num
    
    island_num = 2
    cycle_num = 3
    unit_interaction_num = 10
    
    # start running
    for _ in range(island_num):
        ideasearcher.add_island()
        
    for cycle in range(cycle_num):
        
        if cycle != 0:
            ideasearcher.repopulate_islands()
    
        ideasearcher.run(unit_interaction_num)
        
    # utilize results
    print(ideasearcher.get_best_idea())


if __name__ == "__main__":
    
    main()