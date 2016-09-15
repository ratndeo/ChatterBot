from output_adapter import OutputAdapter
from terminal import TerminalAdapter
from chatterbot.utils.module_loading import import_module
from chatterbot.conversation import Statement


class ActionAdapter(OutputAdapter):
    def __init__(self, **kwargs):
        super(ActionAdapter, self).__init__(**kwargs)
        delegate_adapter_path = kwargs.get("delegate_adapter")
        self.delegate_adapter = import_module(delegate_adapter_path)(**kwargs) or TerminalAdapter(**kwargs)

        self.action_map = kwargs.get("action_map", {})

    def process_response(self, statement):
        text = statement.text
        if not text:
            return self.delegate_adapter.process_response(statement)

        tokens = text.split()
        for token in tokens:
            if token[0] == "{" and token[-1] == "}":
                action_token = token[1:-1]
                action_executor_s = self.action_map.get(action_token)
                if action_executor_s:
                    action_executor = import_module(action_executor_s)
                    token_response = action_executor()
                    text = text.replace(token, token_response)

        return self.delegate_adapter.process_response(Statement(text))
