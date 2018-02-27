'use strict';

var gulp = require('gulp');

gulp.task('scripts', function(){
  console.log('... collecting java-scripts');

  return gulp.src([
    './node_modules/bootstrap/dist/js/bootstrap.min.js',
    './node_modules/popper.js/dist/popper.min.js',
    './node_modules/jquery/dist/jquery.slim.min.js'
    ])
    .pipe(gulp.dest('./build'));
});

gulp.task('bootstrap', function () {
    var sass         = require('gulp-sass');
    var postcss      = require('gulp-postcss');
    var sourcemaps   = require('gulp-sourcemaps');
    var autoprefixer = require('autoprefixer');
    var cssnano      = require('cssnano');

    console.log('+++ Building Bootstrap4 (John Joesson)');

    return gulp.src('./src/bootstrap-custom.scss')
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(postcss([
          autoprefixer({ browsers: ['last 2 versions'] }),
          cssnano()
          ]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./build'));
});

gulp.task('default', ['bootstrap', 'scripts']);