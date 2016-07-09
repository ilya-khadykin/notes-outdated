# configuration
$file_path="C:\Windows\System32\cmd.exe"
$arguments="/K cd $code_path & dir"

$i=1
DO
{
  "Starting process $i"
  $i++
  Start-Process -FilePath $file_path -ArgumentList $arguments
} While ($i -le 1)