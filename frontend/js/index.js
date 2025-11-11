// index.js - carga y muestra videojuegos, permite crear

async function renderCelulares(){
  const list = document.getElementById('celulares-list');
  list.innerHTML = '<p class="small">Cargando...</p>';
  try{
    const celulares = await window.__api.getCelulares();
    if(!celulares || celulares.length === 0){
      list.innerHTML = '<p class="small">No hay celulares aún.</p>';
      return;
    }
    list.innerHTML = '';
    celulares.forEach(c => {
      const card = document.createElement('div');
      card.className = 'game-card';
      card.innerHTML = `<h3>${escapeHtml(c.modelo)}</h3>
        <p>Precio: $${c.precio}</p>
        <p class="small">Marca: ${c.marca_id}</p>
        <div style="margin-top:8px">
          <button data-id="${c.id}" class="btn-edit">Editar</button>
          <button data-id="${c.id}" class="btn-delete">Eliminar</button>
        </div>`;
      list.appendChild(card);
    });
  }catch(err){
    list.innerHTML = `<p class="small">Error al cargar celulares: ${err.message}</p>`;
  }
}

function escapeHtml(s){ if(!s) return ''; return String(s).replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;"})[c]); }

document.getElementById('add-celular-form').addEventListener('submit', async (e)=>{
  e.preventDefault();
  const f = e.target;
  const data = {
    modelo: f.modelo.value,
    precio: parseFloat(f.precio.value),
    marca_id: parseInt(f.marca_id.value)
  };
  try{
    await window.__api.createCelular(data);
    f.reset();
    await renderCelulares();
  }catch(err){
    alert('Error creando: ' + (err.body?.error || err.message));
  }
});


// Delegación para editar/eliminar
document.getElementById('games-list').addEventListener('click', async (e)=>{
  const id = e.target.getAttribute('data-id');
  if(!id) return;
  if(e.target.classList.contains('btn-delete')){
    if(!confirm('¿Eliminar este videojuego?')) return;
    try{ await window.__api.deleteGame(id); await renderCelulares()(); }catch(err){ alert('Error al eliminar: '+err.message); }
  }
  if(e.target.classList.contains('btn-edit')){
    const newTitle = prompt('Nuevo título');
    if(newTitle==null) return;
    try{ await window.__api.updateGame(id,{titulo:newTitle}); await renderCelulares()(); }catch(err){ alert('Error al editar: '+err.message); }
  }
});

// Inicializar
renderCelulares()();
