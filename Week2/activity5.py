class TemperatureCoverter:
    def convertToCelsius(f): #convert f to c
        return (f-32)*5/9
    

    def convertToFarenheit(c): #convert c to f
        return (c*9/5)+32
    

    def validateInput(temp): # String slice [start:end:step] method used for validation to get first char & check rest are number
        if temp[:1] == "F" and float(temp[1:]): #check whether input is Farenheit
            return "F",temp[1:] #return scale name & digit value
        elif temp[:1] == "C" and float(temp[1:]): #check whether input is Celsius
            return "C",temp[1:]
        else:
            return None,None # return None if input is invalid
        

    def main(userInput):
        
        scale,value = TemperatureCoverter.validateInput(userInput) 
        
        if scale == "C":
            convertedFarenheit = round(TemperatureCoverter.convertToFarenheit(float(value)),2) # convert the value and round to 2 decimal places
            print(f"{userInput} degrees Celsius is converted to {convertedFarenheit} degrees Fahrenheit")

        elif scale == "F":
            convertedCelsius = round(TemperatureCoverter.convertToCelsius(float(value)),2)
            print(f"{userInput} degrees Fahrenheit is converted to {convertedCelsius} degrees Celsius")

        else:
            print("Invalid input. Please enter the temperature with the correct 'C' or F' prefix")



if __name__ == "__main__":

    userInput = input("Enter temperature with unit (e.g., F100 for 100 Fahrenheit or C30 for 30 Celsius): ")
    TemperatureCoverter.main(userInput)