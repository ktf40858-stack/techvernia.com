#!/bin/bash
# Script to check translation progress

echo "════════════════════════════════════════════════════════════"
echo "   🌍 TRANSLATION PROGRESS MONITOR"
echo "════════════════════════════════════════════════════════════"
echo ""

# Check if process is running
PID=$(cat translator_pid.txt 2>/dev/null)
if [ -n "$PID" ] && kill -0 $PID 2>/dev/null; then
    echo "✅ Translation process is RUNNING (PID: $PID)"
else
    echo "❌ Translation process is NOT running"
fi

echo ""
echo "────────────────────────────────────────────────────────────"
echo "📊 PROGRESS FILES"
echo "────────────────────────────────────────────────────────────"
ls -lh real_translation* 2>/dev/null | tail -15

echo ""
echo "────────────────────────────────────────────────────────────"
echo "📝 LATEST LOG OUTPUT (last 30 lines)"
echo "────────────────────────────────────────────────────────────"
tail -30 real_translation.log

echo ""
echo "────────────────────────────────────────────────────────────"
echo "💾 CACHE & PROGRESS STATUS"
echo "────────────────────────────────────────────────────────────"

if [ -f "real_translation_cache.json" ]; then
    CACHE_SIZE=$(wc -c < real_translation_cache.json)
    echo "Cache file: $(numfmt --to=iec-i --suffix=B $CACHE_SIZE)"
fi

if [ -f "real_translation_progress.json" ]; then
    COMPLETED=$(jq '.completed_keys | length' real_translation_progress.json 2>/dev/null || echo "0")
    echo "Keys completed: $COMPLETED / 18425 ($(echo "scale=2; $COMPLETED * 100 / 18425" | bc)%)"
fi

echo ""
echo "────────────────────────────────────────────────────────────"
echo "🔄 Commands:"
echo "   Monitor live:  tail -f real_translation.log"
echo "   Stop process:  kill $PID"
echo "   Resume later:  python3 real_translator_auto.py"
echo "════════════════════════════════════════════════════════════"
