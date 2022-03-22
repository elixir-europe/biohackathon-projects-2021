To generate the BioHackrXiv PDF with a local copy of the Docker image, run the command
```shell
docker run --rm -it -v $(pwd):/work -w /work biohackrxiv/gen-pdf:local gen-pdf /work BH21EU
```