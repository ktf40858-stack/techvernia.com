import requests
from pathlib import Path

logos_dir = Path("assets/images/logos")

# URLs alternatives pour DeepSeek
urls = [
    'https://logo.clearbit.com/deepseek.com',
    'https://avatars.githubusercontent.com/u/165788083',
    'https://deepseek.com/favicon.ico',
]

for i, url in enumerate(urls):
    try:
        print(f"Tentative {i+1}: {url}...")
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200 and len(response.content) > 500:
            # Sauvegarder
            with open(logos_dir / "deepseek.png", 'wb') as f:
                f.write(response.content)
            print(f"✅ Logo DeepSeek téléchargé ({len(response.content)} bytes)")
            break
        else:
            print(f"❌ Échec (status: {response.status_code}, size: {len(response.content)})")
    except Exception as e:
        print(f"❌ Erreur: {e}")

