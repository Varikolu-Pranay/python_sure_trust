class Mobile:
    def __init__(self,company,processor,camera,display,OS,display_size,benchmark_score):
        self.comapny=company
        self.processor=processor
        self.camera=camera
        self.display=display
        self.OS=OS
        self.display_size=display_size
        self.benchmark_score=benchmark_score
    
IQOO=Mobile("IQOO","snapdragon","50 MP","superamoled","Funtouch OS",15.40,550719)


print(IQOO.comapny)
print(IQOO.display)
print(IQOO.display_size)
print(IQOO.processor)
print(IQOO.camera)
print(IQOO.OS)
print(IQOO.benchmark_score)
