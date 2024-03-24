import fs from 'fs';
import { Fountain } from 'fountain-js';

async function readScriptFromFile(filePath) {
    try {
        const data = await fs.promises.readFile(filePath, 'utf8');
        return data;
    } catch (error) {
        console.error("Error reading file:", error);
        return null;
    }
}

async function parseScript(filePath) {
    const script = await readScriptFromFile(filePath);
    if (!script) return;

    const fountain = new Fountain();
    const output = fountain.parse(script);

    // Optionally, you can access tokens or other properties of the Fountain object here
    const fountainData = {
        script: output.html.script,
        tokens: fountain.tokens
    };

    const folder_path = "./jsonfile";

    const jsonOutput = JSON.stringify(fountaainData, null, 2);
    const jsonFilePath = folder_path + filePath.replace("./fountain_file", "").replace('.fountain', '.json');

    fs.writeFile(jsonFilePath, jsonOutput, 'utf8', (err) => {
        if (err) {
            console.error("Error writing JSON file:", err);
        } else {
            console.log("JSON file saved successfully:", jsonFilePath);
        }
    });
}

// Parsing command line arguments
const args = process.argv.slice(2);
if (args.length !== 1) {
    console.error("Usage: node script_name.js <script_file_path>");
    process.exit(1);
}

const filePath = args[0];
parseScript(filePath);
