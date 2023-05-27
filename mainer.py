import subprocess


lua_script_path = 'main.lua'


lua_process = subprocess.Popen(['lua', lua_script_path],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)


lua_pid = lua_process.pid


try:

    message = b"Hello from Python!"
    lua_process.stdin.write(message)
    lua_process.stdin.close()


    response = lua_process.stdout.read()
    lua_process.stdout.close()

    error = lua_process.stderr.read()
    lua_process.stderr.close()


    lua_process.wait()

    # Print the response and error
    print("Response from Lua process:")
    print(response.decode())
    print("Error from Lua process:")
    print(error.decode())

except Exception as e:

    print("An error occurred:", str(e))



