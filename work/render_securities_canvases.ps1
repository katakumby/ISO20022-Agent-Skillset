$ErrorActionPreference='Stop'
$rootPath=(Get-Location).Path
$word=$null
try {
 $word=New-Object -ComObject Word.Application
 $word.Visible=$false
 $word.AutomationSecurity=3
 $word.Options.UpdateLinksAtOpen=$false
 $word.DisplayAlerts=0
 foreach($n in 1,2) {
  $file=Join-Path $rootPath ('work/documents/src-000374/native-canvases/canvas-'+$n+'.docx')
  $pdf=Join-Path $rootPath ('work/documents/src-000374/native-canvases/canvas-'+$n+'.pdf')
  $doc=$word.Documents.Open($file,$false,$true,$false)
  try {$doc.ExportAsFixedFormat($pdf,17,$false)} finally {$doc.Close(0)}
 }
} finally {if($word){$word.Quit(0)}}
