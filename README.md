# ptz-sampler

This is a plugin for sampling images from a ptz camera

## Running the plugin

The plugin is run using docker. To run the plugin, we first need to build the cross-platform docker image and push it
to DockerHub with the following command:

```bash
sudo docker buildx build --platform=linux/amd64,linux/arm64 -f Dockerfile -t $IMAGETAG --push .
```

Then, we can run the plugin on a waggle node using the following command:

```bash
sudo docker run --rm $IMAGETAG $ARGUMENTS
```

As an example, the following command will run the plugin to sample images from a hanwha camera for 20 iterations
with 30 movement per iteration.

```bash
sudo docker run --rm ptz_image_tag -un JohnDoe -pw NotYourPwd -ip camera.let.go -it 20 -mv 30 -cb 0"
```

You need to replace all variables with `$` with the appropriate values. The following table describes the variables:

| Variable     | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `$IMAGETAG`  | The tag for the Docker image you're building and running.                   |
| `$ARGUMENTS`  | see `main.py`.                                            |
