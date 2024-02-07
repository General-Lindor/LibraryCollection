--local pathway = (io.popen("cd")):read("*a")

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
    --local test = (io.popen('dir "'..testFile..'" /b'):read("*a") ~= "")
    local test = toboolean(string.gsub(io.popen("IF exist \""..testFile.."\" ( echo true ) ELSE ( echo false)"):read("*a"), "\n", ""))
    do return test end
end

function collapseOneDown(path)
    local i = #path
    while path:sub(i, i) ~= "/" and path:sub(i, i) ~= "\\" do
        do i = i - 1 end
        if i == 1 then
            do return path end
        end
    end
    local j = i - 1
    while path:sub(j, j) ~= "/" and path:sub(j, j) ~= "\\" do
        do j = j - 1 end
        if j == 1 then
            do return path end
        end
    end
    local result = path:sub(1, j)..path:sub(i, #path)
    do return result end
end

function renameFile(oldName, newName)
    if fileExists(newName) then
        local i = 2
        local newNewName = newName.."("..tostring(i)..")"
        while fileExists(newNewName) do
            do i = i + 1 end
            do newNewName = newName.."("..tostring(i)..")" end
        end
        do os.rename(oldName, newNewName) end
    else
        do os.rename(oldName, newName) end
    end
end

function collapseRecursive(path)
    local files = io.popen('dir "'..path..'" /b')
    for filename in files:lines() do
        local filePath = path.."\\"..filename
        --do print("checking whether \""..filePath.."\" exists") end
        if fileExists(filePath) then
            do collapseRecursive(filePath) end
        end
    end
    do files:close() end
    do files = io.popen('dir "'..path..'" /b') end
    for filename in files:lines() do
        local filePath = path.."\\"..filename
        --do print("checking whether \""..filePath.."\" exists") end
        if fileExists(filePath) then
            do print("collapsing \""..filePath.."\"") end
            do renameFile(filePath, collapseOneDown(filePath)) end
        end
    end
    do files:close() end
end

::a::
local pathway = io.read()
do pathway = string.gsub(pathway, "\n", "") end
do pathway = string.gsub(pathway, "\"", "") end
do collapseRecursive(pathway) end
do print("Finished. Choose another pathway or end the program.") end
do goto a end