// Start Docusaurus and open MS-Communications test page
const { spawn } = require('child_process');
const http = require('http');
const { exec } = require('child_process');

const PORT = process.env.PORT || 3000;
const TEST_URL = 'http://localhost:' + PORT + '/docs/guru-card-contents/MS-Communications';

function waitForServer(maxAttempts, intervalMs) {
  maxAttempts = maxAttempts || 60;
  intervalMs = intervalMs || 1000;
  return new Promise((resolve, reject) => {
    let attempts = 0;
    function tryConnect() {
      const req = http.get('http://localhost:' + PORT, (res) => { resolve(); });
      req.on('error', () => {
        attempts++;
        if (attempts >= maxAttempts) return reject(new Error('Server did not start in time'));
        setTimeout(tryConnect, intervalMs);
      });
    }
    tryConnect();
  });
}

function openUrl(url) {
  let cmd;
  if (process.platform === 'win32') cmd = 'start "" "' + url + '"';
  else if (process.platform === 'darwin') cmd = 'open "' + url + '"';
  else cmd = 'xdg-open "' + url + '"';
  exec(cmd, (err) => {
    if (err) console.warn('Could not open browser:', err.message);
    else console.log('Opened', url);
  });
}

spawn('npx', ['docusaurus', 'start', '--port', String(PORT)], {
  stdio: 'inherit',
  shell: true,
  env: Object.assign({}, process.env, { PORT: String(PORT) }),
});

console.log('Waiting for server at http://localhost:' + PORT + ' ...');
waitForServer().then(() => openUrl(TEST_URL)).catch((e) => console.error(e.message));
