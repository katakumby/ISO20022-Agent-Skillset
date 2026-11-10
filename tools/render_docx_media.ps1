param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot),
    [string[]]$SourceId = @()
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$repoRoot = (Resolve-Path -LiteralPath $Root).Path
$sourceCatalog = Get-Content -LiteralPath (Join-Path $repoRoot 'catalog/sources.json') -Raw | ConvertFrom-Json
$results = @()
foreach ($source in $sourceCatalog.sources) {
    if ($source.format -ne 'docx') { continue }
    if ($SourceId.Count -gt 0 -and $source.source_id -notin $SourceId) { continue }
    $recordsFile = Join-Path $repoRoot ('work/documents/' + $source.source_id + '/records.json')
    if (-not (Test-Path -LiteralPath $recordsFile)) { continue }
    $records = Get-Content -LiteralPath $recordsFile -Raw | ConvertFrom-Json
    $sourceResults = @()
    foreach ($media in $records.media) {
        $original = Join-Path $repoRoot $media.path
        $extension = [IO.Path]::GetExtension($original).ToLowerInvariant()
        $entry = [ordered]@{ source_id=$source.source_id; original=$media.path; original_sha256=$media.sha256; preview=$media.path; renderer='original raster'; render_status='not-required'; visual_review='not-run'; error=$null }
        if ($extension -in @('.emf','.wmf')) {
            $outDir = Join-Path (Split-Path -Parent (Split-Path -Parent $original)) 'derived-previews'
            $outPath = Join-Path $outDir ([IO.Path]::GetFileName($original)+'.png')
            if (-not $outPath.StartsWith($repoRoot+[IO.Path]::DirectorySeparatorChar)) { throw 'Preview destination outside repository' }
            $entry.preview = $outPath.Substring($repoRoot.Length+1).Replace('\','/')
            $entry.renderer = 'Windows System.Drawing GDI+ metafile rasterization'
            if (-not (Test-Path -LiteralPath $outPath)) {
                $image = $null; $bitmap = $null; $graphics = $null
                try {
                    $actualHash = (Get-FileHash -LiteralPath $original -Algorithm SHA256).Hash.ToLowerInvariant()
                    if ($actualHash -ne $media.sha256) { throw 'Extracted original hash differs from extraction inventory' }
                    $image = [System.Drawing.Image]::FromFile($original)
                    $scale = [Math]::Min(2.0,[Math]::Min(3200.0/[Math]::Max(1,$image.Width),4000.0/[Math]::Max(1,$image.Height)))
                    $width = [Math]::Max(1,[int][Math]::Ceiling($image.Width*$scale))
                    $height = [Math]::Max(1,[int][Math]::Ceiling($image.Height*$scale))
                    $bitmap = [System.Drawing.Bitmap]::new($width,$height)
                    $bitmap.SetResolution(192,192)
                    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
                    $graphics.Clear([System.Drawing.Color]::White)
                    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
                    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
                    $graphics.DrawImage($image,[System.Drawing.Rectangle]::new(0,0,$width,$height))
                    [IO.Directory]::CreateDirectory($outDir) | Out-Null
                    $bitmap.Save($outPath,[System.Drawing.Imaging.ImageFormat]::Png)
                    $entry.render_status='pass';$entry.width=$width;$entry.height=$height
                } catch { $entry.render_status='fail';$entry.error=$_.Exception.Message }
                finally { if($graphics){$graphics.Dispose()};if($bitmap){$bitmap.Dispose()};if($image){$image.Dispose()} }
            } else { $entry.render_status='pass-existing-preview' }
        } elseif ($extension -notin @('.png','.jpg','.jpeg','.gif','.bmp','.tif','.tiff')) {
            $entry.render_status='unsupported-preview-format';$entry.error='The original is retained; a separate renderer is required.'
        }
        $sourceResults += [PSCustomObject]$entry
    }
    $record = [ordered]@{ source_id=$source.source_id; media=$sourceResults; date='2026-11-08'; visual_review='not-run'; limitations=@('Rasterization is a derived preview and is not proof that composite Word drawings are complete.','All source drawing groups and embedded objects still require full-document rendering where separate objects supply labels or relationships.','Contact sheets support triage only; detailed diagram comparison must be recorded separately.') }
    $outputFile = Join-Path $repoRoot ('work/documents/'+$source.source_id+'/media-previews.json')
    $record | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $outputFile -Encoding utf8
    $results += [PSCustomObject]@{source_id=$source.source_id;media=$sourceResults.Count;vector_renders=($sourceResults | Where-Object renderer -Like 'Windows*').Count;failures=($sourceResults | Where-Object render_status -In @('fail','unsupported-preview-format')).Count}
    $results[-1] | ConvertTo-Json -Compress | Write-Output
}
$results | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $repoRoot 'work/documents/media-preview-summary.json') -Encoding utf8
