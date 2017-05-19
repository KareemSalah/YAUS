const webpack = require('webpack');
const path = require('path');

module.exports = {
  entry: path.join(__dirname, 'client', 'src', 'app-client.js'),
  output: {
    path: path.join(__dirname, 'client', 'src', 'static', 'js'),
    filename: 'bundle.js'
  },
  // module: {
  //   loaders: [{
  //     test: path.join(__dirname, 'src'),
  //     loader: 'babel',
  //     query: {
  //       cacheDirectory: 'babel_cache',
  //       presets: ['react']
  //     }
  //   }]
  // },
      module: {
        loaders: [
            //a regexp that tells webpack use the following loaders on all
            //.js and .jsx files
            {test: /\.jsx?$/,
                //we definitely don't want babel to transpile all the files in
                //node_modules. That would take a long time.
                exclude: /node_modules/,
                //use the babel loader
                loader: 'babel-loader',
                query: {
                    //specify that we will be dealing with React code
                    presets: ['es2015', 'react']
                }
            }
        ]
    },
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV)
    }),
    new webpack.optimize.DedupePlugin(),
    // new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({
      compress: { warnings: false },
      mangle: true,
      sourcemap: false,
      beautify: false,
      dead_code: true
    })
  ]
};