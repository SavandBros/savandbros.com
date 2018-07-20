var gulp = require("gulp");
var htmlmin = require("gulp-htmlmin");
var exec = require("child_process").exec;

gulp.task("minify", function() {
  return gulp.src("public/**/*.html")
    .pipe(htmlmin({collapseWhitespace: true}))
    .pipe(gulp.dest("public"));
});

gulp.task("build", function() {
  exec("hugo", function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
  });
  exec("gulp minify", function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
  });
});
gulp.task("serve", function () {
  exec("hugo server -D", function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
  });
});
