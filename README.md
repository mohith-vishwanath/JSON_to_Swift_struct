# Convert any JSON response to Swift struct

Many times while deadling with APIs that return JSON objects in Swift, we need to create structs in Swift to be able to use JSONDecoder. If the JSON object is very big, it takes a lot of time to create a struct (or many nested structs) with the exact names and data types. \n

This Python Script takes in a JSON response (either from an API or from a saved file) and creates the struct definitions from it. 

### Example

![Screenshot 2021-07-27 at 10 21 31 PM](https://user-images.githubusercontent.com/47850206/127204538-6469378d-0f45-4800-9405-bb9569309834.png)

The above screenshot shows a typical Weather API response. 

![Screenshot 2021-07-27 at 11 32 56 PM](https://user-images.githubusercontent.com/47850206/127204983-97ba7bad-58fb-44c7-b0cb-372d15b1414c.png)
![Screenshot 2021-07-27 at 11 33 06 PM](https://user-images.githubusercontent.com/47850206/127204990-7d12d7ff-bcea-4f35-8d4f-0314c15aba2f.png)

The above screenshot shows the Structs created by the script using the API response
