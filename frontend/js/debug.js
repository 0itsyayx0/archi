// debug.js - Diagnóstico para debugging en desarrollo
(function(){
  console.log('%c🔍 PhoneStore Debug Mode', 'color: #0066cc; font-size: 16px; font-weight: bold');
  
  const apiBase = window.API_BASE || 'http://localhost:5000';
  console.log(`%cAPI_BASE: ${apiBase}`, 'color: #009900; font-size: 12px');
  console.log(`%cToken: ${localStorage.getItem('token') ? '✓ Presente' : '✗ No presente'}`, 'color: #009900; font-size: 12px');
  
  // Test backend connectivity
  fetch(apiBase + '/celulares', {method: 'GET'})
    .then(r => {
      console.log(`%c✓ Backend accesible (status: ${r.status})`, 'color: #00aa00; font-size: 12px');
      if(!r.ok) console.warn(`⚠ Status ${r.status} - algunos endpoints pueden no estar disponibles`);
    })
    .catch(e => {
      const msg = `✗ No se puede conectar al backend en ${apiBase}. Asegúrate de ejecutar: python app_factory.py`;
      console.error(`%c${msg}`, 'color: #cc0000; font-size: 12px');
    });
  
  // Helper para ver usuarios desde consola
  window.debugGetUsers = async function() {
    try {
      const res = await fetch(apiBase + '/debug/users');
      const users = await res.json();
      console.table(users);
    } catch(e) {
      console.error('Error:', e.message);
    }
  };
  
  console.log('%cComandos disponibles en consola:', 'color: #0066cc; font-weight: bold');
  console.log('  debugGetUsers()  - Lista usuarios registrados');
  console.log('  localStorage.getItem("token")  - Ver token actual');
  console.log('  window.API_BASE  - Ver base de API');
})();
