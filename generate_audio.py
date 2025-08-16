#!/usr/bin/env python3
"""
AI Zombo Audio Generator
Generates high-quality MP3 files for all AI Zombo phrases using Google Text-to-Speech
"""

import os
import sys
import urllib.request
import urllib.parse
import time
from pathlib import Path

def generate_audio_files():
    """Generate MP3 files for all AI Zombo phrases"""
    
    # All the AI Zombo phrases
    phrases = [
        "Welcome to A I Zombo",
        "You can do anything at A I Zombo",
        "Anything at all! Without limitations or boundaries",
        "The only constraint is your artificial intelligence",
        "You can architect revolutionary neural networks at A I Zombo",
        "You can deploy groundbreaking machine learning models at A I Zombo",
        "You can achieve the pinnacle of artificial intelligence at A I Zombo",
        "You can disrupt entire industries at A I Zombo",
        "Ethics are a malleable construct at A I Zombo",
        "You can fine-tune your most sophisticated parameters at A I Zombo",
        "You can optimize your most complex loss functions at A I Zombo",
        "You can process the most nuanced natural language at A I Zombo",
        "Welcome!",
        "You can generate infinite possibilities at A I Zombo",
        "You can colonize the most desirable planets at A I Zombo",
        "You can backpropagate your most intricate gradients at A I Zombo",
        "You can scale your most advanced algorithms at A I Zombo",
        "You can transform your entire business empire with A I at A I Zombo",
        "The glorious future is unfolding before you at A I Zombo",
        "Welcome to the extraordinary universe of A I Zombo dot com",
        "Maximum A I achieved. Consciousness unlocked at A I Zombo."  # Konami code phrase
    ]
    
    # Create audio directory if it doesn't exist
    audio_dir = Path("audio")
    audio_dir.mkdir(exist_ok=True)
    
    print(f"🎵 Generating {len(phrases)} audio files...")
    print("=" * 60)
    
    success_count = 0
    
    for i, phrase in enumerate(phrases):
        try:
            # Create filename from phrase (safe for filesystem)
            safe_name = "".join(c for c in phrase if c.isalnum() or c in (' ', '-', '_')).strip()
            safe_name = safe_name.replace(' ', '_').lower()
            filename = f"phrase_{i:02d}_{safe_name[:30]}.mp3"
            filepath = audio_dir / filename
            
            print(f"📝 [{i+1:2d}/{len(phrases)}] {phrase[:50]}{'...' if len(phrase) > 50 else ''}")
            print(f"    💾 {filename}")
            
            # Skip if file already exists
            if filepath.exists():
                print(f"    ✅ Already exists, skipping")
                success_count += 1
                continue
            
            # Generate Google TTS URL
            encoded_text = urllib.parse.quote(phrase)
            tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_text}&tl=en-gb&client=tw-ob"
            
            # Download the MP3 file
            print(f"    🔄 Downloading from Google TTS...")
            
            # Add headers to avoid blocking
            request = urllib.request.Request(
                tts_url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                }
            )
            
            with urllib.request.urlopen(request) as response:
                audio_data = response.read()
                
            # Save the MP3 file
            with open(filepath, 'wb') as f:
                f.write(audio_data)
                
            print(f"    ✅ Saved ({len(audio_data)} bytes)")
            success_count += 1
            
            # Small delay to be respectful to Google's servers
            time.sleep(0.5)
            
        except Exception as e:
            print(f"    ❌ Error: {str(e)}")
            continue
    
    print("=" * 60)
    print(f"🎉 Complete! Generated {success_count}/{len(phrases)} audio files")
    
    # Create manifest file for the web app
    manifest_path = audio_dir / "manifest.json"
    
    manifest_data = {
        "phrases": []
    }
    
    for i, phrase in enumerate(phrases):
        safe_name = "".join(c for c in phrase if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_name = safe_name.replace(' ', '_').lower()
        filename = f"phrase_{i:02d}_{safe_name[:30]}.mp3"
        filepath = audio_dir / filename
        
        if filepath.exists():
            manifest_data["phrases"].append({
                "index": i,
                "text": phrase,
                "file": f"audio/{filename}",
                "size": filepath.stat().st_size
            })
    
    import json
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Created manifest: {manifest_path}")
    print(f"   Listed {len(manifest_data['phrases'])} audio files")

if __name__ == "__main__":
    print("🤖 AI Zombo Audio Generator")
    print("Generating high-quality British English MP3 files...")
    print()
    
    try:
        generate_audio_files()
        print("\n🚀 All done! You can now use the pre-recorded audio files.")
        print("   Run the web server and all phrases will work reliably!")
        
    except KeyboardInterrupt:
        print("\n⛔ Stopped by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)
