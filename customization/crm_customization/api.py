import frappe

@frappe.whitelist()
def create_task(description,parent,allocated_to,date,template,reference_name,reference_type):

    print(reference_name)
    print(reference_type)
    doc = frappe.get_doc(dict(
        doctype = 'ToDo',
        description = description,
        parent_dict = parent,
        allocated_to = allocated_to,
        date = date,
        template = template,
        reference_type= reference_type,
        reference_name= reference_name
    )).insert()
    
    print(doc)
    return doc
    
    
    
   