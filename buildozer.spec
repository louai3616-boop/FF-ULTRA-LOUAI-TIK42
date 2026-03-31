name: Build LOUAI APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build with Buildozer
        uses: ArtemSerebrennkov/buildozer-action@v1
        with:
          buildozer_version: master
          python_version: 3.10
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: FF_ULTRA_LOUAI_APK
          path: bin/*.apk
