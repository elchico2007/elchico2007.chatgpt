# elchico2007.chatgpt
The Ansible module written to use the ChatGPT API allows users to leverage the power of the ChatGPT language model within their Ansible playbooks. The module enables users to send text prompts to the ChatGPT API and receive responses in real-time, facilitating automated communication and decision-making in various use cases. The module's parameters include the API endpoint, authentication credentials, and the text prompt to send to the API. Once the API processes the prompt, the response is returned to the module and can be further used within the playbook. The module's functionality can be extended to support more complex interactions with the ChatGPT API, making it a valuable addition to any Ansible automation workflow.

## Included Content
### Modules
Name | Description
--- | ---
GPT3 | Module used to send input to the OpenAi API and get a returned output

## Installing this collection

You can install the chatgpt collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install elchico2007.chatgpt

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: elchico2007.chatgpt
```
## Using this collection

The following example shows how to send a prompt using the 'text-davinci-003'

```yaml
---
- name: Test with an input
  elchico2007.chatgpt.gpt3:
    model: "text-davinci-003"
    input: "Given the following switch config '{{ ios_config }}', how can this device be made safer?"
    api_key: "api_key"
```
## Getting your API Key
Create an account https://platform.openai.com/ then go over to https://platform.openai.com/account/api-keys to generate a unique key.

## Models available
Model | Description
--- | ---
text-davinci-003 | Can do any language task with better quality, longer output, and consistent instruction-following than the curie, babbage, or ada models. Also supports inserting completions within text.
text-davinci-002 | Similar capabilities to text-davinci-003 but trained with supervised fine-tuning instead of reinforcement learning
code-davinci-002 | Optimized for code-completion tasks
