# pip install IdeaSearch
from IdeaSearch import IdeaSearcher
from user_code.prompt import prologue_section as TemplateProgram_prologue_section
from user_code.prompt import epilogue_section as TemplateProgram_epilogue_section
from user_code.evaluation import evaluate as TemplateProgram_evaluate


def main():
    
    ideasearcher = IdeaSearcher()
    
    # set language (default: zh)
    # ideasearcher.set_language("en")
    
    # load models
    ideasearcher.set_api_keys_path("api_keys.json")
    
    # set minimum required parameters
    ideasearcher.set_program_name("TemplateProgram")
    ideasearcher.set_database_path("database")
    ideasearcher.set_evaluate_func(TemplateProgram_evaluate)
    ideasearcher.set_prologue_section(TemplateProgram_prologue_section)
    ideasearcher.set_epilogue_section(TemplateProgram_epilogue_section)
    ideasearcher.set_models([
        "Deepseek_V3",
    ])
    
    # set optional parameters
    ideasearcher.set_model_temperatures([
        1.2,
    ])
    ideasearcher.set_load_idea_skip_evaluation(False)
    
    ideasearcher.set_assess_interval(10)

    island_num = 1
    cycle_num = 1
    unit_interaction_num = 20
    
    for _ in range(island_num):
        ideasearcher.add_island()
        
    for cycle in range(cycle_num):
        
        if cycle != 0:
            ideasearcher.repopulate_islands()
    
        ideasearcher.run(unit_interaction_num)


if __name__ == "__main__":
    
    main()