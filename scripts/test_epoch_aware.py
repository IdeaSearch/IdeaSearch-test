# pip install IdeaSearch
from IdeaSearch import IdeaSearcher
from user_code.prompt import prologue_section as TemplateProgram_prologue_section
from user_code.prompt import epilogue_section as TemplateProgram_epilogue_section
from user_code.evaluation import evaluate as TemplateProgram_evaluate
from user_code.initial_ideas import initial_ideas as TemplateProgram_initial_ideas


def main():
    
    ideasearcher = IdeaSearcher()

    ideasearcher.set_api_keys_path("api_keys.json")
 
    ideasearcher.set_program_name("EpochAwareTest")
    ideasearcher.set_database_path("database")
    ideasearcher.set_evaluate_func(TemplateProgram_evaluate)
    ideasearcher.set_prologue_section(TemplateProgram_prologue_section)
    ideasearcher.set_epilogue_section(TemplateProgram_epilogue_section)
    ideasearcher.add_initial_ideas(TemplateProgram_initial_ideas)
    
    island_num = 2
    cycle_num = 3
    unit_interaction_num = 10
    
    for _ in range(island_num):
        ideasearcher.add_island()
        
    for cycle in range(cycle_num):
        ideasearcher.set_models(["Deepseek_V3"] * (cycle + 1))
        ideasearcher.set_model_temperatures([0.9 + 0.1 * i for i in range(cycle + 1)])
        if cycle != 0: ideasearcher.repopulate_islands()
        ideasearcher.run(unit_interaction_num)
        
    print(ideasearcher.get_best_idea())


if __name__ == "__main__":
    
    main()