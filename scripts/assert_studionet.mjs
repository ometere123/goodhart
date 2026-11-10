import { readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const pkg = JSON.parse(readFileSync(new URL('../package.json', import.meta.url)));
if (pkg.devDependencies.genlayer !== '0.39.1') {
  throw new Error('Expected exact repository-local GenLayer CLI 0.39.1');
}
const cli = process.platform === 'win32'
  ? new URL('../node_modules/.bin/genlayer.cmd', import.meta.url)
  : new URL('../node_modules/.bin/genlayer', import.meta.url);
const cliVersion = execFileSync(fileURLToPath(cli), ['--version'], {
  encoding: 'utf8',
  shell: process.platform === 'win32',
}).trim();
if (cliVersion !== '0.39.1') {
  throw new Error(`Wrong repository-local GenLayer CLI: ${cliVersion}`);
}
for (const [key, wanted] of Object.entries({
  GENLAYER_NETWORK: 'studionet',
  GENLAYER_CHAIN_ID: '61999',
  GENLAYER_RPC: 'https://studio.genlayer.com/api',
})) {
  if (process.env[key] && process.env[key] !== wanted) {
    throw new Error(`Refusing ${key}=${process.env[key]}; expected ${wanted}`);
  }
}

const rpc = 'https://studio.genlayer.com/api';
const response = await fetch(rpc, {
  method: 'POST',
  headers: { 'content-type': 'application/json' },
  body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'eth_chainId', params: [] }),
  signal: AbortSignal.timeout(12000),
});
if (!response.ok) throw new Error(`RPC HTTP ${response.status}`);
const data = await response.json();
const chainId = Number.parseInt(data.result, 16);
if (chainId !== 61999) throw new Error(`Wrong chain ID ${String(data.result)}`);
console.log('Confirmed: studionet, chain 61999, RPC https://studio.genlayer.com/api, CLI 0.39.1');
