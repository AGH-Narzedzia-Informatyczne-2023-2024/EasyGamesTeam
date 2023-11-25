state = {"points": 0, "username": "user"}

while 1:
    command = str(input())
    commandArgs = command.split(" ")

    match commandArgs[0].lower():
        case "quit":
            break
        case "set_username":
            if len(commandArgs) < 2:
                print("//DEV: ERROR: no arguments provided")
                continue

            value = " ".join(commandArgs[1::])
            state["username"] = value
            print("//DEV: SET USERNAME ACTION DONE, COMMAND RUN WITH ARGS: ", commandArgs[1::])
            print("new 'username' value: ", state["username"])

        case "start_game":
            print("//DEV: START GAME ACTION DONE, COMMAND RUN WITH ARGS: ", commandArgs[1::])

        case "stop_game":
            print("//DEV: END GAME ACTION DONE, COMMAND RUN WITH ARGS: ", commandArgs[1::])

        case "points":
            if len(commandArgs) < 3:
                print("//DEV: ERROR: no arguments provided")
                continue

            value = int(commandArgs[2])
            match commandArgs[1].lower():
                case "set":
                    state["points"] = value

                case "add":
                    state["points"] += value

                case "remove":
                    state["points"] -= value

            print("//DEV: POINTS ACTION DONE, COMMAND RUN WITH ARGS: ", commandArgs[1::])
            print("new 'points' value: ", state["points"])
