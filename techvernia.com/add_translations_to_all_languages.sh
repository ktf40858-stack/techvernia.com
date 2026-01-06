#!/bin/bash
# Add missing translations to all languages in i18n.js

cd "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

# Backup first
cp js/i18n.js js/i18n.js.backup_$(date +%Y%m%d_%H%M%S)

# Use sed to add translations after filter.enterprise for Spanish
sed -i '/"filter.enterprise": "Empresarial"/a\        ,\n\n        // Additional translations for full site coverage\n        "stats.avgRating": "Calificación Promedio",\n        "country.us": "Estados Unidos"' js/i18n.js

# For German
sed -i '/"filter.enterprise": "Unternehmen"/a\        ,\n\n        // Additional translations for full site coverage\n        "stats.avgRating": "Durchschnittsbewertung",\n        "country.us": "Vereinigte Staaten"' js/i18n.js

# For Portuguese
sed -i '/pt:.*"filter.enterprise": "Empresarial"/a\        ,\n\n        // Additional translations for full site coverage\n        "stats.avgRating": "Classificação Média",\n        "country.us": "Estados Unidos"' js/i18n.js

echo "✅ Translations added to all languages!"
echo "📝 Backup saved as: js/i18n.js.backup_*"
