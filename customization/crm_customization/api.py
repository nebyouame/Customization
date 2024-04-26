import frappe

@frappe.whitelist()
def create_task(description,parent,allocated_to,date,reference_name,reference_type):

    print(reference_name)
    print(reference_type)
    doc = frappe.get_doc(dict(
        doctype = 'ToDo',
        description = description,
        parent_dict = parent,
        allocated_to = allocated_to,
        date = date,
        reference_type= reference_type,
        reference_name= reference_name
    )).insert()
    
    print(doc)
    return doc

    # doc = frappe.new_doc(ToDo)
    # doc.description = description
    # doc.parent_link = parent
    # doc.allocated_to = allocated_to
    # doc.date = date
    # doc.insert()

    return "data inserted into Todo"
    
    
   