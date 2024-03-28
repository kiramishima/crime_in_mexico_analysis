# Mage + Pipelines

<div>
<img src="https://github.com/mage-ai/assets/blob/main/mascots/mascots-shorter.jpeg?raw=true">
</div>

Mage is an open-source, hybrid framework for transforming and integrating data. ✨

## Let's get started

This repo contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/). 


Rename `dev.env` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it _will_ contain credentials in the future.

Now, let's build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up -d
```

Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to start with mage. 

### What just happened?

We just initialized a new mage repository. It will be present in your project under the name `victims_cdmx`. If you changed the varable `PROJECT_NAME` in the `.env` file, it will be named whatever you set it to. Also, you need create `personal-gcp.json` file with your credentials, in case, you load the data to GCS.

This repository should have the following structure:

```
.
├── mage_data
│   └── victims_cdmx
├── victims_cdmx
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
│   ├── data_loaders
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── dev.env
├── docker-compose.yml
└── requirements.txt
```

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): a good place to understand Mage functionality or concepts.
2. [Mage Slack](https://www.mage.ai/chat): a good place to ask questions or get help from the Mage team.
3. [DTC Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_workflow_orchestration): a good place to get help from the community on course-specific inquireies.
4. [Mage GitHub](https://github.com/mage-ai/mage-ai): a good place to open issues or feature requests.
