local absPath = arg[0]
do package.path = package.path..";"..absPath end
local luaPath = require("luaPath")

function toboolean(s)
    --print(s)
    if string.lower(s) == "true" then
        do s = true end
        do return s end
    elseif string.lower(s) == "false" then
        do s = false end
        do return s end
    end
    do return s end
end

function fileExists(testFile)
    --local test = io.popen('dir "'..testFile..'" /b'):read("*a")
    local test = string.gsub(io.popen("IF exist \""..testFile.."\" ( echo true ) ELSE ( echo false)"):read("*a"), "\n", "")
    do return toboolean(test) end
end

function split(s)
	for i = #s, 1, -1 do
		if ((s:sub(i, i) == "/") or (s:sub(i, i) == "\\")) then
			local result = {s:sub(1, i), s:sub(i + 1, #s)}
			do return result end
		end
	end
	local result = {"", s}
	do return result end
end

function main()
	do print("Please insert luapath: ") end
	local filePathLua = io.read()
	do filePathLua = string.gsub(filePathLua, "\n", "") end
	do filePathLua = string.gsub(filePathLua, "\"", "") end
	do filePathLua = string.gsub(filePathLua, "Program Files", "Programme") end
	local filePathExe = string.gsub(filePathLua, "%.lua", ".exe")
	local command = "\"\""..luaPath.srglue.."\" \""..luaPath.srlua.."\" \""..filePathLua.."\" \""..filePathExe.."\"\""
	--print(command)
	do os.execute(command) end
	local fileSplit = split(filePathLua)
	local dllSplit = split(luaPath.dll)
	local dllPath = (fileSplit[1])..(dllSplit[2])
	if not fileExists(dllPath) then
		do os.execute("copy "..luaPath.dll.." "..dllPath) end
	end
	do os.execute("cls") end
	do print("Successfully compiled \""..(fileSplit[2]).."\" into an exe.") end
end

::a::
	do pcall(main) end
do goto a end