local absPath = arg[0]
do package.path = package.path..";"..absPath end
local luaPath = require("luaPath")
::a::
local filePathLua = io.read()
do filePathLua = string.gsub(filePathLua, "\n", "") end
do filePathLua = string.gsub(filePathLua, "\"", "") end
do filePathLua = string.gsub(filePathLua, "Program Files", "Programme") end
do os.execute("\"\""..luaPath.lua.."\" \""..filePathLua.."\"\"") end
do goto a end