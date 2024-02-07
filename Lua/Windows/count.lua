local pathway = (io.popen("cd")):read("*a")
while pathway:sub(#pathway, #pathway) == "\n" do
    do pathway = pathway:sub(1, #pathway - 1) end
end

function fileExists(testFile)
    local test = io.popen('dir "'..testFile..'" /b'):read("*a")
    do return (test ~= "") end
end

local count = 0
function scan(path, tabs)
    local pfile = io.popen('dir "'..path..'" /b')
    local newTabs = "   "..tabs
    for filename in pfile:lines() do
        local newPath = path.."\\"..filename
        if fileExists(newPath) then
            do count = count + 1 end
        end
    end
    do pfile:close() end
end

do scan(pathway, "") end
print(count)
io.read()