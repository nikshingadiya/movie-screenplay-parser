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
    
    const jsonOutput = JSON.stringify(fountainData, null, 2);
    const jsonFilePath = filePath.replace('.fountain', '.json');

    fs.writeFile(jsonFilePath, jsonOutput, 'utf8', (err) => {
        if (err) {
            console.error("Error writing JSON file:", err);
        } else {
            console.log("JSON file saved successfully:", jsonFilePath);
        }
    });
}

const filePath = 'brick.fountain'; // Update with your script file path
parseScript(filePath);
