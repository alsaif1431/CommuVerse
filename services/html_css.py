card_css = """
    <style>
        .card-button {
            background-color: #f0f2f6;
            color: #333;
            width: 100%;
            height: 220px;
            border-radius: 10px;
            padding: 15px;
            margin: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            transition: transform 0.3s, background-color 0.3s;
            cursor: pointer;
            border: none;
            font-size: 18px;
        }
        .card-button:hover {
            transform: translateY(-5px);
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.25);
            background-color: #e1e5ea;
        }
        .card-button h3 {
            color: #1f77b4;
            margin-bottom: 10px;
            font-size: 22px;
        }
        .card-button p {
            color: #4a4a4a;
            font-size: 15px;
        }

        /* Dark mode adjustments */
        @media (prefers-color-scheme: dark) {
            .card-button {
                background-color: #1e1e1e;
                color: #f0f2f6;
            }
            .card-button:hover {
                background-color: #333;
                color: #ffffff;
            }
            .card-button h3 {
                color: #A855F7;
            }
            .card-button p {
                color: #d1d5db;
            }
        }
    </style>
    """

tag_line_css = """
        <div style="text-align: center; padding: 20px; margin-top: 10px;">
            <h1 style="color: #1f77b4; font-size: 36px; font-weight: bold;">
                Explore Vibrant Communities 🌐
            </h1>
            <p style= font-size: 18px; margin-top: 10px;">
                Find your space, connect with others, and grow together in commuVerse!
            </p>
        </div>
        """
        
styles = {
    "card": {
        "background-color": "white",
        "border-radius": "15px",
        "padding": "20px",
        "margin": "10px",
        "box-shadow": "0 4px 20px rgba(0, 0, 0, 0.15)",
        "width": "100%",
        "cursor": "pointer",
        "transition": "transform 0.2s, box-shadow 0.2s",
    },
    "card:hover": {
        "transform": "scale(1.03)",
        "box-shadow": "0 6px 25px rgba(0, 0, 0, 0.25)"
    },
    "title": {
        "font-family": "sans-serif",
        "font-size": "1.2em",
        "font-weight": "bold",
        "color": "#2c3e50",
        "margin-bottom": "10px",
        "text-align": "center",
    },
    "icon": {
        "font-size": "2.5em",
        "color": "#3498db",
        "margin-bottom": "10px",
        "text-align": "center",
    },
    "description": {
        "font-family": "Roboto, sans-serif",
        "font-size": "16px",
        "color": "#4a4a4a",
        "line-height": "1.7",
        "margin-bottom": "15px",
        "text-align": "center",
        "min-height": "60px",
    },
    "view-details-btn": {
        "background-color": "#3498db",
        "color": "white",
        "padding": "8px 16px",
        "border-radius": "5px",
        "text-align": "center",
        "cursor": "pointer",
        "transition": "background-color 0.2s",
        "display": "block",
        "width": "100%",
        "border": "none",
        "font-weight": "bold",
    },
    "view-details-btn:hover": {
        "background-color": "#2980b9",
    },
    "container": {
        "display": "grid",
        "grid-template-columns": "repeat(auto-fit, minmax(300px, 1fr))",
        "gap": "20px",
        "padding": "20px",
        "margin-bottom": "30px",
    },
    "output-container": {
        "margin-top": "30px",
        "padding": "20px",
    },
    "selected-card": {
        "border": "2px solid #3498db",
        "background-color": "#f7fbfe",
    }
}
