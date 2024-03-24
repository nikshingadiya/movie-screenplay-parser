import express from 'express';
import { Fountain } from 'fountain-js';

const app = express();
const PORT = process.env.PORT || 8016;

async function parseScript(script) {
    try {
        if (!script) throw new Error("Script data not provided.");

        const fountain = new Fountain();
        const output = fountain.parse(script);

        // Optionally, you can access tokens or other properties of the Fountain object here
        const fountainData = {
            tokens: fountain.tokens
        };

        return fountainData;
    } catch (error) {
        throw error;
    }
}

app.use(express.json());

app.post('/parseScript', async (req, res) => {
    const { script } = req.body;
    if (!script) {
        return res.status(400).json({ error: "Script data not provided." });
    }

    try {
        const result = await parseScript(script);
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
