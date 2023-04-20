import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_dict = json.loads(sampleJson)


salary = json_dict["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)


json_dict["company"]["employee"]["birth_date"] = "1990-01-01"


with open("output.json", "w") as outfile:
    json.dump(json_dict, outfile)
