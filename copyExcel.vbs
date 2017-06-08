yyyymm=Left(DateAdd("m",-1,Now()),7)
yyyymm=Replace(yyyymm, "/", "")
filename="anesinvoice" & yyyymm & ".xlsm"
str_macro = "makeinvoice"
set objWshShell=CreateObject("WScript.Shell")
set objExcel=CreateObject("Excel.Application")
set objFileSystem=CreateObject("Scripting.FileSystemObject")
set objFolder = objFileSystem.GetFolder("./")

'ファイルと解凍する
For Each objFile In objFolder.Files
    If objFileSystem.GetExtensionName(objFile.Name) = "zip" Then
        set RC1=objWshShell.Exec("powershell expand-archive ./" & objFile.Name)
        WScript.Sleep 4000
        objFileSystem.MoveFolder objWshShell.CurrentDirectory & "\" & objFileSystem.getBaseName(objFile.Name) & "\zzzzzzzzz" , objWshShell.CurrentDirectory & "\"
        objFileSystem.DeleteFolder objWshShell.CurrentDirectory & "\" & objFileSystem.getBaseName(objFile.Name),True
        objFileSystem.DeleteFile objWshShell.CurrentDirectory & "\" & objFile.Name,True
    end If
Next


set RC1=objWshShell.Exec("python convertyyyyyy.py")

objFileSystem.CopyFile "anesinvoicesample.xlsm",filename
set objFile = objFileSystem.GetFile(objWshShell.CurrentDirectory & "\" & filename)
objFile.Attributes = 0
'  Exlceの起動
Set objWbk = objExcel.Workbooks.Open(objWshShell.CurrentDirectory & "\" & filename  , False, True)
' Excelウィンドウを表示
objExcel.Visible = True ' Trueは表示