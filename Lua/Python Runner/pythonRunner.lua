if arg[1] ~= nil then
    do os.execute("cls") end
    do os.execute("C:\\Windows\\py.exe".." "..arg[1]) end
else
    ::a::
    do test = io.read() end
    do os.execute("cls") end
    --do print(test) end
    do os.execute("C:\\Windows\\py.exe".." "..test) end
    do goto a end
end