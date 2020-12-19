"use strict";

const csso = require("gulp-csso");
const del = require("del");
const gulp = require("gulp");
const htmlmin = require("gulp-htmlmin");
const sass = require("gulp-sass");
const connect = require("gulp-connect");
const i18n = require("gulp-html-i18n");

const I18N_CONFIG = {
  langDir: "i18n",
  createLangDirs: true,
  renderEngine: "mustache",
  defaultLang: "en",
  delimiters: ["{{", "}}"],
  fallback: "en",
  filenameI18n: true,
};

// CLEAN

gulp.task("clean", () => {
  return del(["dist", "serve"]);
});

// BUILD

gulp.task("build:style", () => {
  return gulp.src("src/asset/**/*.scss")
    // Compile SASS files
    .pipe(sass({
      outputStyle: "nested",
      precision: 10,
      includePaths: ["."],
      onError: console.error.bind(console, "Sass error:"),
    }))
    // Minify the file
    .pipe(csso())
    // Output
    .pipe(gulp.dest("dist/asset"));
});

gulp.task("build:html", () => {
  return gulp.src(["src/**/*.html"])
    .pipe(htmlmin({
      collapseWhitespace: true,
      removeComments: true,
    }))
    .pipe(gulp.dest("dist"));
});

gulp.task("build:asset", () => {
  return gulp.src("src/asset/*/**/*")
    .pipe(gulp.dest("dist/asset/"));
});

gulp.task("build:localize", function () {
  return gulp.src("dist/index.html")
    .pipe(i18n(I18N_CONFIG))
    .pipe(gulp.dest("dist"));
});

gulp.task("build", gulp.series(
  "clean",
  "build:style",
  "build:html",
  "build:asset",
  "build:localize",
));

// SERVE

gulp.task("serve:html", () => {
  return gulp.src(["src/**/*.html"])
    .pipe(gulp.dest("serve"));
});

gulp.task("serve:style", () => {
  return gulp.src("src/asset/*.scss")
    .pipe(sass({
      outputStyle: "nested",
      precision: 10,
      includePaths: ["."],
      onError: console.error.bind(console, "Sass error:"),
    }))
    .pipe(gulp.dest("serve/asset/"));
});

gulp.task("serve:asset", () => {
  return gulp.src(["src/asset/*/**/*", "src/asset/*.js"])
    .pipe(gulp.dest("serve/asset/"));
});

gulp.task("serve:localize", function () {
  return gulp.src("serve/index.html")
    .pipe(i18n(I18N_CONFIG))
    .pipe(gulp.dest("serve"));
});

gulp.task("serve:reload", () => {
  return gulp.src("serve").pipe(connect.reload());
});

gulp.task("serve:watch", async () => {
  return gulp.watch("src/**/*", gulp.series(
    "clean",
    "serve:html",
    "serve:asset",
    "serve:style",
    "serve:localize",
    "serve:reload",
  ));
});

gulp.task("serve:connect", async () => {
  connect.server({
    port: 4000,
    root: "serve",
    livereload: true,
  });
});

gulp.task("serve", gulp.series(
  "clean",
  "serve:html",
  "serve:asset",
  "serve:style",
  "serve:localize",
  "serve:reload",
  "serve:connect",
  "serve:watch",
));

// DEFAULT

gulp.task("default", async () => {
  console.log("Check scripts in package.json to see development commands.");
});
