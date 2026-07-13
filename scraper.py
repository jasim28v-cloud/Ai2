import os

def create_website_files():
    """إنشاء موقع Face Swap AI الفخم"""
    
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

        .note {
            font-size: 9px;
            color: #ff4444;
            text-align: center;
            margin-top: 8px;
            letter-spacing: 1px;
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
                <img id="resultImage" alt="Result">
                <div class="loading-overlay" id="loadingOverlay">
                    <div class="spinner"></div>
                    <span class="loading-text">Swapping Faces...</span>
                </div>
            </div>

            <button class="btn-download" id="downloadBtn" onclick="downloadResult()">
                ⬇ Save Result
            </button>
        </div>

        <p class="note">⚠️ Use clear front-facing photos for best results</p>
        <p class="footer">Powered by <span>AI Face Swap</span> • Free & Unlimited</p>
    </div>

    <script>
        let sourceFile = null;
        let targetFile = null;
        let resultImageUrl = null;

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

        async function swapFaces() {
            if (!sourceFile || !targetFile) return;

            const loadingOverlay = document.getElementById('loadingOverlay');
            const resultImage = document.getElementById('resultImage');
            const resultPlaceholder = document.getElementById('resultPlaceholder');
            const downloadBtn = document.getElementById('downloadBtn');
            const swapBtn = document.getElementById('swapBtn');

            loadingOverlay.classList.add('show');
            swapBtn.disabled = true;
            resultImage.style.display = 'none';
            resultPlaceholder.style.display = 'block';

            try {
                const sourceBase64 = await fileToBase64(sourceFile);
                const targetBase64 = await fileToBase64(targetFile);

                // Using free API for face swap
                const swappedUrl = await performFaceSwap(sourceBase64, targetBase64);

                resultImage.src = swappedUrl;
                resultImage.onload = function() {
                    loadingOverlay.classList.remove('show');
                    resultImage.style.display = 'block';
                    resultPlaceholder.style.display = 'none';
                    downloadBtn.classList.add('visible');
                    swapBtn.disabled = false;
                    resultImageUrl = swappedUrl;
                };
            } catch (error) {
                loadingOverlay.classList.remove('show');
                swapBtn.disabled = false;
                alert('Failed to swap faces. Please try again with clearer photos.');
                console.error(error);
            }
        }

        function fileToBase64(file) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = () => resolve(reader.result.split(',')[1]);
                reader.onerror = reject;
                reader.readAsDataURL(file);
            });
        }

        async function performFaceSwap(sourceBase64, targetBase64) {
            // Using Hugging Face free API for face swap
            const response = await fetch('https://api-inference.huggingface.co/models/ezioruan/face-swap', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    inputs: {
                        source: sourceBase64,
                        target: targetBase64
                    }
                })
            });

            if (!response.ok) {
                throw new Error('API request failed');
            }

            const blob = await response.blob();
            return URL.createObjectURL(blob);
        }

        function downloadResult() {
            if (!resultImageUrl) return;

            const a = document.createElement('a');
            a.href = resultImageUrl;
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

    print("✅ تم إنشاء موقع Face Swap AI الفخم")
    print(f"📁 المجلد: www/")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")

if __name__ == "__main__":
    create_website_files()
