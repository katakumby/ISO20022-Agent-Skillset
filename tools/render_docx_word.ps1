param(
 [string]$Root = (Split-Path $PSScriptRoot -Parent),
 [Parameter(Mandatory=$true)][string]$SourceId
)
$ErrorActionPreference = 'Stop'
$rootPath = (Resolve-Path -LiteralPath $Root).Path
if ($SourceId -notmatch '^src-\d{6}$') { throw 'Invalid registered source identifier.' }
$catalog = Get-Content -Raw -LiteralPath (Join-Path $rootPath 'catalog/sources.json') | ConvertFrom-Json
$source = @($catalog.sources | Where-Object source_id -EQ $SourceId)
if ($source.Count -ne 1 -or $source[0].format -ne 'docx') { throw 'Source must be one registered DOCX.' }
$source = $source[0]
$occurrence = $source.occurrences[0]
$outputDir = [System.IO.Path]::GetFullPath((Join-Path $rootPath ('work/docx-render/' + $SourceId)))
if (-not $outputDir.StartsWith($rootPath + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Output escapes repository.' }
[System.IO.Directory]::CreateDirectory($outputDir) | Out-Null
$originalPath = Join-Path $rootPath $occurrence.path
$originalHash = (Get-FileHash -LiteralPath $originalPath -Algorithm SHA256).Hash.ToLowerInvariant()
$inputPath = $originalPath
if ($occurrence.archive_member) {
 Add-Type -AssemblyName System.IO.Compression.FileSystem
 $archive = [System.IO.Compression.ZipFile]::OpenRead($originalPath)
 try {
  $entry = $archive.GetEntry($occurrence.archive_member)
  if (-not $entry) { throw 'Registered archive member missing.' }
  $inputPath = Join-Path $outputDir 'source.docx'
  $stream = $entry.Open(); $target = [System.IO.File]::Create($inputPath)
  try { $stream.CopyTo($target) } finally { $target.Dispose(); $stream.Dispose() }
 } finally { $archive.Dispose() }
}
$inputHash = (Get-FileHash -LiteralPath $inputPath -Algorithm SHA256).Hash.ToLowerInvariant()
if ($inputHash -ne $source.sha256) { throw 'Input differs from registered source checksum.' }
$pdfPath = Join-Path $outputDir 'document.pdf'
$word = $null; $document = $null; $oldSecurity = $null; $oldUpdateLinks = $null
$report = [ordered]@{source_id=$SourceId; source_sha256=$inputHash; original_path=$occurrence.path; archive_member=$occurrence.archive_member; started=(Get-Date).ToString('o'); read_only=$true; macros_disabled=$true; update_links=$false; result='failed'}
try {
 $word = New-Object -ComObject Word.Application
 $word.Visible = $false
 $oldSecurity = $word.AutomationSecurity; $word.AutomationSecurity = 3
 $oldUpdateLinks = $word.Options.UpdateLinksAtOpen; $word.Options.UpdateLinksAtOpen = $false
 $word.DisplayAlerts = 0
 $missing = [System.Type]::Missing
 $document = $word.Documents.Open($inputPath,$false,$true,$false,$missing,$missing,$false,$missing,$missing,$missing,$missing,$false)
 $report.word_version = $word.Version
 $report.word_build = $word.Build
 $document.ExportAsFixedFormat($pdfPath,17,$false)
 $report.pages = $document.ComputeStatistics(2)
 $report.paragraphs = $document.Paragraphs.Count
 $report.tables = $document.Tables.Count
 $report.inline_shapes = $document.InlineShapes.Count
 $report.floating_shapes = $document.Shapes.Count
 $locations = [System.Collections.Generic.List[object]]::new()
 $shaProvider = [System.Security.Cryptography.SHA256]::Create()
 try {
  for ($i = 1; $i -le $document.InlineShapes.Count; $i++) {
   $shape = $document.InlineShapes.Item($i); $range = $shape.Range
   $startRange = $range.Duplicate; $startRange.Collapse(1)
   $endRange = $range.Duplicate; $endRange.Collapse(0)
   $shapeRecord = [ordered]@{kind='inline-shape';ordinal=$i;range_start=$range.Start;range_end=$range.End;start_file_page=$startRange.Information(3);end_file_page=$endRange.Information(3);start_printed_page=$startRange.Information(1);width_points=$shape.Width;height_points=$shape.Height;shape_type=$shape.Type;asset_fingerprints=@()}
   try {
    [xml]$flatXml = $range.WordOpenXML
    $fingerprints = [System.Collections.Generic.List[object]]::new()
    foreach ($part in $flatXml.SelectNodes("/*[local-name()='package']/*[local-name()='part']")) {
     $data = $part.SelectSingleNode("*[local-name()='binaryData']")
     if ($data) {
      $bytes = [Convert]::FromBase64String($data.InnerText)
      $hash = [BitConverter]::ToString($shaProvider.ComputeHash($bytes)).Replace('-','').ToLowerInvariant()
      $fingerprints.Add([ordered]@{package_part=$part.GetAttribute('name','http://schemas.microsoft.com/office/2006/xmlPackage');sha256=$hash;size_bytes=$bytes.Length})
     }
    }
    $shapeRecord.asset_fingerprints = @($fingerprints.ToArray())
   } catch { $shapeRecord.fingerprint_limitation = $_.Exception.Message }
   $locations.Add($shapeRecord)
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($startRange) | Out-Null
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($endRange) | Out-Null
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($range) | Out-Null
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($shape) | Out-Null
  }
  for ($i = 1; $i -le $document.Tables.Count; $i++) {
   $table = $document.Tables.Item($i); $range = $table.Range
   $startRange = $range.Duplicate; $startRange.Collapse(1)
   $endRange = $range.Duplicate; $endRange.Collapse(0)
   $locations.Add([ordered]@{kind='table';ordinal=$i;range_start=$range.Start;range_end=$range.End;start_file_page=$startRange.Information(3);end_file_page=$endRange.Information(3);start_printed_page=$startRange.Information(1)})
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($startRange) | Out-Null
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($endRange) | Out-Null
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($range) | Out-Null
   [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($table) | Out-Null
  }
 } finally { $shaProvider.Dispose() }
 [ordered]@{source_id=$SourceId;source_sha256=$inputHash;word_version=$report.word_version;word_build=$report.word_build;pdf='work/docx-render/'+$SourceId+'/document.pdf';locations=@($locations.ToArray());limitations=@('Word-generated pagination is additional to immutable source XML/paragraph locators.','Asset hashes identify unchanged binary parts in the Word range; native hidden-layer equivalence is not established.')} | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $outputDir 'page-locations.json') -Encoding utf8
 $report.location_manifest = 'work/docx-render/' + $SourceId + '/page-locations.json'
 $report.output = 'work/docx-render/' + $SourceId + '/document.pdf'
 $report.output_sha256 = (Get-FileHash -LiteralPath $pdfPath -Algorithm SHA256).Hash.ToLowerInvariant()
 $report.result = 'rendered-needs-visual-review'
} catch {
 $report.error = $_.Exception.Message
 throw
} finally {
 if ($document) { $document.Close(0); [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($document) | Out-Null }
 if ($word) {
  if ($null -ne $oldSecurity) { $word.AutomationSecurity = $oldSecurity }
  if ($null -ne $oldUpdateLinks) { $word.Options.UpdateLinksAtOpen = $oldUpdateLinks }
  $word.Quit(0); [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) | Out-Null
 }
 $report.finished = (Get-Date).ToString('o')
 $afterHash = (Get-FileHash -LiteralPath $originalPath -Algorithm SHA256).Hash.ToLowerInvariant()
 $report.original_unchanged = ($afterHash -eq $originalHash)
 if (-not $report.original_unchanged) { $report.result = 'source-checksum-failed' }
 $report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $outputDir 'render-report.json') -Encoding utf8
 $report | ConvertTo-Json -Depth 8 -Compress
}
