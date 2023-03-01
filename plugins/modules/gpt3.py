#!/usr/bin/python

# Copyright: (c) 2023, Luis Valle <levalle232@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: gpt3

short_description: Uses OpenAi's API to query gpt3

version_added: "1.0.0"

options:
    api_key:
        description: Key pulled from your account in order to use the API
        required: true
        type: str
    model:
        description: trained model to use
        required: false
        type: str
    input:
        description: Prompt to ask the ai
        required: true
        type: str
    instruction:
        decription:
            - instruction to send over tot he ai
            - when combined with the right model, the ai can return edited code or text
        required: false
        type: str

author:
    - Luis Valle (@elchico2007)
'''

EXAMPLES = r'''
# Pass a simple input
- name: Test with an input
  luvalle.chatgpt.gpt3:
    model: "text-davinci-003"
    input: "tell me a funny joke"
    api_key: "api_key"

# Test with an instruction
- name: Test with an input
  luvalle.chatgpt.gpt3:
    model: "text-davinci-edit-001"
    input: "This is a brokan santence."
    instruction: "Fix my grammar"
    api_key: "api_key"
'''

RETURN = r'''
output:
    description: Dictionary containing choices
    type: dict
    returned: always
    sample: 
        "output": {
            "choices": [
                {
                    "finish_reason": "stop",
                    "index": 0,
                    "logprobs": null,
                    "text": "This is a test"
                }
            ],
            "created": 1677635518,
            "id": "cmpl-6p5vKFlwCi5Gpwuf9j0IcOPITP2zC",
            "model": "text-davinci-003",
            "object": "text_completion",
            "usage": {
                "completion_tokens": 37,
                "prompt_tokens": 797,
                "total_tokens": 834
            }
        }
'''

from ansible.module_utils.basic import AnsibleModule
import openai


def run_gpt3():
    module_args = dict(
        api_key=dict(type='str', required=True, no_log=True),
        model=dict(type='str', default='text-davinci-003', choices=['text-curie-001', 'text-davinci-003', 'text-babbage-001', 'text-ada-001', 'text-davinci-edit-001']),
        input=dict(type='str', required=True),
        instruction=dict(type='str', required=False),
    )

    result = dict(
        output=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    openai.api_key = module.params['api_key']

    if module.params['instruction']:
        if module.params['model'] not in ['text-davinci-edit-001', 'code-davinci-edit-001']:
            module.fail_json('You need to select "text-davinci-edit-001" or "code-davinci-edit-001" when specifying an "instruction"')
        gpt_result = openai.Edit.create(
            model=module.params['model'],
            input=module.params['input'],
            instruction=module.params['instruction']
        )
    else:
        gpt_result = openai.Completion.create(
            model=module.params['model'],
            max_tokens=2000,
            prompt=module.params['input']
        )
    # Removing leading and trailing newline
    gpt_result['choices'][0]['text'] = gpt_result['choices'][0]['text'].strip()
    result['output'] = gpt_result

    module.exit_json(**result)


def main():
    run_gpt3()


if __name__ == '__main__':
    main()
