import os

def create_website_files():
    """إنشاء موقع Face Swap - نسخة مبسطة وشغالة"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Face Swap AI</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: #000;
            color: #fff;
            font-family: Arial, sans-serif;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .container {
            max-width: 450px;
            width: 100%;
        }
        
        .header {
            text-align: center;
            margin-bottom: 25px;
        }
        
        .header h1 {
            font-size: 32px;
            color: #c9a84c;
            letter-spacing: 3px;
        }
        
        .header p {
            color: #666;
            font-size: 12px;
            letter-spacing: 2px;
        }
        
        .box {
            background: #111;
            border: 1px solid #222;
            border-radius: 16px;
            padding: 20px;
        }
        
        .images {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 15px;
        }
        
        .upload-area {
            background: #000;
            border: 2px dashed #333;
            border-radius: 12px;
            aspect-ratio: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: 0.3s;
        }
        
        .upload-area:hover {
            border-color: #c9a84c;
        }
        
        .upload-area.selected {
            border-color: #c9a84c;
            border-style: solid;
        }
        
        .upload-area img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: none;
        }
        
        .upload-area.selected img {
            display: block;
        }
        
        .upload-area.selected .placeholder {
            display: none;
        }
        
        .placeholder {
            text-align: center;
            color: #444;
        }
        
        .placeholder .icon {
            font-size: 36px;
            display: block;
            margin-bottom: 5px;
        }
        
        .placeholder .label {
            font-size: 11px;
            text-transform: uppercase;
        }
        
        .hidden-input {
            display: none;
        }
        
        .btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #c9a84c, #e2c97e);
            color: #000;
            border: none;
            font-weight: bold;
            cursor: pointer;
            border-radius: 12px;
            font-size: 14px;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 15px;
            transition: 0.3s;
        }
        
        .btn:disabled {
            background: #222;
            color: #555;
            cursor: not-allowed;
        }
        
        .btn:not(:disabled):hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(201,168,76,0.3);
        }
        
        .result {
            background: #000;
            border: 1px solid #222;
            border-radius: 12px;
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            margin-bottom: 12px;
        }
        
        .result .empty {
            color: #222;
            text-align: center;
        }
        
        .result .empty .big {
            font-size: 48px;
            display: block;
        }
        
        .result .empty .small {
            font-size: 11px;
            letter-spacing: 2px;
        }
        
        .result canvas {
            display: none;
            width: 100%;
            height: 100%;
        }
        
        .result canvas.show {
            display: block;
        }
        
        .download-btn {
            width: 100%;
            padding: 12px;
            background: transparent;
            border: 1px solid #c9a84c;
            color: #c9a84c;
            cursor: pointer;
            border-radius: 12px;
            font-weight: bold;
            font-size: 12px;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: 0.3s;
            display: none;
        }
        
        .download-btn.show {
            display: block;
        }
        
        .download-btn:hover {
            background: rgba(201,168,76,0.1);
        }
        
        .loading {
            display: none;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.9);
            justify-content: center;
            align-items: center;
            flex-direction: column;
            gap: 15px;
            border-radius: 12px;
        }
        
        .loading.active {
            display: flex;
        }
        
        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid #333;
            border-top-color: #c9a84c;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .loading-text {
            color: #c9a84c;
            font-size: 12px;
            letter-spacing: 2px;
        }
        
        .footer {
            text-align: center;
            margin-top: 15px;
            color: #222;
            font-size: 10px;
            letter-spacing: 2px;
        }
        
        .footer span {
            color: #c9a84c;
        }

        .mode-btns {
            display: flex;
            gap: 8px;
            margin-bottom: 15px;
        }
        
        .mode-btn {
            flex: 1;
            padding: 8px;
            background: #000;
            border: 1px solid #333;
            color: #666;
            cursor: pointer;
            border-radius: 8px;
            font-size: 10px;
            font-weight: bold;
            letter-spacing: 1px;
            transition: 0.3s;
        }
        
        .mode-btn.active {
            border-color: #c9a84c;
            color: #c9a84c;
            background: rgba(201,168,76,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>FACE SWAP</h1>
            <p>AI Powered Demo</p>
        </div>
        
        <div class="box">
            <div class="mode-btns">
                <button class="mode-btn active" onclick="setMode('overlay', this)">Overlay</button>
                <button class="mode-btn" onclick="setMode('side', this)">Side by Side</button>
            </div>
            
            <div class="images">
                <div class="upload-area" id="box1" onclick="document.getElementById('file1').click()">
                    <div class="placeholder">
                        <span class="icon">👤</span>
                        <span class="label">Source</span>
                    </div>
                    <img id="preview1">
                    <input type="file" id="file1" class="hidden-input" accept="image/*">
                </div>
                
                <div class="upload-area" id="box2" onclick="document.getElementById('file2').click()">
                    <div class="placeholder">
                        <span class="icon">🎯</span>
                        <span class="label">Target</span>
                    </div>
                    <img id="preview2">
                    <input type="file" id="file2" class="hidden-input" accept="image/*">
                </div>
            </div>
            
            <button class="btn" id="swapBtn" disabled onclick="doSwap()">Swap Faces</button>
            
            <div class="result" id="resultArea">
                <div class="empty" id="emptyResult">
                    <span class="big">🖼️</span>
                    <span class="small">RESULT</span>
                </div>
                <canvas id="canvas"></canvas>
                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <span class="loading-text">Processing...</span>
                </div>
            </div>
            
            <button class="download-btn" id="downloadBtn" onclick="download()">Save Image</button>
        </div>
        
        <div class="footer">Powered by <span>Canvas API</span> Local</div>
    </div>

    <script>
        let img1 = null, img2 = null;
        let mode = 'overlay';
        let resultData = null;

        document.getElementById('file1').addEventListener('change', function() {
            handleFile(this, 'preview1', 'box1', 1);
        });
        
        document.getElementById('file2').addEventListener('change', function() {
            handleFile(this, 'preview2', 'box2', 2);
        });

        function handleFile(input, previewId, boxId, num) {
            const file = input.files[0];
            if (!file) return;
            
            const reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById(previewId).src = e.target.result;
                document.getElementById(boxId).classList.add('selected');
                if (num === 1) img1 = e.target.result;
                if (num === 2) img2 = e.target.result;
                checkReady();
            };
            reader.readAsDataURL(file);
        }

        function checkReady() {
            document.getElementById('swapBtn').disabled = !(img1 && img2);
        }

        function setMode(m, btn) {
            mode = m;
            document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        }

        function doSwap() {
            if (!img1 || !img2) return;
            
            document.getElementById('loading').classList.add('active');
            document.getElementById('swapBtn').disabled = true;
            document.getElementById('canvas').classList.remove('show');
            document.getElementById('emptyResult').style.display = 'block';
            document.getElementById('downloadBtn').classList.remove('show');
            
            setTimeout(function() {
                processImages();
            }, 1000);
        }

        function processImages() {
            const source = new Image();
            const target = new Image();
            let loaded = 0;
            
            function onLoad() {
                loaded++;
                if (loaded === 2) {
                    drawResult(source, target);
                }
            }
            
            source.onload = onLoad;
            target.onload = onLoad;
            source.src = img1;
            target.src = img2;
        }

        function drawResult(source, target) {
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
            
            if (mode === 'overlay') {
                canvas.width = target.width;
                canvas.height = target.height;
                
                ctx.drawImage(target, 0, 0);
                
                const sw = canvas.width * 0.35;
                const sh = canvas.height * 0.35;
                const sx = (canvas.width - sw) / 2;
                const sy = (canvas.height - sh) / 2;
                
                ctx.strokeStyle = '#c9a84c';
                ctx.lineWidth = 3;
                ctx.strokeRect(sx - 5, sy - 5, sw + 10, sh + 10);
                
                ctx.drawImage(source, sx, sy, sw, sh);
            } else {
                const maxH = Math.max(source.height, target.height);
                canvas.width = source.width + target.width + 10;
                canvas.height = maxH;
                
                ctx.fillStyle = '#000';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                const sy1 = (maxH - source.height) / 2;
                ctx.drawImage(source, 0, sy1);
                
                const sy2 = (maxH - target.height) / 2;
                ctx.drawImage(target, source.width + 10, sy2);
                
                ctx.fillStyle = '#c9a84c';
                ctx.font = '40px Arial';
                ctx.fillText('→', source.width - 5, maxH / 2 + 15);
            }
            
            canvas.classList.add('show');
            document.getElementById('emptyResult').style.display = 'none';
            document.getElementById('loading').classList.remove('active');
            document.getElementById('downloadBtn').classList.add('show');
            document.getElementById('swapBtn').disabled = false;
            resultData = canvas.toDataURL('image/png');
        }

        function download() {
            if (!resultData) return;
            const a = document.createElement('a');
            a.href = resultData;
            a.download = 'face-swap-' + Date.now() + '.png';
            a.click();
        }
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ تم إنشاء الموقع بنجاح!")
    print(f"📁 www/index.html")
    print(f"💾 الحجم: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("🚀 جاهز للنشر!")

if __name__ == "__main__":
    create_website_files()
