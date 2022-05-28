[app]

title = KVSearch

package.name = KVSearch
package.domain = io.github.tj20201.kvsearch

source.dir = .
source.include_exts = py,png,kv
source.exclude_exts = spec
source.exclude_dirs = tests, bin

version = 1.0.0
requirements = python3,kivy,webbrowser
orientation = all
fullscreen = 0

android.permissions = INTERNET
android.api = 24
android.minapi = 24
android.sdk = 24

[buildozer]

log_level = 1
