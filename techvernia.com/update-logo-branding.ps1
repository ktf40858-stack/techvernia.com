# Script PowerShell pour remplacer le logo et le branding GenuisNet.ai par TechVernia
# Ce script remplace:
# 1. logo-neon.svg -> logo-techvernia-neon.svg
# 2. GenuisNet.ai -> TechVernia (dans le texte et les attributs)
# 3. genuisnet.ai -> techvernia.com (dans les URLs)

Write-Host "Debut du remplacement du logo et du branding..." -ForegroundColor Green

# Compteurs
$filesProcessed = 0
$totalReplacements = 0

# Trouver tous les fichiers HTML
$htmlFiles = Get-ChildItem -Path "." -Recurse -Filter "*.html"

Write-Host "Nombre de fichiers HTML trouves: $($htmlFiles.Count)" -ForegroundColor Cyan

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    $fileReplacements = 0

    # Remplacement 1: logo-neon.svg -> logo-techvernia-neon.svg
    $content = $content -replace 'logo-neon\.svg', 'logo-techvernia-neon.svg'
    if ($content -ne $originalContent) { $fileReplacements++ }

    # Remplacement 2: "GenuisNet.ai Logo" -> "TechVernia Logo"
    $content = $content -replace 'GenuisNet\.ai Logo', 'TechVernia Logo'

    # Remplacement 3: nav.genuisnetai-logo -> nav.techvernia-logo
    $content = $content -replace 'nav\.genuisnetai-logo', 'nav.techvernia-logo'

    # Remplacement 4: GenuisNet.ai -> TechVernia (dans le texte)
    $content = $content -replace 'GenuisNet\.ai', 'TechVernia'

    # Remplacement 5: genuisnet.ai -> techvernia.com (dans les URLs)
    $content = $content -replace 'https://genuisnet\.ai', 'https://techvernia.com'
    $content = $content -replace 'genuisnet\.ai', 'techvernia.com'

    # Remplacement 6: Why GenuisNet.ai? -> Why TechVernia?
    $content = $content -replace 'Why GenuisNet\.ai\?', 'Why TechVernia?'

    # Si le contenu a change, sauvegarder le fichier
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        $filesProcessed++
        $totalReplacements++
        Write-Host "  Modifie: $($file.FullName)" -ForegroundColor Yellow
    }
}

Write-Host "`nTermine!" -ForegroundColor Green
Write-Host "Fichiers modifies: $filesProcessed" -ForegroundColor Cyan
Write-Host "Total de remplacements: $totalReplacements" -ForegroundColor Cyan
