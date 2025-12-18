import requests
from pathlib import Path
import time

logos_dir = Path("assets/images/logos")

# URLs pour le vrai logo DeepSeek
urls = [
    'https://chat.deepseek.com/favicon.ico',
    'https://www.deepseek.com/static/images/logo.png',
    'https://avatars.githubusercontent.com/u/156286804',
    'https://raw.githubusercontent.com/deepseek-ai/DeepSeek-V2/main/figures/logo.svg',
]

print("🔍 Recherche du vrai logo DeepSeek...\n")

for i, url in enumerate(urls):
    try:
        print(f"Tentative {i+1}: {url}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'image/*, */*'
        }
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            size = len(response.content)
            
            print(f"   Status: {response.status_code}")
            print(f"   Type: {content_type}")
            print(f"   Taille: {size} bytes")
            
            if size > 500:
                # Déterminer l'extension
                if 'svg' in content_type or url.endswith('.svg'):
                    ext = '.svg'
                elif 'png' in content_type or url.endswith('.png'):
                    ext = '.png'
                elif url.endswith('.ico'):
                    ext = '.ico'
                else:
                    ext = '.png'
                
                # Sauvegarder
                filepath = logos_dir / f"deepseek{ext}"
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                print(f"   ✅ Sauvegardé: {filepath.name}\n")
                break
        else:
            print(f"   ❌ Échec (status: {response.status_code})\n")
    except Exception as e:
        print(f"   ❌ Erreur: {e}\n")
    
    time.sleep(0.5)

print("✨ Terminé!")

