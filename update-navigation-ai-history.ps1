# PowerShell script to add AI History link to navigation across all pages
# Author: TechVernia Team
# Date: 2025

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Adding AI History to Navigation Menu  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Set base directory
$baseDir = "C:\Users\Freddy\Desktop\techvernia.com\techvernia.com"
Set-Location $baseDir

# Counter for tracking updates
$filesUpdated = 0
$filesSkipped = 0
$errors = 0

# Get all HTML files in pages directory and subdirectories
$htmlFiles = Get-ChildItem -Path "pages" -Filter "*.html" -Recurse -File

Write-Host "Found $($htmlFiles.Count) HTML files to process..." -ForegroundColor Yellow
Write-Host ""

foreach ($file in $htmlFiles) {
    try {
        $content = Get-Content $file.FullName -Raw -Encoding UTF8

        # Check if AI History link already exists
        if ($content -match 'ai-history\.html') {
            Write-Host "  [SKIP] $($file.Name) - AI History link already exists" -ForegroundColor Gray
            $filesSkipped++
            continue
        }

        # Pattern to find: Compare link followed by Blog link
        # We'll insert AI History between them
        $pattern = '(<li class="nav-item">\s*<a class="nav-link"[^>]*href="[^"]*comparisons\.html"[^>]*>.*?</a>\s*</li>\s*)(<li class="nav-item">\s*<a class="nav-link"[^>]*href="[^"]*blog\.html")'

        # Replacement: Compare link + AI History link + Blog link
        $replacement = '$1<li class="nav-item">' + "`n" +
                      '<a class="nav-link" data-i18n="nav.ai-history" href="ai-history.html"><span data-i18n="nav.ai-history">AI History</span></a>' + "`n" +
                      '</li>' + "`n" +
                      '$2'

        # Check file location depth to adjust href path
        $relativePath = $file.DirectoryName.Replace($baseDir, "").TrimStart('\')
        $depth = ($relativePath -split '\\').Count - 1  # -1 because pages is already depth 1

        if ($depth -gt 0) {
            # Files in subdirectories need ../ prefix
            $hrefPath = "../" * $depth + "ai-history.html"
        } else {
            # Files directly in pages folder
            $hrefPath = "ai-history.html"
        }

        # Update replacement with correct path
        $replacement = '$1<li class="nav-item">' + "`n" +
                      '<a class="nav-link" data-i18n="nav.ai-history" href="' + $hrefPath + '"><span data-i18n="nav.ai-history">AI History</span></a>' + "`n" +
                      '</li>' + "`n" +
                      '$2'

        # Perform replacement
        $newContent = $content -replace $pattern, $replacement

        # Check if replacement was made
        if ($newContent -ne $content) {
            # Save updated content
            Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
            Write-Host "  [OK] $($file.Name) - AI History link added" -ForegroundColor Green
            $filesUpdated++
        } else {
            Write-Host "  [SKIP] $($file.Name) - Pattern not found" -ForegroundColor Yellow
            $filesSkipped++
        }

    } catch {
        Write-Host "  [ERROR] $($file.Name) - $($_.Exception.Message)" -ForegroundColor Red
        $errors++
    }
}

# Summary
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "           Update Summary               " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Files updated:  $filesUpdated" -ForegroundColor Green
Write-Host "Files skipped:  $filesSkipped" -ForegroundColor Yellow
Write-Host "Errors:         $errors" -ForegroundColor Red
Write-Host ""

if ($filesUpdated -gt 0) {
    Write-Host "[SUCCESS] AI History navigation link has been added to $filesUpdated pages!" -ForegroundColor Green
} else {
    Write-Host "[WARNING] No files were updated. Check if the navigation structure matches the expected pattern." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Script completed!" -ForegroundColor Cyan
