const HtmlWebPackPlugin = require("html-webpack-plugin")

module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.css$/,
                include: /node_modules/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.(png|jpg|gif)$/,
                use: [{
                    loader: 'file-loader',
                    options: {}
                }]
            },
            {
                test: /\.html$/,
                use: [{
                    loader: "html-loader"
                }]
            }
        ]
    },
    entry: "./src/index.js",
    output: {
        filename: "./static/index.js"
    },
    plugins: [
        new HtmlWebPackPlugin({
            template: "./public/index.html",
            filename: "../prod-template/index.html"
        })
    ]
};
