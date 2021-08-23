
Torch's python package is quite large, so we have to increase docker's allowed memory usage (Docker: Preferences -> Resources -> Memory) to 4GB.

```
docker build -t force_control .
```

This initial build can take some time, because some large dependencies are installed.

```
docker run -v $PWD/force_control.py:/main.py force_control
```

[How to use GUI on Mac](https://fredrikaverpil.github.io/2016/07/31/docker-for-mac-and-gui-applications/)