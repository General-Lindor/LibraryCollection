local pathway = (io.popen("cd")):read("*a")
while pathway:sub(#pathway, #pathway) == "\n" do
    do pathway = pathway:sub(1, #pathway - 1) end
end
local file = io.open("scan.txt", "w")

function fileExists(testFile)
    local test = io.popen('dir "'..testFile..'" /b'):read("*a")
    do return (test ~= "") end
end

function scan(path, tabs)
    local pfile = io.popen('dir "'..path..'" /b')
    local newTabs = "   "..tabs
    for filename in pfile:lines() do
        local newPath = path.."\\"..filename
        if fileExists(newPath) then
            do file:write(tabs..filename, "\n") end
            do scan(newPath, newTabs) end
        end
    end
    do pfile:close() end
end

do scan(pathway, "") end
do file:close() end