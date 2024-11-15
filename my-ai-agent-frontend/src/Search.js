// src/Search.js
import React, { useState } from 'react';
import axios from 'axios';

const Search = ({ entities }) => {
    const [entity, setEntity] = useState('');
    const [prompt, setPrompt] = useState('');
    const [results, setResults] = useState(null);

    const handleSearch = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/search', {
                entity,
                prompt,
            });
            setResults(response.data);
        } catch (error) {
            console.error('Error performing search:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSearch}>
                <input
                    type="text"
                    value={entity}
                    onChange={(e) => setEntity(e.target.value)}
                    placeholder="Enter entity"
                />
                <input
                    type="text"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="Enter prompt"
                />
                <button type="submit">Search</button>
            </form>
            {results && (
                <div>
                    <h2>Search Results</h2>
                    <pre>{JSON.stringify(results, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default Search;