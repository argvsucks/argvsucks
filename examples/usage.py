# Usage
from argvsucks import handle_command_line

dct = handle_command_line(["program ···", "start", "end=0", "finish", "n=5", "name=Foo", "lst=a,b,c"], n=int, start=False, end=bool, lst=list)
print(dct)
# ...
