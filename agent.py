from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
groq_model = os.getenv("GROQ_MODEL", "llama3-70b-8192")

class Agent:
    def __init__(self, name, model=groq_model):
        self.name = name
        self.model = model
        self.token_counter = {
            "input": 0,
            "output": 0,
            "total": 0
        }
        self.messages = []

    def run(self, prompt, max_tokens=1000):
        self.messages.append({"role": "user", "content": prompt})

        # Llamar al LLM
        response = client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=0.7,
            max_tokens=max_tokens
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})

        # Actualizar contadores de tokens
        self.token_counter["input"] += response.usage.prompt_tokens
        self.token_counter["output"] += response.usage.completion_tokens
        self.token_counter["total"] += response.usage.total_tokens

        return answer

def solve_complex_question(question):
    agents = {
        "investigator": Agent("Investigador"),
        "analyst": Agent("Analista"),
        "critic": Agent("Crítico"),
        "coordinator": Agent("Coordinador")
    }

    # Fase 1: Investigación
    research_result = agents["investigator"].run(
        f"Como investigador, busca información sobre: {question}. Proporciona datos clave y fuentes."
    )

    # Fase 2: Análisis
    analysis_result = agents["analyst"].run(
        f"Como analista, extrae patrones y detalles técnicos de: {research_result}"
    )

    # Fase 3: Crítica
    critic_result = agents["critic"].run(
        f"Como crítico, identifica errores o riesgos en: {analysis_result}"
    )

    # Fase 4: Coordinación
    final_answer = agents["coordinator"].run(
        f"Combina estos insights:\n- Investigación: {research_result}\n- Análisis: {analysis_result}\n- Crítica: {critic_result}\n\nGenera una respuesta final para: {question}"
    )

    # Cálculo de tokens
    input_tokens = sum(agent.token_counter["input"] for agent in agents.values())
    output_tokens = sum(agent.token_counter["output"] for agent in agents.values())
    total_tokens = sum(agent.token_counter["total"] for agent in agents.values())

    reasoning_tokens = (
        agents["investigator"].token_counter["total"] +
        agents["analyst"].token_counter["total"] +
        agents["critic"].token_counter["total"]
    )

    intermediate_reasoning = {
        "Investigador": research_result,
        "Analista": analysis_result,
        "Crítico": critic_result
    }

    return {
        "answer": final_answer,
        "intermediate_reasoning": intermediate_reasoning,
        "tokens": {
            "input": input_tokens,
            "output": output_tokens,
            "reasoning": reasoning_tokens,
            "total": total_tokens
        },
        "agents": agents
    }