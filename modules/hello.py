#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

	module_args = dict(
            name=dict(type='str', required=True)
        )
	module = AnsibleModule(
				 argument_spec=module_args,
				 supports_check_mode=True
			 )
	response = {"NAME": module.params['name']}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
