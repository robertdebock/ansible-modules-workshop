#!/usr/bin/python
# Import necesary libraries
from ansible.module_utils.basic import AnsibleModule

# end import modules
# start defining the functions

def create_file(module, full_path_name):
    # create file
    # uses touch to create a file
    result = {}
    touch = module.get_bin_path("touch")
    (rc, out, err) = module.run_command([touch, full_path_name])
    if rc == 0:
        result['changed'] = True
        result['msg'] = "file: " + full_path_name + " created"
    else:
        module.fail_json(
                 msg="Could not create " + full_path_name, rc=rc, err=err)
    return result


def remove_file(module, full_path_name):
    # remove file
    # uses rm to remove file
    result = {}
    rm = module.get_bin_path("rm")
    (rc, out, err) = module.run_command([rm, full_path_name])
    if rc == 0:
        result['changed'] = True
        result['msg'] = "file: " + full_path_name + " removed"
    else:
        module.fail_json(
                 msg="Could not remove " + full_path_name, rc=rc, err=err)
    return result


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            location=dict(type='str', default='/tmp'),
            state=dict(type='str', choices=['absent', 'present'],
                    default='present'),
        ),
    )

    result = {
        'msg': "",
        'changed': False
    }

    full_path_name = module.params['location'] + "/" + module.params['name']

    if module.params['state'] == 'present':
            result = create_file(module, full_path_name)
    else:
            result = remove_file(module, full_path_name)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
