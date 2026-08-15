from functions import Function


function = Function()

while True:
    function.display_contents()

    if function.path == "home":
        prompt = "Choose the Item's Number you want to select (or 0 to exit): "
    else:
        prompt = "Choose the Item's Number you want to select: "

    try:
        choice = int(input(prompt))
    except ValueError:
        print("Enter a Valid Response")
        continue

    if function.path == "home" and choice == 0:
        print("Exiting File Management System...")
        break

    function.function(choice)
