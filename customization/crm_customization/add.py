import os
import shutil


def copy_and_replace(source_path, destination_path):
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)

def after_install():
    print('This is custom app running')
    current_working_directory = os.getcwd()
    print(current_working_directory)
    # html
    source_file = '../apps/customization/customization/crm_customization/crm_activities.html'
    destination_file = '../apps/erpnext/erpnext/public/js/templates/crm_activities.html'
    copy_and_replace(source_file, destination_file)
    # crm_activities.js
    source_file = '../apps/customization/customization/crm_customization/crm_activities.js'
    destination_file = '../apps/erpnext/erpnext/public/js/utils/crm_activities.js'
    copy_and_replace(source_file, destination_file)
    # util.py
    source_file = '../apps/customization/customization/crm_customization/utils.py'
    destination_file = '../apps/erpnext/erpnext/crm/utils.py'
    copy_and_replace(source_file, destination_file)
    # api.py
    source_file = '../apps/customization/customization/crm_customization/api.py'
    destination_file = '../apps/frappe/frappe/desk/doctype/todo/api.py'
    copy_and_replace(source_file, destination_file)
    # project.py
    source_file = '../apps/customization/customization/crm_customization/project.py'
    destination_file = '../apps/erpnext/erpnext/projects/doctype/project/project.py'
    copy_and_replace(source_file, destination_file)
    # goal.py
    source_file = '../apps/customization/customization/crm_customization/goal.py'
    destination_file = '../apps/hrms/hrms/hr/doctype/goal/goal.py'
    copy_and_replace(source_file, destination_file)
    # goal.json
    source_file = '../apps/customization/customization/crm_customization/goal.json'
    destination_file = '../apps/hrms/hrms/hr/doctype/goal/goal.json'
    copy_and_replace(source_file, destination_file)
    # leave_policy_assignment.py
    source_file = '../apps/customization/customization/crm_customization/leave_policy_assignment.py'
    destination_file = '../apps/hrms/hrms/hr/doctype/leave_policy_assignment/leave_policy_assignment.py'
    copy_and_replace(source_file, destination_file)

    os.system('bench build')