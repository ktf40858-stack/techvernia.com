import requests
from pathlib import Path

logos_dir = Path("assets/images/logos")

# URLs directes pour le logo DeepSeek
urls = [
    # SeekLogo - PNG direct
    'https://seeklogo.com/images/D/deepseek-ai-logo-9DC0A19C8D-seeklogo.com.png',
    # Alternative
    'https://cdn.jsdelivr.net/gh/lobehub/lobe-icons@latest/packages/static/png/deepseek.png',
]

print("📥 Téléchargement du vrai logo DeepSeek...\n")

for url in urls:
    try:
        print(f"Essai: {url}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        
        if response.status_code == 200:
            # Vérifier si c'est vraiment une image
            content_type = response.headers.get('content-type', '')
            
            if 'image' in content_type or len(response.content) > 1000:
                # Sauvegarder
                with open(logos_dir / "deepseek.png", 'wb') as f:
                    f.write(response.content)
                
                print(f"✅ Logo téléchargé: {len(response.content)} bytes")
                print(f"   Type: {content_type}")
                
                # Vérifier le fichier
                import subprocess
                result = subprocess.run(['file', str(logos_dir / "deepseek.png")], 
                                      capture_output=True, text=True)
                print(f"   Vérifié: {result.stdout.split(':')[1].strip()}")
                
                if 'PNG' in result.stdout or 'image' in result.stdout:
                    print("\n✨ Logo DeepSeek officiel téléchargé avec succès!")
                    break
                else:
                    print("   ⚠️  Pas une vraie image, essai suivant...")
            else:
                print(f"   ❌ Pas une image (type: {content_type})")
        else:
            print(f"   ❌ Erreur {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Erreur: {e}")

