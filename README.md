# Arithmetic api

A server with an api endpoint that takes a json with integers x and y and an operation:
{ “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
Performs a a simple arithmetic then returns the result:
{“result”: Integer, “operation_type”: Enum.value }
Hosted https://stage2hngi.herokuapp.com/post

