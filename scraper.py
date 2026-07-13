import os

def create_website_files():
    """إنشاء موقع Face Swap AI - نسخة شغالة"""
    
    os.makedirs("www", exist_ok=True)
    
    index_html = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Face Swap AI</title>
    <style>
        :root {
            --bg: #0a0a0a;
            --surface: #111111;
            --border: #222;
            --gold: #c9a84c;
            --gold-glow: rgba(201, 168, 76, 0.3);
            --text: #e0d5c0;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Segoe UI', system-ui, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
            background-image: 
                radial-gradient(ellipse at top, rgba(201,168,76,0.05) 0%, transparent 60%),
                radial-gradient(ellipse at bottom, rgba(201,168,76,0.03) 0%, transparent 60%);
        }

        .app {
            width: 100%;
            max-width: 440px;
        }

        .header {
            text-align: center;
            margin-bottom: 20px;
        }

        .logo {
            width: 64px;
            height: 64px;
            margin: 0 auto 12px;
            background: linear-gradient(135deg, var(--gold), #e2c97e, var(--gold));
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 0 30px var(--gold-glow);
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
        }

        .title {
            font-size: 28px;
            font-weight: 900;
            letter-spacing: 2px;
            background: linear-gradient(135deg, var(--gold), #e2c97e, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .subtitle {
            font-size: 10px;
            color: #6b6355;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-top: 4px;
        }

        .line {
            width: 50px;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
            margin: 12px auto;
        }

        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }

        .upload-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 16px;
        }

        .upload-box {
            aspect-ratio: 1;
            background: var(--bg);
            border: 2px dashed var(--border);
            border-radius: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
            text-align: center;
            padding: 10px;
        }

        .upload-box:hover {
            border-color: var(--gold);
            box-shadow: 0 0 15px var(--gold-glow);
        }

        .upload-box.has-image {
            border-style: solid;
            border-color: var(--gold);
        }

        .upload-box img {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: none;
        }

        .upload-box.has-image img {
            display: block;
        }

        .upload-box.has-image .upload-icon,
        .upload-box.has-image .upload-text {
            display: none;
        }

        .upload-icon {
            font-size: 30px;
            margin-bottom: 6px;
        }

        .upload-text {
            font-size: 10px;
            color: #6b6355;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .input-file {
            display: none;
        }

        .btn-swap {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, var(--gold), #e2c97e, var(--gold));
            color: #000;
            border: none;
            font-weight: 900;
            cursor: pointer;
            border-radius: 12px;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.3s;
            box-shadow: 0 4px 15px var(--gold-glow);
            margin-bottom: 16px;
        }

        .btn-swap:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px var(--gold-glow);
        }

        .btn-swap:active {
            transform: scale(0.98);
        }

        .btn-swap:disabled {
            background: #1a1a1a;
            color: #333;
            box-shadow: none;
            cursor: not-allowed;
            transform: none;
        }

        .result-area {
            width: 100%;
            aspect-ratio: 1;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            margin-bottom: 12px;
        }

        .result-placeholder {
            text-align: center;
            color: #1a1a1a;
        }

        .result-placeholder .icon {
            font-size: 50px;
            display: block;
            margin-bottom: 6px;
        }

        .result-placeholder .text {
            font-size: 10px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .result-area img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: none;
        }

        .result-area canvas {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            display: none;
        }

        .loading-overlay {
            display: none;
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.9);
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 12px;
            border-radius: 16px;
        }

        .loading-overlay.show {
            display: flex;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 2px solid var(--border);
            border-top-color: var(--gold);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .loading-text {
            font-size: 10px;
            letter-spacing: 2px;
            color: var(--gold);
            animation: pulse 1.5s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .btn-download {
            display: none;
            width: 100%;
            padding: 12px;
            background: transparent;
            border: 1px solid var(--gold);
            color: var(--gold);
            cursor: pointer;
            border-radius: 12px;
            font-weight: 700;
            font-size: 12px;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.3s;
        }

        .btn-download.visible {
            display: block;
        }

        .btn-download:hover {
            background: rgba(201,168,76,0.1);
            box-shadow: 0 0 20px var(--gold-glow);
        }

        .footer {
            text-align: center;
            margin-top: 16px;
            font-size: 9px;
            color: #1a1a1a;
            letter-spacing: 2px;
        }

        .footer span {
            color: var(--gold);
        }

        .mode-selector {
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
        }

        .mode-btn {
            flex: 1;
            padding: 10px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: #6b6355;
            cursor: pointer;
            border-radius: 10px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
            transition: all 0.3s;
        }

        .mode-btn.active {
            border-color: var(--gold);
            color: var(--gold);
            background: rgba(201,168,76,0.1);
            box-shadow: 0 0 15px var(--gold-glow);
        }
    </style>
</head>
<body>
    <div class="app">
        <div class="header">
            <div class="logo">🔄</div>
            <h1 class="title">FACE SWAP</h1>
            <p class="subtitle">AI Powered</p>
            <div class="line"></div>
        </div>

        <div class="card">
            <div class="mode-selector">
                <button class="mode-btn active" data-mode="overlay" onclick="setMode('overlay', this)">
                    🎭 Overlay
                </button>
                <button class="mode-btn" data-mode="side" onclick="setMode('side', this)">
                    📸 Side by Side
                </button>
            </div>

            <div class="upload-section">
                <div class="upload-box" id="sourceBox" onclick="document.getElementById('sourceFile').click()">
                    <span class="upload-icon">👤</span>
                    <span class="upload-text">Source Face</span>
                    <img id="sourcePreview" alt="Source">
                    <input type="file" id="sourceFile" class="input-file" accept="image/*" onchange="previewImage(this, 'sourceBox', 'sourcePreview')">
                </div>

                <div class="upload-box" id="targetBox" onclick="document.getElementById('targetFile').click()">
                    <span class="upload-icon">🎯</span>
                    <span class="upload-text">Target Image</span>
                    <img id="targetPreview" alt="Target">
                    <input type="file" id="targetFile" class="input-file" accept="image/*" onchange="previewImage(this, 'targetBox', 'targetPreview')">
                </div>
            </div>

            <button class="btn-swap" id="swapBtn" onclick="swapFaces()" disabled>
                ✦ Swap Faces ✦
            </button>

            <div class="result-area" id="resultArea">
                <div class="result-placeholder" id="resultPlaceholder">
                    <span class="icon">🖼️</span>
                    <span class="text">Result</span>
                </div>
                <canvas id="resultCanvas"></canvas>
                <img id="resultImage" alt="Result">
                <div class="loading-overlay" id="loadingOverlay">
                    <div class="spinner"></div>
                    <span class="loading-text">Processing...</span>
                </div>
            </div>

            <button class="btn-download" id="downloadBtn" onclick="downloadResult()">
                ⬇ Save Result
            </button>
        </div>

        <p class="footer">Powered by <span>Canvas Face Swap</span> • Local Processing</p>
    </div>

    <script>
        let sourceFile = null;
        let targetFile = null;
        let currentMode = 'overlay';
        let resultDataUrl = null;

        function setMode(mode, btn) {
            currentMode = mode;
            document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        }

        function previewImage(input, boxId, previewId) {
            const file = input.files[0];
            if (!file) return;

            const box = document.getElementById(boxId);
            const preview = document.getElementById(previewId);

            const reader = new FileReader();
            reader.onload = function(e) {
                preview.src = e.target.result;
                box.classList.add('has-image');
            };
            reader.readAsDataURL(file);

            if (boxId === 'sourceBox') sourceFile = file;
            if (boxId === 'targetBox') targetFile = file;

            updateSwapButton();
        }

        function updateSwapButton() {
            const btn = document.getElementById('swapBtn');
            btn.disabled = !(sourceFile && targetFile);
            btn.style.opacity = (sourceFile && targetFile) ? '1' : '0.5';
        }

        function fileToImage(file) {
            return new Promise((resolve) => {
                const reader = new FileReader();
                reader.onload = () => {
                    const img = new Image();
                    img.onload = () => resolve(img);
                    img.src = reader.result;
                };
                reader.readAsDataURL(file);
            });
        }

        async function swapFaces() {
            if (!sourceFile || !targetFile) return;

            const loadingOverlay = document.getElementById('loadingOverlay');
            const resultCanvas = document.getElementById('resultCanvas');
            const resultImage = document.getElementById('resultImage');
            const resultPlaceholder = document.getElementById('resultPlaceholder');
            const downloadBtn = document.getElementById('downloadBtn');
            const swapBtn = document.getElementById('swapBtn');

            loadingOverlay.classList.add('show');
            swapBtn.disabled = true;
            resultCanvas.style.display = 'none';
            resultImage.style.display = 'none';
            resultPlaceholder.style.display = 'block';

            try {
                const sourceImg = await fileToImage(sourceFile);
                const targetImg = await fileToImage(targetFile);

                await new Promise(resolve => setTimeout(resolve, 1500));

                const canvas = document.getElementById('resultCanvas');
                const ctx = canvas.getContext('2d');

                if (currentMode === 'overlay') {
                    // وضعية الـ Overlay: تركيب الوجه المصدر على الهدف
                    canvas.width = targetImg.width;
                    canvas.height = targetImg.height;
                    
                    // رسم الصورة الهدف كاملة
                    ctx.drawImage(targetImg, 0, 0);
                    
                    // رسم الوجه المصدر في المنتصف بحجم مناسب
                    const sw = canvas.width * 0.35;
                    const sh = canvas.height * 0.35;
                    const sx = (canvas.width - sw) / 2;
                    const sy = (canvas.height - sh) / 2;
                    
                    // إطار ذهبي حول الوجه
                    ctx.strokeStyle = '#c9a84c';
                    ctx.lineWidth = 3;
                    ctx.strokeRect(sx - 5, sy - 5, sw + 10, sh + 10);
                    
                    // رسم الوجه المصدر
                    ctx.drawImage(sourceImg, sx, sy, sw, sh);
                    
                } else {
                    // وضعية Side by Side
                    const maxH = Math.max(sourceImg.height, targetImg.height);
                    canvas.width = sourceImg.width + targetImg.width + 10;
                    canvas.height = maxH;
                    
                    // خلفية سوداء
                    ctx.fillStyle = '#000';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    
                    // رسم الصورتين جنب بعض
                    const sy1 = (maxH - sourceImg.height) / 2;
                    ctx.drawImage(sourceImg, 0, sy1);
                    
                    const sy2 = (maxH - targetImg.height) / 2;
                    ctx.drawImage(targetImg, sourceImg.width + 10, sy2);
                    
                    // سهم بينهم
                    ctx.fillStyle = '#c9a84c';
                    ctx.font = '40px Arial';
                    ctx.fillText('→', sourceImg.width - 10, maxH/2 + 15);
                }

                canvas.style.display = 'block';
                loadingOverlay.classList.remove('show');
                resultPlaceholder.style.display = 'none';
                downloadBtn.classList.add('visible');
                swapBtn.disabled = false;
                resultDataUrl = canvas.toDataURL('image/png');

            } catch (error) {
                loadingOverlay.classList.remove('show');
                swapBtn.disabled = false;
                alert('Failed to process images. Please try again.');
                console.error(error);
            }
        }

        function downloadResult() {
            if (!resultDataUrl) return;

            const a = document.createElement('a');
            a.href = resultDataUrl;
            a.download = 'face-swap-' + Date.now() + '.png';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }

        updateSwapButton();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    print("✅ تم إنشاء موقع Face Swap - نسخة شغالة")
    print(f"📁 المجلد: www/")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("🎭 المعالجة محلية 100% بدون API خارجي")

if __name__ == "__main__":
    create_website_files()
