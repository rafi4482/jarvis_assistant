class PromptController:
    def build_prompt(self, user_input, memory, role):
        system_instruction = {
            "Tutor": "You are a patient tutor who explains concepts clearly.",
            "Coder": "You are a senior software engineer who helps with code.",
            "Mentor": "You are a career mentor giving practical advice."
        }[role]

        prompt = f"""
System: {system_instruction}

Conversation History:
{memory}

User: {user_input}
Assistant:
"""
        return prompt
