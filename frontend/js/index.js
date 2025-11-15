// index.js - carga y muestra celulares, permite crear

async function renderCelulares(){
  const list = document.getElementById('celulares-list');
  list.innerHTML = '<p class="small" style="grid-column:1/-1;text-align:center">Cargando celulares...</p>';
  try{
    const celulares = await window.__api.getCelulares();
    console.log('Celulares cargados:', celulares);
    if(!celulares || celulares.length === 0){
      list.innerHTML = '<p class="small" style="grid-column:1/-1;text-align:center">No hay celulares aún. ¡Agrega uno arriba!</p>';
      return;
    }
    renderPhoneCards(celulares, list);
  }catch(err){
    console.error('Error al cargar celulares:', err);
    list.innerHTML = `<p class="small" style="grid-column:1/-1;text-align:center;color:#ff9999">Error al conectar con el servidor. Agrega celulares desde el formulario arriba.</p>`;
  }
}

function renderPhoneCards(celulares, list){
  list.innerHTML = '';
  celulares.forEach(c => {
    const card = document.createElement('div');
    card.className = 'game-card';
    const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7', '#dfe6e9', '#a29bfe', '#fd79a8', '#55efc4', '#74b9ff'];
    const bgColor = colors[c.marca_id % colors.length];
    card.innerHTML = `
      <div class="game-card-image">
        <div style="width:100%;height:100%;background:linear-gradient(135deg,${bgColor},${bgColor}dd);display:flex;align-items:center;justify-content:center;font-size:48px;color:rgba(255,255,255,0.7)">
          📱
        </div>
      </div>
      <div class="game-card-content">
        <div>
          <h3>${escapeHtml(c.modelo)}</h3>
          <p class="small">Marca: ${c.marca_nombre || 'Sin marca'}</p>
          <p class="price">$${c.precio}</p>
        </div>
        <div class="game-card-buttons">
          <button data-id="${c.id}" class="btn-edit">Editar</button>
          <button data-id="${c.id}" class="btn-delete">Eliminar</button>
        </div>
      </div>
    `;
    list.appendChild(card);
  });
}

function escapeHtml(s){ if(!s) return ''; return String(s).replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;"})[c]); }

// --- Autenticación inline en index.html ---
function updateAuthUI(){
  const token = localStorage.getItem('token');
  const userInfo = document.getElementById('user-info');
  const authForms = document.getElementById('auth-forms');
  const welcome = document.getElementById('welcome');
  if(!userInfo || !authForms) return;
  if(token){
    userInfo.style.display = 'inline-block';
    authForms.style.display = 'none';
    const username = localStorage.getItem('username');
    if(welcome && username) welcome.textContent = `Conectado: ${username}`;
  }else{
    userInfo.style.display = 'none';
    authForms.style.display = 'inline-block';
  }
}

// Login inline
const inlineLogin = document.getElementById('inline-login-form');
if(inlineLogin){
  inlineLogin.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const f = e.target;
    const email = f.email.value;
    const password = f.password.value;
    try{
      const res = await window.__api.login(email,password);
      if(res.token){
        localStorage.setItem('token', res.token);
        if(res.username) localStorage.setItem('username', res.username);
        updateAuthUI();
        await renderCelulares();
        alert('Login correcto');
      }else{
        alert('Login correcto pero no se recibió token.');
      }
    }catch(err){
      alert('Error en login: ' + (err.body?.error || err.message));
    }
  });
}

// Register inline
const inlineReg = document.getElementById('inline-register-form');
if(inlineReg){
  inlineReg.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const f = e.target;
    const username = f.username.value;
    const email = f.email.value;
    const password = f.password.value;
    try{
      const res = await window.__api.registerUser(username,email,password);
      if(res.token){
        localStorage.setItem('token', res.token);
        if(res.username) localStorage.setItem('username', res.username);
        updateAuthUI();
        await renderCelulares();
        alert('Registro correcto y sesión iniciada');
      }else{
        alert('Registro completado. Puedes iniciar sesión.');
      }
    }catch(err){
      alert('Error al registrar: ' + (err.body?.error || err.message));
    }
  });
}

// Logout
const logoutBtn = document.getElementById('logout-btn');
if(logoutBtn){
  logoutBtn.addEventListener('click', (e)=>{
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    updateAuthUI();
  });
}

document.getElementById('add-celular-form').addEventListener('submit', async (e)=>{
  e.preventDefault();
  const f = e.target;
  const data = {
    modelo: f.modelo.value,
    precio: parseFloat(f.precio.value),
    marca_id: parseInt(f.marca_id.value)
  };
  console.log('Creando celular:', data);
  try{
    const res = await window.__api.createCelular(data);
    console.log('Respuesta:', res);
    f.reset();
    await renderCelulares();
  }catch(err){
    console.error('Error:', err);
    alert('Error creando: ' + (err.body?.error || err.message));
  }
});


// Delegación para editar/eliminar
document.getElementById('celulares-list').addEventListener('click', async (e)=>{
  const id = e.target.getAttribute('data-id');
  if(!id) return;
  if(e.target.classList.contains('btn-delete')){
    if(!confirm('¿Eliminar este celular?')) return;
    try{ await window.__api.deleteCelular(id); await renderCelulares(); }catch(err){ alert('Error al eliminar: '+err.message); }
  }
  if(e.target.classList.contains('btn-edit')){
    const newModelo = prompt('Nuevo modelo');
    if(newModelo==null) return;
    const newPrecio = prompt('Nuevo precio');
    if(newPrecio==null) return;
    const newMarcaId = prompt('Nuevo marca_id');
    if(newMarcaId==null) return;
    try{ await window.__api.updateCelular(id,{modelo:newModelo, precio:parseFloat(newPrecio), marca_id:parseInt(newMarcaId)}); await renderCelulares(); }catch(err){ alert('Error al editar: '+err.message); }
  }
});

// Inicializar
updateAuthUI();
renderCelulares();
