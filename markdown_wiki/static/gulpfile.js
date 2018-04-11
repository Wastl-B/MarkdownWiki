'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('autoprefixer');
var cssnano = require('cssnano');
var rename = require('gulp-rename');

gulp.task('scripts', () =>
	gulp
		.src([
			'./node_modules/bootstrap/dist/js/bootstrap.min.js',
			'./node_modules/popper.js/dist/popper.min.js',
			'./node_modules/jquery/dist/jquery.slim.min.js',
		])
		.pipe(gulp.dest('./build'))
);

gulp.task('sass', () =>
	gulp
		.src('./src/bootstrap-custom.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(gulp.dest('./build'))
);

gulp.task('minify-sass', ['sass'], () =>
	gulp
		.src('./build/*.css')
		.pipe(
			rename({
				suffix: '.min',
			})
		)
		.pipe(sourcemaps.init())
		.pipe(postcss([autoprefixer({ browsers: ['last 2 version'] }), cssnano()]))
		.pipe(sourcemaps.write('.'))
		.pipe(gulp.dest('./build'))
);

gulp.task('watch', ['sass'], () => gulp.watch(['./src/*.scss'], ['sass']));

gulp.task('default', ['sass', 'scripts']);
