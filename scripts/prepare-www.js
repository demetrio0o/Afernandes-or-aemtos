// Copia jsPDF e as fontes de node_modules para www/vendor, para o app funcionar 100% offline.
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const nm = (...p) => path.join(root, 'node_modules', ...p);
const out = path.join(root, 'www', 'vendor');

function copy(from, to) {
  if (!fs.existsSync(from)) { console.error('Arquivo não encontrado: ' + from + '\nRode "npm install" antes.'); process.exit(1); }
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.cpSync(from, to, { recursive: true });
}

fs.rmSync(out, { recursive: true, force: true });
copy(nm('jspdf', 'dist', 'jspdf.umd.min.js'), path.join(out, 'jspdf.umd.min.js'));
copy(nm('jspdf-autotable', 'dist', 'jspdf.plugin.autotable.min.js'), path.join(out, 'jspdf.plugin.autotable.min.js'));
copy(nm('@fontsource-variable', 'montserrat', 'index.css'), path.join(out, 'fonts', 'montserrat', 'index.css'));
copy(nm('@fontsource-variable', 'montserrat', 'files'), path.join(out, 'fonts', 'montserrat', 'files'));
copy(nm('@fontsource-variable', 'public-sans', 'index.css'), path.join(out, 'fonts', 'public-sans', 'index.css'));
copy(nm('@fontsource-variable', 'public-sans', 'files'), path.join(out, 'fonts', 'public-sans', 'files'));
console.log('www/vendor pronto.');
