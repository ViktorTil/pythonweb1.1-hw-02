
filename = "data.bin"

format_maps = {
                "phone": "any ukrainian number",
                "email": "any email format",
                "birthday": "any data format in this sequence: dd,mm, yyyy",
                "address": "free",
            }

available_options = {
    "add":
        {
            "contact": True, 
            "phone": True, 
            "email": True, 
            "birthday": True, 
            "address": True, 
            "note": True,
            "tags": True
        },
    "edit":
        {
            "contact": False, 
            "phone": True,  
            "email": True,  
            "birthday": True,  
            "address": True,  
            "note": True, 
            "tags": False
        },
    "delete": 
        {
            "contact": True, 
            "phone": True,  
            "email": True,  
            "birthday": True,  
            "address": True,  
            "note": True, 
            "tags": False
        }
    }
