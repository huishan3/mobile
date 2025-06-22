<!DOCTYPE html>
<html lang="zh-Hant">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Melody Beans</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      /* Define 標楷體 as a web font */
      @font-face {
        font-family: 'BiaoKaiTiWeb'; /* This is the name you'll use in your CSS */
        src: url('./fonts/BiaoKaiTi.woff2') format('woff2'), /* Path to your WOFF2 font file */
             url('./fonts/BiaoKaiTi.woff') format('woff'),    /* Path to your WOFF font file */
             url('./fonts/DFKai-SB.ttf') format('truetype'); /* Fallback to TTF if needed, ensure path is correct */
        font-weight: normal; /* 標楷體 typically has one weight */
        font-style: normal;
        font-display: swap; /* Very important: Shows fallback text while font loads */
      }

      html {
        scroll-behavior: smooth;
      }
      body {
        /* Set the body font to your custom web font first, then system fallbacks */
        font-family: 'BiaoKaiTiWeb', 'DFKai-SB', '標楷體', 'PingFang TC', 'Microsoft JhengHei', sans-serif;
        background-color: #fdfaf5;
        background-image: url('https://www.transparenttextures.com/patterns/wood-pattern.png');
        background-size: cover;
        background-attachment: fixed;
        color: #3f2e2e;
      }
      .staff-lines {
        background-image: linear-gradient(to bottom, transparent 18%, #ccc 18%, #ccc 19%, transparent 19%, transparent 38%, #ccc 38%, #ccc 39%, transparent 39%, transparent 58%, #ccc 58%, #ccc 59%, transparent 59%, transparent 78%, #ccc 78%, #ccc 79%, transparent 79%);
        background-size: 100% 100px;
        background-repeat: repeat-y;
        opacity: 0.05;
      }
      .floating-note {
        position: absolute;
        animation: floatNote 6s ease-in-out infinite;
        font-size: 1.5rem;
        color: #b58863;
        opacity: 0;
      }
      @keyframes floatNote {
        0% { transform: translateY(20px); opacity: 0; }
        50% { opacity: 0.6; }
        100% { transform: translateY(-100px); opacity: 0; }
      }
      .fade-up {
        opacity: 0;
        transform: translateY(60px);
        transition: opacity 1.2s ease-out, transform 1.2s ease-out;
      }
      .fade-up.active {
        opacity: 1;
        transform: translateY(0);
      }
      .floating-cart {
        position: fixed;
        bottom: 24px;
        right: 24px;
        background-color: #b58863;
        color: white;
        border-radius: 9999px;
        padding: 16px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        font-size: 1.5rem;
        z-index: 1000;
        transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out; /* Added opacity for smooth hide/show */
      }
      .floating-cart:hover {
        transform: scale(1.1);
      }
      /* 浮動購物車彈跳動畫 */
      @keyframes pop {
        0% { transform: scale(1); }
        50% { transform: scale(1.15); }
        100% { transform: scale(1); }
      }
      .animate-pop {
        animation: pop 0.3s ease-out;
      }

      .ornate-box {
        border: 2px solid #b58863;
        border-radius: 1rem;
        background: url('https://www.transparenttextures.com/patterns/wood-pattern.png'); /* 卡片內部維持木紋 */
        background-size: cover;
        padding: 1rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* 添加陰影過渡 */
      }
      .ornate-box:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2); /* 懸停時陰影變大變深 */
      }
      /* Custom styles for table cells */
      .cart-table td {
        padding: 8px; /* Add some padding */
        vertical-align: middle; /* Align content vertically */
      }
      /* Checkout Modal Background Blur */
      #checkoutModal, #memberModal {
        backdrop-filter: blur(5px); /* Add this for blur effect on the background */
      }
      /* 導航連結 Hover 效果 */
      .navbar-link-hover:hover {
        color: #b58863; /* 改變文字顏色 */
        transition: color 0.3s ease-in-out; /* 平滑過渡 */
      }
      /* 按鈕點擊效果 */
      .btn-press:active {
        transform: translateY(1px); /* 輕微下壓 */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* 陰影變小 */
      }

      /* 首頁背景樣式 */
      #home {
        background-image: url('./image/image_2.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh; /* 調整為視窗高度 */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        position: relative;
        overflow: hidden;
      }

      /* 背景疊層 */
      #home::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.4);
        z-index: 1;
      }

      #home > * {
        position: relative;
        z-index: 2;
      }

      /* 調整staff-lines透明度以適應深色背景 */
      #home .staff-lines {
        opacity: 0.15;
        background-image: linear-gradient(to bottom, transparent 18%, rgba(255, 255, 255, 0.3) 18%, rgba(255, 255, 255, 0.3) 19%, transparent 19%, transparent 38%, rgba(255, 255, 255, 0.3) 38%, rgba(255, 255, 255, 0.3) 39%, transparent 39%, transparent 58%, rgba(255, 255, 255, 0.3) 58%, rgba(255, 255, 255, 0.3) 59%, transparent 59%, transparent 78%, rgba(255, 255, 255, 0.3) 78%, rgba(255, 255, 255, 0.3) 79%, transparent 79%);
      }
      /* 調整浮動音符的顏色以適應深色背景 */
      #home .floating-note {
          color: #f0e68c;
      }

      /* 為響應式設計調整主要內容區塊的內邊距 */
      @media (max-width: 767px) { /* Small screens (mobile) */
        .px-6 {
          padding-left: 1rem; /* px-4 = 16px */
          padding-right: 1rem;
        }
        .text-5xl { /* 針對小螢幕調整標題大小 */
          font-size: 2.5rem; /* 約 40px */
        }
        .text-xl { /* 針對小螢幕調整副標題大小 */
          font-size: 1.125rem; /* 約 18px */
        }
      }

      @media (min-width: 768px) and (max-width: 1023px) { /* Medium screens (tablet) */
        .px-6 {
          padding-left: 1.5rem; /* px-6 = 24px */
          padding-right: 1.5rem;
        }
        .text-5xl {
          font-size: 3.5rem; /* 約 56px */
        }
        .text-xl {
          font-size: 1.25rem; /* 約 20px */
        }
      }

      @media (min-width: 1024px) { /* Large screens (desktop) */
        .px-6 {
          padding-left: 1.5rem; /* px-6 = 24px */
          padding-right: 1.5rem;
        }
        .text-5xl {
          font-size: 4rem; /* 64px */
        }
        .text-xl {
          font-size: 1.5rem; /* 24px */
        }
      }

    </style>
  </head>
  <body class="text-[#3f2e2e]">
    <nav class="bg-[#f5efe6] shadow-md sticky top-0 z-50 fade-up">
      <div class="max-w-[1200px] mx-auto flex justify-between items-center py-4 px-6">
        <div class="flex items-center">
            <img src="./image/image_2.png" alt="Melody Beans Logo" class="h-10 mr-3" />
            <h1 class="text-2xl font-bold">🎼 Melody Beans</h1>
        </div>
        <button id="menu-button" class="md:hidden text-2xl px-2 py-1 focus:outline-none focus:ring-2 focus:ring-[#b58863] rounded">
          ☰
        </button>
        <ul id="navbar-links" class="hidden md:flex gap-6 text-lg">
          <li><a href="#home" class="hover:underline navbar-link-hover" onclick="closeMenu()">首頁</a></li>
          <li><a href="#products" class="hover:underline navbar-link-hover" onclick="closeMenu()">商品</a></li>
          <li><a href="#education" class="hover:underline navbar-link-hover" onclick="closeMenu()">咖啡知識</a></li>
          <li><a href="#cart" class="hover:underline navbar-link-hover" onclick="closeMenu()">購物車</a></li>
          <li><a href="#review" class="hover:underline navbar-link-hover" onclick="closeMenu()">評論</a></li>
          <li><a href="#about" class="hover:underline navbar-link-hover" onclick="closeMenu()">關於我們</a></li>
          <li><a href="#" class="hover:underline navbar-link-hover" onclick="openMemberModal(); return false;" id="memberLink">會員登入/註冊</a></li>
        </ul>
        <button class="ml-4 text-sm underline hidden md:block">EN</button> </div>
      <div id="mobile-menu" class="hidden md:hidden bg-[#f5efe6] pb-4 px-6">
        <ul class="flex flex-col gap-2 text-lg">
          <li><a href="#home" class="block py-2 hover:bg-[#eae0d5] rounded" onclick="closeMenu()">首頁</a></li>
          <li><a href="#products" class="block py-2 hover:bg-[#eae0d5] rounded" onclick="closeMenu()">商品</a></li>
          <li><a href="#education" class="block py-2 hover:bg-[#eae0d5] rounded" onclick="closeMenu()">咖啡知識</a></li>
          <li><a href="#cart" class="block py-2 hover:bg-[#eae0d5] rounded" onclick="closeMenu()">購物車</a></li>
          <li><a href="#review" class="block py-2 hover:bg-[#eae0d5] rounded" onclick="closeMenu()">評論</a></li>
          <li><a href="#about" class="block py-2 hover:bg-[#eae0d5] rounded" onclick="closeMenu()">關於我們</a></li>
          <li><a href="#" class="block py-2 hover:bg-[#eae0d5] rounded" onclick="openMemberModal(); closeMenu(); return false;">會員登入/註冊</a></li>
        </ul>
        <button class="mt-4 text-sm underline block mx-auto">EN</button>
      </div>
    </nav>

    <section id="home" class="fade-up">
      <div class="staff-lines absolute inset-0"></div>
      <div class="floating-note" style="top:65%;left:10%">𝄞</div>
      <div class="floating-note" style="top:75%;left:80%">♩</div>
      <div class="floating-note" style="top:70%;left:20%">♪</div>
      <div class="floating-note" style="top:80%;left:60%">♬</div>

      <div class="max-w-[800px] px-6 z-10 flex flex-col justify-center items-center text-center">
        <h2 class="text-5xl md:text-6xl lg:text-7xl font-extrabold mb-4 drop-shadow">讓每一杯咖啡☕都有旋律🎵</h2>
        <p class="text-xl md:text-2xl lg:text-3xl text-white font-medium">結合咖啡的香與音樂的韻，啟動生活靈感。</p>
      </div>
    </section>

    <section id="products" class="py-16 fade-up">
      <div class="max-w-[1200px] mx-auto px-6">
        <h2 class="text-3xl mb-6 text-center">🎵 精選咖啡豆</h2>
        <div class="mb-6 flex flex-col sm:flex-row items-center justify-center gap-4">
          <div class="flex items-center w-full sm:w-auto">
            <label for="category" class="mr-2 font-bold">分類：</label>
            <select id="category" class="p-2 border rounded bg-[#fffdf8] shadow-md hover:border-[#b58863] focus:outline-none w-full sm:w-auto">
              <option value="all">全部</option>
              <option value="light">淺焙</option>
              <option value="medium">中焙</option>
              <option value="dark">深焙</option>
            </select>
          </div>
          <div class="flex items-center w-full sm:w-auto">
            <label for="product-search" class="sr-only">搜尋商品</label>
            <input type="text" id="product-search" placeholder="搜尋商品名稱或風味..." class="p-2 border rounded w-full bg-[#fffdf8] shadow-md hover:border-[#b58863] focus:outline-none" />
          </div>
        </div>
        <div id="product-cards" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
      </div>
    </section>

    <!-- 新增咖啡教育內容區塊 -->
    <section id="education" class="py-16 bg-[#fdfaf5] fade-up">
      <div class="max-w-[1000px] mx-auto px-6">
        <h2 class="text-3xl mb-8 text-center text-[#b58863]">📚 咖啡知識殿堂</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- 咖啡文章區塊 -->
          <div class="ornate-box p-6">
            <h3 class="text-2xl font-bold mb-4">深入了解咖啡處理法</h3>
            
            <div class="mb-6">
              <h4 class="text-xl font-semibold mb-2">☀️ 日曬法（Natural Process）</h4>
              <p class="mb-1">想像把新鮮的咖啡果實鋪在陽光下曬乾，像曬葡萄變葡萄乾。這就是日曬法。咖啡果實在曬乾的過程中，果肉的糖分會慢慢滲進豆子裡，讓它變得甜甜的，像是水果乾的感覺。</p>
              <p class="font-bold">📌 風味特色：</p>
              <ul class="list-disc list-inside ml-4 mb-2 text-sm">
                <li>香氣奔放、甜感明顯、常有莓果或葡萄乾的味道。</li>
              </ul>
              <p class="font-bold">📌 適合喜歡：</p>
              <ul class="list-disc list-inside ml-4 mb-4 text-sm">
                <li>果香調、熱情奔放風味的你。</li>
              </ul>
            </div>

            <div class="mb-6">
              <h4 class="text-xl font-semibold mb-2">💧 水洗法（Washed Process）</h4>
              <p class="mb-1">水洗法像是幫咖啡果實洗香香——把果肉用水沖掉，留下純淨的豆子。這種方式讓豆子的本質被保留下來，像是聽一首沒有伴奏的純淨旋律。</p>
              <p class="font-bold">📌 風味特色：</p>
              <ul class="list-disc list-inside ml-4 mb-2 text-sm">
                <li>乾淨、明亮、酸值清晰、口感輕盈。</li>
              </ul>
              <p class="font-bold">📌 適合喜歡：</p>
              <ul class="list-disc list-inside ml-4 mb-4 text-sm">
                <li>茶感、清新、精緻風味的你。</li>
              </ul>
            </div>

            <div class="mb-6">
              <h4 class="text-xl font-semibold mb-2">🍯 蜜處理法（Honey Process）</h4>
              <p class="mb-1">蜜處理不是加蜂蜜，而是讓咖啡果肉的「黏黏果膠層」保留在豆子上曬乾，像是一層自然糖漿。這就像是把日曬的甜感和水洗的清爽融合在一起，達到剛剛好的甜美平衡。</p>
              <p class="font-bold">📌 風味特色：</p>
              <ul class="list-disc list-inside ml-4 mb-2 text-sm">
                <li>甜中帶酸、柔和圓潤、常有蜂蜜、水果、太妃糖的味道。</li>
              </ul>
              <p class="font-bold">📌 適合喜歡：</p>
              <ul class="list-disc list-inside ml-4 mb-4 text-sm">
                <li>平衡感、圓滑口感的你。</li>
              </ul>
            </div>

            <div class="mb-6">
              <h4 class="text-xl font-semibold mb-2">🌌 厭氧發酵（Anaerobic Fermentation）</h4>
              <p class="mb-1">這是咖啡界的實驗室風味。咖啡果實被放進密閉容器中，不讓氧氣進來，像是「閉門造車」般發酵。這種方式可以創造出很特別的香氣和層次，有時像酒、有時像香料。</p>
              <p class="font-bold">📌 風味特色：</p>
              <ul class="list-disc list-inside ml-4 mb-2 text-sm">
                <li>香氣奔放、口感層次豐富，帶有酒香、發酵感。</li>
              </ul>
              <p class="font-bold">📌 適合喜歡：</p>
              <ul class="list-disc list-inside ml-4 mb-4 text-sm">
                <li>獨特、冒險、不一樣風味體驗的你。</li>
              </ul>
            </div>

          </div>

          <!-- 咖啡影片與保存方式區塊 -->
          <div class="ornate-box p-6">
            <h3 class="text-2xl font-bold mb-4">專業沖煮與保存</h3>
            <p class="mb-4">學會正確的沖煮技巧和保存方式，讓您的每一杯咖啡都能達到最佳風味。</p>
            
            <div class="mb-6">
              <h4 class="text-xl font-semibold mb-2">推薦沖煮影片：</h4>
              <div class="aspect-video bg-gray-200 rounded overflow-hidden">
                <!-- 嵌入 YouTube 影片或使用佔位圖 -->
                <iframe 
                  src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
                  frameborder="0" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen
                  class="w-full h-full"
                  title="如何手沖咖啡 - 示範影片">
                </iframe>
                <p class="text-center text-sm text-gray-600 mt-2">（此為示範影片，實際將嵌入相關教學影片）</p>
              </div>
            </div>

            <div>
              <h4 class="text-xl font-semibold mb-2">咖啡豆保存方式：</h4>
              <ul class="list-disc list-inside space-y-2">
                <li>密封保存：使用不透光、密封性好的容器。</li>
                <li>避光避濕：避免陽光直射和潮濕環境。</li>
                <li>避免異味：遠離有強烈氣味的物品。</li>
                <li>適溫存放：建議存放在陰涼乾燥處，無需冷藏或冷凍（除非長時間保存）。</li>
                <li>最佳賞味期：咖啡豆開封後，建議在一個月內飲用完畢以保持最佳風味。</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="cart" class="py-16 bg-[#fff9f0] fade-up">
      <div class="max-w-[900px] mx-auto px-6">
        <h2 class="text-2xl mb-4">🛒 購物車</h2>
        <div class="overflow-x-auto">
          <table class="w-full border text-left cart-table">
            <thead>
              <tr class="bg-[#f5efe6]">
                <th class="p-2 border whitespace-nowrap">商品</th>
                <th class="p-2 border whitespace-nowrap">數量</th>
                <th class="p-2 border whitespace-nowrap">單價</th>
                <th class="p-2 border whitespace-nowrap">小計</th>
              </tr>
            </thead>
            <tbody id="cart-body"></tbody>
          </table>
        </div>
        <p class="text-right mt-4 font-bold">總金額：<span id="total-amount">NT$0</span></p>
        <p class="text-sm text-red-600 text-right mt-2 font-bold">※ 本網站所有商品不提供退換貨服務。</p>
        <div class="text-right mt-4">
          <button onclick="checkout()" class="bg-[#3f2e2e] text-white px-6 py-2 rounded btn-press">結帳</button>
        </div>
      </div>
    </section>

    <section id="review" class="bg-[#fdfaf5] py-16 fade-up">
      <div class="max-w-[600px] mx-auto px-6">
        <h2 class="text-2xl mb-6 text-center">留下您的評論</h2>
        <form class="grid gap-4" onsubmit="submitReview(event)">
          <input id="reviewer" type="text" placeholder="您的名稱" class="p-3 border rounded" required />
          <textarea id="review-content" rows="4" placeholder="您的評論內容..." class="p-3 border rounded" required></textarea>
          <select id="review-rating" class="p-3 border rounded" required>
            <option value="" disabled selected>給我們幾顆星？</option>
            <option value="⭐️⭐️⭐️⭐️⭐️">⭐️⭐️⭐️⭐️⭐️</option>
            <option value="⭐️⭐️⭐️⭐️">⭐️⭐️⭐️⭐️</option>
            <option value="⭐️⭐️⭐️">⭐️⭐️⭐️</option>
            <option value="⭐️⭐️">⭐️⭐️</option>
            <option value="⭐️">⭐️</option>
          </select> 
          <button type="submit" class="bg-[#3f2e2e] text-white px-6 py-2 rounded btn-press">送出評論</button>
        </form>
        <div id="review-list" class="mt-6 space-y-4"></div>
      </div>
    </section>

    <section id="about" class="bg-[#fffdf8] py-16 fade-up">
      <div class="max-w-[1000px] mx-auto px-6 text-center">
        <h2 class="text-3xl mb-4">關於 Melody Beans</h2>
        <p class="mb-4">我們是一家結合音樂靈感與手工咖啡的品牌，每款豆子皆源自一段旋律，希望每一口都讓你想起一首歌。</p>
        <p class="mb-1">📞 電話：03-4081932</p>
        <p class="mb-1">🏠 地址：桃園市中壢區中正路4段141號</p>
      </div>
    </section>

    <footer class="text-center py-6 bg-[#f5efe6] text-sm text-[#3f2e2e]">
      © 2025 Melody Beans. 品味旋律，啜飲人生。
    </footer>

    <div id="floatingCart" class="floating-cart" onclick="toggleCartPanel(); renderCartPanel()">
      🛒
      <span id="cart-badge" class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">0</span>
    </div>

    <div id="cartPanel" class="fixed top-0 right-0 w-full md:w-[300px] h-full bg-[#fff9f0] shadow-lg p-4 transform translate-x-full transition-transform duration-300 z-[9999] overflow-y-auto">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-bold">🛍️ 購物清單</h2>
        <button onclick="toggleCartPanel()" class="text-xl font-bold text-[#b58863]">✕</button>
      </div>
      <div id="cartPanelBody" class="space-y-4 text-sm">
        </div>
      <div class="mt-4 text-right font-bold">總金額：<span id="panelTotal">NT$0</span></div>
      <div class="mt-2 text-right">
        <button onclick="checkout()" class="bg-[#3f2e2e] text-white px-4 py-2 rounded btn-press">結帳</button>
      </div>
    </div> 

    <!-- 會員登入/註冊模態框 -->
    <div id="memberModal" class="fixed inset-0 bg-gray-900 bg-opacity-75 flex items-center justify-center z-[10001] hidden">
      <div class="bg-[#fff9f0] p-8 rounded-lg shadow-2xl w-full max-w-sm relative ornate-box transform scale-95 opacity-0 transition-all duration-300 mx-4" id="memberModalContent">
        <button onclick="closeMemberModal()" class="absolute top-4 right-4 text-gray-600 hover:text-gray-900 text-2xl font-bold">✕</button>
        <h2 class="text-2xl font-bold mb-6 text-center text-[#b58863]">會員登入 / 註冊</h2>
        
        <div id="loginSection">
          <form id="loginForm" class="grid gap-4">
            <div>
              <label for="loginEmail" class="block text-sm font-medium text-gray-700 mb-1">電子郵件</label>
              <input type="email" id="loginEmail" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="請輸入您的電子郵件" required>
            </div>
            <div>
              <label for="loginPassword" class="block text-sm font-medium text-gray-700 mb-1">密碼</label>
              <input type="password" id="loginPassword" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="請輸入密碼" required>
            </div>
            <button type="submit" class="bg-[#b58863] text-white px-6 py-3 rounded-md hover:bg-[#a07a5c] transition-colors duration-300 text-lg font-semibold btn-press">登入</button>
          </form>
          <p class="text-center mt-4">還沒有帳號？<button onclick="showRegisterForm()" class="text-blue-600 hover:underline">立即註冊</button></p>
        </div>

        <div id="registerSection" class="hidden">
          <form id="registerForm" class="grid gap-4">
            <div>
              <label for="registerEmail" class="block text-sm font-medium text-gray-700 mb-1">電子郵件</label>
              <input type="email" id="registerEmail" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="請輸入您的 Gmail 帳號" required pattern=".+@gmail\.com$" title="請輸入有效的 Gmail 帳號 (例如: example@gmail.com)">
            </div>
            <div>
              <label for="registerPassword" class="block text-sm font-medium text-gray-700 mb-1">密碼</label>
              <input type="password" id="registerPassword" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="設定密碼 (至少6位)" required minlength="6">
            </div>
            <button type="submit" class="bg-[#3f2e2e] text-white px-6 py-3 rounded-md hover:bg-[#5a4444] transition-colors duration-300 text-lg font-semibold btn-press">註冊</button>
          </form>
          <p class="text-center mt-4">已有帳號？<button onclick="showLoginForm()" class="text-blue-600 hover:underline">返回登入</button></p>
        </div>

        <div id="memberInfo" class="hidden text-center py-4">
          <h3 class="text-xl font-bold mb-4">會員資訊</h3>
          <p class="mb-2">歡迎，<strong id="loggedInUserEmail"></strong>！</p>
          <button onclick="viewPurchaseHistory()" class="bg-[#b58863] text-white px-4 py-2 rounded-md hover:bg-[#a07a5c] transition-colors duration-300 btn-press">查看購買紀錄</button>
          <button onclick="logout()" class="bg-gray-500 text-white px-4 py-2 rounded-md hover:bg-gray-600 transition-colors duration-300 ml-2 btn-press">登出</button>
        </div>

        <div id="purchaseHistorySection" class="hidden mt-6">
            <h4 class="text-xl font-semibold mb-3">您的購買紀錄</h4>
            <div id="purchaseHistoryList" class="space-y-3 max-h-60 overflow-y-auto">
                <!-- 購買紀錄將動態載入這裡 -->
            </div>
            <button onclick="hidePurchaseHistory()" class="mt-4 bg-gray-500 text-white px-4 py-2 rounded-md hover:bg-gray-600 transition-colors duration-300 btn-press">返回會員中心</button>
        </div>

      </div>
    </div>


    <div id="checkoutModal" class="fixed inset-0 bg-gray-900 bg-opacity-75 flex items-center justify-center z-[10000] hidden">
      <div class="bg-[#fff9f0] p-8 rounded-lg shadow-2xl w-full max-w-lg relative ornate-box transform scale-95 opacity-0 transition-all duration-300 mx-4 sm:mx-auto max-h-[90vh] overflow-y-auto" id="checkoutModalContent">
        <button onclick="closeCheckoutModal()" class="absolute top-4 right-4 text-gray-600 hover:text-gray-900 text-2xl font-bold">✕</button>
        
        <h2 class="text-2xl font-bold mb-6 text-center text-[#b58863]">訂單確認與結帳</h2>
        
        <div id="orderSummary" class="mb-6 border-b border-gray-300 pb-4">
          <h3 class="text-xl font-semibold mb-3">您的訂單</h3>
          <div id="modalCartItems" class="space-y-1 text-sm max-h-40 overflow-y-auto pr-2"> 
            </div>
          <p class="text-right font-bold text-lg mt-4">小計：<span id="modalSubTotalAmount">NT$0</span></p>
          <p class="text-right text-sm text-gray-600">運費：NT$<span id="shippingFee">60</span></p>
          <p class="text-right font-bold text-xl mt-2">總金額：<span id="modalTotalAmount">NT$0</span></p>
        </div>

        <form id="checkoutForm" class="grid grid-cols-1 gap-4">
          <p class="text-sm text-red-600 font-bold">※ 本網站所有商品不提供退換貨服務。請您確認後再下單。</p>
          <div>
            <label for="customerName" class="block text-sm font-medium text-gray-700 mb-1">收件人姓名</label>
            <input type="text" id="customerName" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="請輸入您的姓名" required>
          </div>
          <div>
            <label for="customerPhone" class="block text-sm font-medium text-gray-700 mb-1">聯絡電話</label>
            <input type="tel" id="customerPhone" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="請輸入聯絡電話" required>
          </div>
          <div>
            <label for="customerAddress" class="block text-sm font-medium text-gray-700 mb-1">收件地址</label>
            <textarea id="customerAddress" rows="3" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="請輸入收件地址" required></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">付款方式</label>
            <div class="flex flex-col gap-2">
              <label class="inline-flex items-center">
                <input type="radio" name="paymentMethod" value="cashOnDelivery" class="form-radio text-[#b58863]" checked onchange="toggleCreditCardFields(this)">
                <span class="ml-2">貨到付款</span>
              </label>
              <label class="inline-flex items-center">
                <input type="radio" name="paymentMethod" value="creditCard" class="form-radio text-[#b58863]" onchange="toggleCreditCardFields(this)">
                <span class="ml-2">信用卡 (此為模擬，無實際扣款)</span>
              </label>
            </div>
            <div id="creditCardFields" class="mt-4 grid grid-cols-1 gap-3 hidden">
                <div>
                    <label for="cardNumber" class="block text-sm font-medium text-gray-700 mb-1">信用卡號</label>
                    <input type="text" id="cardNumber" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="XXXX XXXX XXXX XXXX" pattern="\d{16}" title="請輸入16位數字信用卡號" disabled>
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label for="expiryDate" class="block text-sm font-medium text-gray-700 mb-1">有效期 (MM/YY)</label>
                        <input type="text" id="expiryDate" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="MM/YY" pattern="(0[1-9]|1[0-2])\/\d{2}" title="請輸入MM/YY格式，例如01/25" disabled>
                    </div>
                    <div>
                        <label for="cvv" class="block text-sm font-medium text-gray-700 mb-1">CVV</label>
                        <input type="text" id="cvv" class="p-3 border rounded-md w-full focus:ring-[#b58863] focus:border-[#b58863]" placeholder="XXX" pattern="\d{3,4}" title="請輸入3或4位數字" disabled>
                    </div>
                </div>
            </div>
          </div>

          <div class="mt-2">
            <h4 class="text-sm font-medium text-gray-700 mb-1">配送時間</h4>
            <p class="text-sm text-gray-600">訂單確認後約 3-5 個工作天送達 (不含例假日)。</p>
          </div>

          <button type="submit" class="bg-[#3f2e2e] text-white px-6 py-3 rounded-md hover:bg-[#5a4444] transition-colors duration-300 text-lg font-semibold btn-press">確認下單</button>
        </form>

        <div id="thankYouMessage" class="text-center py-8 hidden">
          <h3 class="text-3xl font-bold text-[#b58863] mb-4">� 訂單已成立！感謝您的購買！ 🎉</h3>
          <p class="text-lg mb-2">您的訂單號碼為：<strong id="finalOrderId" class="text-[#3f2e2e]"></strong></p>
          <p class="text-md text-gray-700">我們將盡快為您處理訂單，請留意電話或信件通知。</p>
          <button onclick="closeCheckoutModal(true)" class="mt-8 bg-[#b58863] text-white px-8 py-3 rounded-md hover:bg-[#a07a5c] transition-colors duration-300 text-lg btn-press">繼續購物</button>
        </div>

      </div>
    </div>
  </body>
</html>

<script>
  // Global cart object
  let cart = {};
  // Review functions (add localStorage for persistence)
  let reviews = [];

  // Variables for floating cart visibility
  let lastScrollY = 0;
  const floatingCart = document.getElementById('floatingCart');

  // 會員相關變數
  let loggedInUser = null; // 儲存當前登入的使用者資訊
  let users = {}; // 模擬使用者資料庫 { email: { password, purchaseHistory: [], browsingHistory: [], loginCount } }
  const SHIPPING_FEE = 60; // 運費

  window.addEventListener('DOMContentLoaded', () => {
    const fadeSections = document.querySelectorAll('.fade-up');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    fadeSections.forEach(section => observer.observe(section));

    loadCart(); // Load cart from localStorage on page load
    loadUsers(); // 加載使用者資料
    checkLoginStatus(); // 檢查登入狀態
    updateCartBadge(); // 初始化購物車徽章數量
    renderProducts(); // Initial render of products
    renderCart(); // Initial render of main cart
    renderCartPanel(); // Initial render of side cart panel

    // Language button alert
    const langBtn = document.querySelector('button.underline');
    if (langBtn) {
      langBtn.addEventListener('click', () => {
        alert('目前僅提供繁體中文，English version 敬請期待！');
      });
    }

    // Category filter event listener
    const categoryFilter = document.getElementById('category');
    if (categoryFilter) {
      categoryFilter.addEventListener('change', () => renderProducts()); // 篩選時重新渲染商品
    }

    // Product search event listener
    const productSearchInput = document.getElementById('product-search');
    if (productSearchInput) {
        productSearchInput.addEventListener('input', () => renderProducts()); // 搜尋時重新渲染商品
    }

    // Checkout Form Submission Listener
    const checkoutForm = document.getElementById('checkoutForm');
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function(e) {
            e.preventDefault(); // 阻止表單預設提交行為

            const customerName = document.getElementById('customerName').value;
            const customerPhone = document.getElementById('customerPhone').value;
            const customerAddress = document.getElementById('customerAddress').value;
            const paymentMethod = document.querySelector('input[name="paymentMethod"]:checked').value;

            // 簡單的表單驗證
            if (!customerName || !customerPhone || !customerAddress) {
                alert('請填寫所有必填資訊！');
                return;
            }

            // 如果選擇信用卡，也模擬檢查這些欄位是否填寫（儘管沒有實際驗證）
            if (paymentMethod === 'creditCard') {
                const cardNumber = document.getElementById('cardNumber').value;
                const expiryDate = document.getElementById('expiryDate').value;
                const cvv = document.getElementById('cvv').value;
                if (!cardNumber || !expiryDate || !cvv) {
                    alert('請填寫完整的信用卡資訊！');
                    return;
                }
            }
            
            const subTotal = calculateCartTotal();
            const totalWithShipping = subTotal + SHIPPING_FEE;

            const orderId = generateOrderId();
            
            // 模擬訂單提交到後端
            const orderDetails = {
                orderId: orderId,
                customerInfo: {
                    name: customerName,
                    phone: customerPhone,
                    address: customerAddress
                },
                items: JSON.parse(JSON.stringify(cart)), // 深拷貝購物車內容
                subTotal: subTotal,
                shippingFee: SHIPPING_FEE,
                totalAmount: totalWithShipping,
                paymentMethod: paymentMethod,
                timestamp: new Date().toISOString()
            };

            console.log('模擬訂單已送出:', orderDetails);
            
            // 如果有會員登入，將訂單加入會員的購買紀錄
            if (loggedInUser) {
              users[loggedInUser.email].purchaseHistory.push(orderDetails);
              saveUsers();
            }

            // 在實際應用中，這裡會發送 AJAX 請求到後端 API

            // 顯示感謝訊息
            document.getElementById('checkoutForm').classList.add('hidden');
            document.getElementById('orderSummary').classList.add('hidden');
            document.getElementById('thankYouMessage').classList.remove('hidden');
            document.getElementById('finalOrderId').textContent = orderId;

            // 結帳成功後清空購物車（但由 closeModal 的 clearCartAfter 參數控制，此處不直接清空）
        });
    }

    // Initial load of reviews
    loadReviews();
    renderReviews();

    // Floating cart visibility on scroll
    window.addEventListener('scroll', () => {
        if (floatingCart) {
            if (window.scrollY > lastScrollY && window.scrollY > 100) { // Scrolling down and past initial 100px
                floatingCart.classList.add('hidden-scroll');
            } else { // Scrolling up
                floatingCart.classList.remove('hidden-scroll');
            }
            lastScrollY = window.scrollY;
        }
    });

    // 瀏覽紀錄：模擬點擊產品時記錄
    document.getElementById('product-cards').addEventListener('click', (event) => {
      const button = event.target.closest('button.btn-press');
      if (button) {
        const productName = button.getAttribute('onclick').match(/'([^']+)'/)[1];
        if (loggedInUser && productName) {
          const user = users[loggedInUser.email];
          // 避免重複記錄連續點擊
          if (user.browsingHistory.length === 0 || user.browsingHistory[user.browsingHistory.length - 1].productName !== productName) {
            user.browsingHistory.push({ productName, timestamp: new Date().toISOString() });
            saveUsers();
          }
        }
      }
    });

    // 會員登入/註冊表單提交
    document.getElementById('loginForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value;
      const password = document.getElementById('loginPassword').value;
      
      if (users[email] && users[email].password === password) {
        loggedInUser = { email: email };
        users[email].loginCount = (users[email].loginCount || 0) + 1; // 增加登入次數
        saveUsers();
        saveLoginStatus();
        updateMemberUI();
        closeMemberModal();
        alert('登入成功！');
      } else {
        alert('電子郵件或密碼錯誤。');
      }
    });

    document.getElementById('registerForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const email = document.getElementById('registerEmail').value;
      const password = document.getElementById('registerPassword').value;

      // 在這裡添加 Gmail 驗證
      const gmailPattern = /.+@gmail\.com$/;
      if (!gmailPattern.test(email)) {
          alert('請輸入有效的 Gmail 帳號 (例如: example@gmail.com)！');
          return;
      }

      if (users[email]) {
        alert('此電子郵件已被註冊。');
        return;
      }

      users[email] = {
        password: password,
        purchaseHistory: [],
        browsingHistory: [],
        loginCount: 0
      };
      saveUsers();
      alert('註冊成功！請登入。');
      showLoginForm();
    });
  });

  // 購物車徽章更新函數
  function updateCartBadge() {
      const cartBadge = document.getElementById('cart-badge');
      if (!cartBadge) return;
      let totalItems = 0;
      for (let item in cart) {
          totalItems += cart[item].qty;
      }
      cartBadge.textContent = totalItems;
      cartBadge.style.display = totalItems > 0 ? 'flex' : 'none'; // 有商品才顯示徽章
  }

  // 結帳彈窗相關函數
  function openCheckoutModal() {
    const modal = document.getElementById('checkoutModal');
    const modalContent = document.getElementById('checkoutModalContent');
    
    if (Object.keys(cart).length === 0) {
      alert('購物車是空的，請先加入商品！');
      return;
    }

    // 渲染購物車內容到彈窗
    const modalCartItems = document.getElementById('modalCartItems');
    const modalSubTotalAmount = document.getElementById('modalSubTotalAmount');
    const modalTotalAmount = document.getElementById('modalTotalAmount');
    
    modalCartItems.innerHTML = '';
    let subTotal = 0;

    for (let item in cart) {
      const { qty, price } = cart[item];
      const sub = qty * price;
      subTotal += sub;
      const itemDiv = document.createElement('div');
      itemDiv.className = 'flex justify-between items-center';
      itemDiv.innerHTML = `
        <span>${item} x ${qty}</span>
        <span>${formatPrice(sub)}</span>
      `;
      modalCartItems.appendChild(itemDiv);
    }
    modalSubTotalAmount.textContent = formatPrice(subTotal);
    modalTotalAmount.textContent = formatPrice(subTotal + SHIPPING_FEE); // 加上運費

    // 重置表單和隱藏感謝訊息
    document.getElementById('checkoutForm').reset();
    document.getElementById('checkoutForm').classList.remove('hidden');
    document.getElementById('orderSummary').classList.remove('hidden');
    document.getElementById('thankYouMessage').classList.add('hidden');
    
    // 預設將信用卡欄位隱藏並禁用
    document.getElementById('creditCardFields').classList.add('hidden');
    document.getElementById('cardNumber').disabled = true;
    document.getElementById('expiryDate').disabled = true;
    document.getElementById('cvv').disabled = true;

    // 顯示模態框並觸發動畫
    modal.classList.remove('hidden');
    setTimeout(() => {
      modalContent.classList.remove('scale-95', 'opacity-0');
      modalContent.classList.add('scale-100', 'opacity-100');
    }, 10); // 小延遲確保過渡效果
  }

  function closeCheckoutModal(clearCartAfter = false) {
    const modal = document.getElementById('checkoutModal');
    const modalContent = document.getElementById('checkoutModalContent');
    
    modalContent.classList.remove('scale-100', 'opacity-100');
    modalContent.classList.add('scale-95', 'opacity-0');

    setTimeout(() => {
      modal.classList.add('hidden');
      if (clearCartAfter) {
        cart = {};
        saveCart();
        renderCart();
        renderCartPanel();
        updateCartBadge(); // 清空購物車後更新徽章
      }
    }, 300); // 等待動畫結束後隱藏
  }

  // 修改原有的 checkout 函數，使其呼叫 openCheckoutModal
  window.checkout = function() {
    openCheckoutModal();
  };

  // 信用卡欄位顯示/隱藏控制
  window.toggleCreditCardFields = function(radio) {
      const creditCardFields = document.getElementById('creditCardFields');
      const cardNumber = document.getElementById('cardNumber');
      const expiryDate = document.getElementById('expiryDate');
      const cvv = document.getElementById('cvv');

      if (radio.value === 'creditCard') {
          creditCardFields.classList.remove('hidden');
          cardNumber.disabled = false;
          expiryDate.disabled = false;
          cvv.disabled = false;
          // 可以選擇在這裡將這些欄位設為 required，如果要求用戶必須填寫
          // cardNumber.required = true;
          // expiryDate.required = true;
          // cvv.required = true;
      } else {
          creditCardFields.classList.add('hidden');
          cardNumber.disabled = true;
          expiryDate.disabled = true;
          cvv.disabled = true;
          // cardNumber.required = false;
          // expiryDate.required = false;
          // cvv.required = false;
      }
  };


  function toggleCartPanel() {
    const panel = document.getElementById('cartPanel');
    panel.classList.toggle('translate-x-full');

    // 浮動購物車圖標點擊動畫
    const floatingCart = document.getElementById('floatingCart');
    floatingCart.classList.add('animate-pop'); // 添加一個臨時動畫類別
    setTimeout(() => {
        floatingCart.classList.remove('animate-pop'); // 移除類別以允許再次觸發
    }, 300); // 動畫持續時間
  }

  function renderCartPanel() {
    const panelBody = document.getElementById('cartPanelBody');
    const panelTotal = document.getElementById('panelTotal');
    if (!panelBody || !panelTotal) return; 

    panelBody.innerHTML = '';
    let total = 0;

    for (let item in cart) {
      const { qty, price } = cart[item];
      const sub = qty * price;
      total += sub;

      const div = document.createElement('div');
      div.className = 'border-b pb-2';
      div.innerHTML = `
        <div class="font-bold">${item}</div>
        <div class="text-sm text-gray-500">單價：${formatPrice(price)}</div>
        <div class="flex justify-between items-center mt-1">
          <button onclick="updateQty('${item}', -1); renderCart(); renderCartPanel();" class="px-2 bg-gray-200 rounded">➖</button>
          ${qty}
          <button onclick="updateQty('${item}', 1); renderCart(); renderCartPanel();" class="px-2 bg-gray-200 rounded">➕</button>
          <div class="text-right font-bold">${formatPrice(sub)}</div>
        </div>
      `;
      panelBody.appendChild(div);
    }
    panelTotal.textContent = formatPrice(total);
  }

  const products = [
    {
      name: 'GEISHA 水洗（114g）',
      country: '衣索比亞',
      variety: 'GEISHA 水洗',
      flavor: '接骨木花、茉莉花橙花、白玫瑰、百合花蘋果、野莓果醬、檸檬、百香果',
      roast: '淺焙',
      weight: '114g',
      expiry: '2025/10/12',
      price: 280,
      category: 'light',
      image: './image/image_1.png' 
    },
    {
      name: 'Heirloom 雙重厭氧（227g）- 批次A',
      country: '衣索比亞',
      variety: 'Heirloom',
      flavor: '茉莉、橙花、蜂蜜、水蜜桃',
      roast: '淺焙',
      weight: '227g',
      expiry: '2025/10/28',
      price: 600,
      category: 'light',
      image: './image/image_2.png'
    },
    {
      name: 'Heirloom 雙重厭氧（227g）- 批次B',
      country: '衣索比亞',
      variety: 'Heirloom',
      flavor: '茉莉、橙花、蜂蜜、水蜜桃',
      roast: '淺焙',
      weight: '227g',
      expiry: '2025/10/31',
      price: 600,
      category: 'light',
      image: './image/image_3.png'
    },
    {
      name: 'GEISHA（227g）中淺焙',
      country: '衣索比亞',
      variety: 'GEISHA',
      flavor: '接骨木花、茉莉花橙花、白玫瑰、百合花蘋果、野莓果醬、檸檬',
      roast: '中淺焙',
      weight: '227g',
      expiry: '2025/11/01',
      price: 540,
      category: 'medium',
      image: './image/image_4.png'
    },
    {
      name: 'GEISHA 水洗（227g）2280m',
      country: '衣索比亞',
      variety: 'GEISHA 水洗',
      flavor: '接骨木花、茉莉花橙花、白玫瑰、百合花蘋果、野莓果醬、檸檬',
      roast: '中淺焙',
      weight: '227g',
      expiry: '2025/11/01',
      price: 540,
      category: 'medium',
      image: './image/image_5.png'
    },
    {
      name: '衣索比亞 淺焙（227g）',
      country: '衣索比亞',
      variety: '',
      flavor: '接骨木花、茉莉花橙花、白玫瑰、百合花蘋果、野莓果醬、檸檬',
      roast: '淺焙',
      weight: '227g',
      expiry: '2025/11/01',
      price: 540,
      category: 'light',
      image: './image/image_6.png'
    },
    {
      name: '哥斯大黎加 Geisha 白蜜（114g）',
      country: '哥斯大黎加',
      variety: 'Geisha（藝妓）',
      flavor: '百合花、野薑花、檸檬草、柑橘、紅色莓果、蜂蜜',
      roast: '淺焙',
      weight: '114g',
      expiry: '2025/08/15',
      price: 800,
      category: 'light',
      image: './image/image_7.png'
    },
    {
      name: '哥斯大黎加 淺焙（227g）',
      country: '哥斯大黎加',
      variety: '',
      flavor: '百合花、野薑花、檸檬草、柑橘、紅色莓果、蜂蜜',
      roast: '淺焙',
      weight: '227g',
      expiry: '2025/08/15',
      price: 1800,
      category: 'light',
      image: './image/image_8.png'
    }
  ];

  function renderProducts() {
    const productContainer = document.getElementById('product-cards');
    const categoryFilter = document.getElementById('category').value;
    const searchTerm = document.getElementById('product-search').value.toLowerCase();
    
    if (!productContainer) return;
    productContainer.innerHTML = '';

    const filteredProducts = products.filter(p => {
        const matchesCategory = categoryFilter === 'all' || p.category === categoryFilter;
        const matchesSearch = p.name.toLowerCase().includes(searchTerm) || 
                              p.flavor.toLowerCase().includes(searchTerm) ||
                              p.country.toLowerCase().includes(searchTerm);
        return matchesCategory && matchesSearch;
    });

    if (filteredProducts.length === 0) {
        productContainer.innerHTML = '<p class="text-center col-span-full text-lg text-gray-600">抱歉，沒有找到符合條件的商品。</p>';
        return;
    }

    filteredProducts.forEach(p => {
      const card = document.createElement('div');
      card.className = 'ornate-box hover:scale-105 transition-transform duration-300';
      card.innerHTML = `
        <img src="${p.image}" alt="${p.name}" class="w-full h-48 object-cover rounded mb-3" />
        <h3 class="text-xl font-bold mb-1">${p.name}</h3>
        <p class="mb-1">國家：${p.country}｜品種：${p.variety}</p>
        <p class="mb-1">風味：${p.flavor}</p>
        <p class="mb-1">焙度：${p.roast}｜重量：${p.weight}</p>
        <p class="mb-1">期限：${p.expiry}</p>
        <p class="mb-2 font-bold">NT$${p.price}</p>
        <button class="bg-[#3f2e2e] text-white px-4 py-2 rounded btn-press" onclick="addToCart('${p.name}', ${p.price})">加入購物車</button>
      `;
      productContainer.appendChild(card);
    });
  }

  window.addToCart = function(name, price) {
    if (!cart[name]) cart[name] = { qty: 0, price };
    cart[name].qty++;
    saveCart(); 
    renderCart();
    renderCartPanel(); 
    updateCartBadge();
    
    const floatingCart = document.getElementById('floatingCart');
    floatingCart.classList.add('animate-pop');
    setTimeout(() => {
        floatingCart.classList.remove('animate-pop');
    }, 300); 
  }

  function formatPrice(n) {
    return `NT$${n.toLocaleString('zh-Hant-TW')}`;
  }

  window.updateQty = function(name, delta) {
    if (!cart[name]) return;
    cart[name].qty += delta;
    if (cart[name].qty <= 0) {
      delete cart[name];
    }
    saveCart(); 
    renderCart();
    renderCartPanel(); 
    updateCartBadge();
  }

  window.removeItem = function(name) {
    delete cart[name];
    saveCart(); 
    renderCart();
    renderCartPanel(); 
    updateCartBadge();
  }

  function renderCart() {
    const tbody = document.getElementById('cart-body');
    if (!tbody) return;
    tbody.innerHTML = '';
    let total = 0;

    for (let item in cart) {
      const tr = document.createElement('tr');
      const { qty, price } = cart[item];
      const sub = qty * price;
      total += sub;

      tr.innerHTML = `
        <td class="border p-2">${item}</td>
        <td class="border p-2 flex items-center gap-2">
          <button onclick="updateQty('${item}', -1)" class="px-2 bg-gray-200 rounded">➖</button>
          ${qty}
          <button onclick="updateQty('${item}', 1)" class="px-2 bg-gray-200 rounded">➕</button>
        </td>
        <td class="border p-2">${formatPrice(price)}</td>
        <td class="border p-2 flex justify-between items-center">
          ${formatPrice(sub)}
          <button onclick="removeItem('${item}')" class="ml-4 text-red-500">🗑️</button>
        </td>
      `;
      tbody.appendChild(tr);
    }

    const totalElem = document.getElementById('total-amount');
    if (totalElem) totalElem.textContent = formatPrice(total);
  }

  // Save cart to Local Storage
  function saveCart() {
    localStorage.setItem('melodyBeansCart', JSON.stringify(cart));
    // 如果用戶已登入，也更新其購物車綁定
    if (loggedInUser) {
        users[loggedInUser.email].cart = JSON.parse(JSON.stringify(cart));
        saveUsers();
    }
  }

  // Load cart from Local Storage
  function loadCart() {
    const storedCart = localStorage.getItem('melodyBeansCart');
    if (storedCart) {
      cart = JSON.parse(storedCart);
    }
  }

  // Review functions (add localStorage for persistence)
  function loadReviews() {
    const storedReviews = localStorage.getItem('melodyBeansReviews');
    if (storedReviews) {
      reviews = JSON.parse(storedReviews);
    }
  }

  function saveReviews() {
    localStorage.setItem('melodyBeansReviews', JSON.stringify(reviews));
  }

  window.submitReview = function(e) {
    e.preventDefault();
    const name = document.getElementById('reviewer').value;
    const content = document.getElementById('review-content').value;
    const rating = document.getElementById('review-rating').value;
    
    reviews.push({ name, content, rating, timestamp: new Date().toISOString() });
    saveReviews();
    renderReviews();
    e.target.reset();
  }
 
  function renderReviews() {
    const reviewList = document.getElementById('review-list');
    if (!reviewList) return;
    reviewList.innerHTML = ''; 
    reviews.slice().reverse().forEach(review => {
      const div = document.createElement('div');
      div.className = 'p-4 border rounded shadow bg-white'; 
      div.innerHTML = `<strong>${review.name} ${review.rating}</strong><p class="mt-1">${review.content}</p>`;
      reviewList.appendChild(div);
    });
  }
  
  function generateOrderId() {
    const now = new Date();
    return `ORD-${now.getFullYear()}${(now.getMonth()+1).toString().padStart(2,'0')}${now.getDate().toString().padStart(2,'0')}${now.getHours().toString().padStart(2,'0')}${now.getMinutes().toString().padStart(2,'0')}${now.getSeconds().toString().padStart(2,'0')}`;
  }

  // 計算購物車總金額的輔助函數
  function calculateCartTotal() {
      let total = 0;
      for (let item in cart) {
          total += cart[item].qty * cart[item].price;
      }
      return total;
  }

  // Function to close mobile menu when a nav link is clicked
  window.closeMenu = function() {
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
      mobileMenu.classList.add('hidden');
    }
  };

  // Toggle mobile menu for the hamburger icon (on DOMContentLoaded)
  document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.getElementById('menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuButton && mobileMenu) {
      menuButton.addEventListener('click', function() {
        mobileMenu.classList.toggle('hidden');
      });
    }
  });

  // 會員模態框相關函數
  function openMemberModal() {
    const modal = document.getElementById('memberModal');
    const modalContent = document.getElementById('memberModalContent');
    
    // 重置為登入介面
    showLoginForm();
    hidePurchaseHistory();

    // 顯示模態框並觸發動畫
    modal.classList.remove('hidden');
    setTimeout(() => {
      modalContent.classList.remove('scale-95', 'opacity-0');
      modalContent.classList.add('scale-100', 'opacity-100');
    }, 10);
  }

  function closeMemberModal() {
    const modal = document.getElementById('memberModal');
    const modalContent = document.getElementById('memberModalContent');
    
    modalContent.classList.remove('scale-100', 'opacity-100');
    modalContent.classList.add('scale-95', 'opacity-0');

    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
  }

  function showLoginForm() {
    document.getElementById('loginSection').classList.remove('hidden');
    document.getElementById('registerSection').classList.add('hidden');
    document.getElementById('memberInfo').classList.add('hidden');
    document.getElementById('loginForm').reset(); // 清空表單
  }

  function showRegisterForm() {
    document.getElementById('loginSection').classList.add('hidden');
    document.getElementById('registerSection').classList.remove('hidden');
    document.getElementById('memberInfo').classList.add('hidden');
    document.getElementById('registerForm').reset(); // 清空表單
  }

  function updateMemberUI() {
    const memberLink = document.getElementById('memberLink');
    const loggedInUserEmail = document.getElementById('loggedInUserEmail');
    const loginSection = document.getElementById('loginSection');
    const registerSection = document.getElementById('registerSection');
    const memberInfo = document.getElementById('memberInfo');

    if (loggedInUser) {
      memberLink.textContent = `歡迎 ${loggedInUser.email.split('@')[0]}！`;
      memberLink.onclick = () => { openMemberModal(); return false; }; // 點擊顯示會員資訊
      loggedInUserEmail.textContent = loggedInUser.email;
      loginSection.classList.add('hidden');
      registerSection.classList.add('hidden');
      memberInfo.classList.remove('hidden');

      // 檢查是否有儲存的購物車，並與會員購物車同步
      const userCart = users[loggedInUser.email].cart || {};
      if (Object.keys(userCart).length > 0 && Object.keys(cart).length === 0) {
          cart = userCart;
          saveCart(); // 更新本地儲存
          renderCart();
          renderCartPanel();
          updateCartBadge();
      } else if (Object.keys(cart).length > 0 && JSON.stringify(cart) !== JSON.stringify(userCart)) {
          // 如果本地購物車有內容且與會員購物車不同，以本地為準並更新會員購物車
          users[loggedInUser.email].cart = JSON.parse(JSON.stringify(cart));
          saveUsers();
      }
      
    } else {
      memberLink.textContent = '會員登入/註冊';
      memberLink.onclick = () => { openMemberModal(); return false; };
      loggedInUserEmail.textContent = '';
      loginSection.classList.remove('hidden');
      registerSection.classList.add('hidden');
      memberInfo.classList.add('hidden');
      // 登出後，清空購物車，但保留本地 localStorage 的內容，下次登入前可恢復
      // cart = {}; // 如果登出需要清空購物車，則啟用此行
      // saveCart(); // 儲存清空後的購物車
      // renderCart();
      // renderCartPanel();
      // updateCartBadge();
    }
  }

  function saveUsers() {
    localStorage.setItem('melodyBeansUsers', JSON.stringify(users));
  }

  function loadUsers() {
    const storedUsers = localStorage.getItem('melodyBeansUsers');
    if (storedUsers) {
      users = JSON.parse(storedUsers);
    }
  }

  function saveLoginStatus() {
    if (loggedInUser) {
      sessionStorage.setItem('melodyBeansLoggedInUser', JSON.stringify(loggedInUser));
    } else {
      sessionStorage.removeItem('melodyBeansLoggedInUser');
    }
  }

  function checkLoginStatus() {
    const storedLogin = sessionStorage.getItem('melodyBeansLoggedInUser');
    if (storedLogin) {
      loggedInUser = JSON.parse(storedLogin);
      updateMemberUI();
    }
  }

  window.logout = function() {
    loggedInUser = null;
    saveLoginStatus();
    updateMemberUI();
    closeMemberModal();
    alert('您已登出！');
  }

  window.viewPurchaseHistory = function() {
    if (!loggedInUser) {
      alert('請先登入以查看購買紀錄。');
      return;
    }

    const historyList = document.getElementById('purchaseHistoryList');
    historyList.innerHTML = '';
    const user = users[loggedInUser.email];

    if (user && user.purchaseHistory.length > 0) {
      user.purchaseHistory.slice().reverse().forEach(order => {
        const orderDiv = document.createElement('div');
        orderDiv.className = 'border p-3 rounded-md bg-white shadow-sm';
        
        let itemsHtml = '';
        for (const itemName in order.items) {
            const item = order.items[itemName];
            itemsHtml += `<li>${itemName} x ${item.qty} (NT$${item.price})</li>`;
        }

        orderDiv.innerHTML = `
          <p class="font-bold">訂單號碼: ${order.orderId}</p>
          <p class="text-sm text-gray-600">日期: ${new Date(order.timestamp).toLocaleString()}</p>
          <p class="mt-2 font-semibold">商品清單:</p>
          <ul class="list-disc list-inside text-sm ml-4">${itemsHtml}</ul>
          <p class="text-right font-semibold mt-2">總金額: ${formatPrice(order.totalAmount)}</p>
          <p class="text-right text-xs text-gray-500">付款方式: ${order.paymentMethod === 'cashOnDelivery' ? '貨到付款' : '信用卡(模擬)'}</p>
        `;
        historyList.appendChild(orderDiv);
      });
    } else {
      historyList.innerHTML = '<p class="text-center text-gray-600">您目前沒有任何購買紀錄。</p>';
    }

    document.getElementById('memberInfo').classList.add('hidden');
    document.getElementById('purchaseHistorySection').classList.remove('hidden');
  }

  window.hidePurchaseHistory = function() {
    document.getElementById('purchaseHistorySection').classList.add('hidden');
    document.getElementById('memberInfo').classList.remove('hidden');
  }

  // 輔助函數：記錄瀏覽紀錄（可以放在 addToCart 或產品卡片點擊事件中）
  function recordBrowsingHistory(productName) {
    if (loggedInUser) {
      const user = users[loggedInUser.email];
      user.browsingHistory.push({ productName, timestamp: new Date().toISOString() });
      saveUsers();
      // console.log(`已記錄 ${loggedInUser.email} 瀏覽了 ${productName}`);
    }
  }

</script>
�
