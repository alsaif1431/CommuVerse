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
            <p style="color: #4a4a4a; font-size: 18px; margin-top: 10px;">
                Find your space, connect with others, and grow together in commuVerse!
            </p>
        </div>
        """
