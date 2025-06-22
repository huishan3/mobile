 <script>
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

const products = [
  {
    name: '淺焙日曬（Violin Blend）',
    country: '哥倫比亞',
    variety: '卡杜拉',
    flavor: '莓果、花香',
    weight: '200g',
    roast: '淺焙',
    expiry: '2025/09/15',
    price: 350,
    category: 'light',
    image: 'https://source.unsplash.com/featured/?light,coffee'
  }
];



      const productContainer = document.getElementById('product-cards');
      const categoryFilter = document.getElementById('category');
      const cart = {};

      function renderProducts(filter = 'all') {
        productContainer.innerHTML = '';
        products.filter(p => filter === 'all' || p.category === filter).forEach(p => {
          const card = document.createElement('div');
          card.className = 'ornate-box hover:scale-105 transition-transform duration-300';

          card.innerHTML = `
          <img src="${p.image}" alt="${p.name}" class="w-full h-48 object-cover rounded mb-3"/>
          <h3 class="text-xl font-bold mb-1">${p.name}</h3>
          <p class="mb-1">國家：${p.country}｜品種：${p.variety}</p>
          <p class="mb-1">風味：${p.flavor}</p>
          <p class="mb-1">焙度：${p.roast}｜重量：${p.weight}</p>
          <p class="mb-1">期限：${p.expiry}</p>
          <p class="mb-2 font-bold">NT$${p.price}</p>
          <button class="bg-[#3f2e2e] text-white px-4 py-2 rounded" onclick="addToCart('${p.name}', ${p.price})">加入購物車</button>
`;


      

      function addToCart(name, price) {
        if (!cart[name]) cart[name] = { qty: 0, price };
        cart[name].qty++;
        renderCart();
      }

      function formatPrice(n) {
        return `NT$${n.toLocaleString('zh-Hant-TW')}`;
      }
      
      function updateQty(name, delta) {
        if (!cart[name]) return;
        cart[name].qty += delta;
        if (cart[name].qty <= 0) {
          delete cart[name];
        }
        renderCart();
      }
      
      function removeItem(name) {
        delete cart[name];
        renderCart();
      }
      
      function renderCart() {
        const tbody = document.getElementById('cart-body');
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
      
        document.getElementById('total-amount').textContent = formatPrice(total);
      }

      function removeItem(name) {
        delete cart[name];
        renderCart();
      }
      
      function updateQty(name, delta) {
        if (!cart[name]) return;
        cart[name].qty += delta;
        if (cart[name].qty <= 0) {
          delete cart[name];
        }
        renderCart();
      }      
      

      function submitReview(e) {
        e.preventDefault();
        const name = document.getElementById('reviewer').value;
        const content = document.getElementById('review-content').value;
        const reviewList = document.getElementById('review-list');
        const div = document.createElement('div');
        div.className = 'p-4 border rounded shadow';
        div.innerHTML = `<strong>${name}</strong><p class="mt-1">${content}</p>`;
        reviewList.prepend(div);
        e.target.reset();
      }

      function generateOrderId() {
  const now = new Date();
  return `ORD-${now.getFullYear()}${(now.getMonth() + 1).toString().padStart(2, '0')}${now.getDate().toString().padStart(2, '0')}${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;
}





function checkout() {
  if (Object.keys(cart).length === 0) return alert('購物車是空的！');
  submitOrder();
}
categoryFilter.addEventListener('change', e => renderProducts(e.target.value));
      renderProducts();
    </script>