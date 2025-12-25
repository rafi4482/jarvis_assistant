class JarvisAssistant:
    def __init__(self, engine, prompt_controller, memory):
        self.engine = engine
        self.prompt_controller = prompt_controller
        self.memory = memory

    def respond(self, user_input, role):
        history = self.memory.get_history()
        prompt = self.prompt_controller.build_prompt(user_input, history, role)
        response = self.engine.generate(prompt)
        self.memory.add("User", user_input)
        self.memory.add("Assistant", response)
        return response
