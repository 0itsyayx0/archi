// api.js - funciones para comunicarse con el backend
// Preferir `window.API_BASE` si está definida (se puede fijar desde el HTML).
// Por defecto usar el backend de desarrollo en localhost:5000.
// Esto evita enviar peticiones al servidor estático (ej. Live Server) por error.
const API_BASE = window.API_BASE || 'http://localhost:5000';

async function request(path, opts={}){
  const headers = opts.headers || {};
  const token = localStorage.getItem('token');
  if(token){ headers['Authorization'] = 'Bearer ' + token; }
  headers['Content-Type'] = headers['Content-Type'] || 'application/json';

  const res = await fetch(API_BASE + path, {...opts, headers});
  let body = null;
  let text = null; 
  try{ body = await res.json(); }catch(e){
    // respuesta no-JSON (por ejemplo un 404 HTML del servidor estático)
    try{ text = await res.text(); }catch(e2){ text = null; }
  }
  if(!res.ok){
    const errMsg = (body && (body.message || body.error)) || text || 'Error en la petición';
    const err = new Error(errMsg);
    err.status = res.status; err.body = body;
    throw err;
  }
  // devolver JSON cuando exista, o texto plano si no
  return body !== null ? body : text;
}

// Autenticación
async function login(email, password){
  return request('/auth/login', {method:'POST', body: JSON.stringify({email,password})});
}

async function registerUser(username, email, password){
  return request('/auth/register', {method:'POST', body: JSON.stringify({username,email,password})});
}

async function logout(){
  localStorage.removeItem('token');
}

// Celulares
async function getCelulares(){
  return request('/celulares', {method:'GET'});
}

async function createCelular(payload){
  return request('/celulares/', {method:'POST', body: JSON.stringify(payload)});
}

async function updateCelular(id, payload){
  return request(`/celulares/${id}`, {method:'PUT', body: JSON.stringify(payload)});
}

async function deleteCelular(id){
  return request(`/celulares/${id}`, {method:'DELETE'});
}

window.__api = {
  getCelulares, createCelular, updateCelular, deleteCelular,
  login, registerUser, logout
};
