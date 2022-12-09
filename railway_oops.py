class Railway:
    formType="RailwayForm"

    def printDetails(self):
        return f"{self.name},{self.age},{self.train},{self.destination}"

shiva_Application=Railway()
shiva_Application.name="Sonu Ram"
shiva_Application.age=34
shiva_Application.train="Jammutavi"
shiva_Application.destination="Jammu"
print(shiva_Application.printDetails())
