from crewai import Agent, Task, Crew
from datetime import datetime

### [Agent ---> Tasks] --> CrewAI ---> kicoff ---> Result
#
# 
# 
# 
from dotenv import load_dotenv
load_dotenv() 

from crewai import LLM

llm = LLM(
    model="gpt-4o",
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)

escritor_de_newsletter = Agent(
    role="Escritor de Newsletter", # Qual é a função do agente
    goal = "Escrever uma newsletter com muita qualidade e linguagem de fácil acesso para todos os públicos.", # QUal é o objetivo desse agente
    backstory = "Você é um escritor de artigos científicos e de newsletter em revistas brasileiras, você é amplamente elogiado pela sua qualidade de escrita em seus materiais.", # Qual é o conhecimento/vivência do Agente
    allow_delegation = False,
    model=llm
) 

newsletter = Task(
    description = f"Escreva uma newsletter com o tema de `Importância do Aprendizado de Computação para pessoas da Terceira Idade`. Tenha em mente a data de hoje: {datetime.now().strftime('%d/%m/%Y')}",
    agent = escritor_de_newsletter,
    expected_output = "Uma newsletter top das galáxias"
)

crew = Crew(
    agents = [escritor_de_newsletter],
    tasks = [newsletter],
    verbose = True,
    memory = True
)

output = str(crew.kickoff())

print(f"Saída do Agente ======= {output}")



