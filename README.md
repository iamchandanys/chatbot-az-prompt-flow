Prompt flow is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications, from ideation, prototyping, testing, evaluation to production deployment and monitoring. It makes prompt engineering much easier and enables you to build LLM apps with production quality.

## Prompt Flow VS Code Extension

To enhance your development experience, you can add the Prompt Flow extension to Visual Studio Code. This extension provides a range of features to streamline your workflow, including syntax highlighting, code snippets, and integration with the Prompt Flow CLI.

### Installation

1. Open Visual Studio Code.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
3. Search for "Prompt Flow" by Microsoft.
4. Click the Install button for the Prompt Flow extension.

Once installed, you can start using the extension to improve your prompt engineering and development process.

## Recommended Python Version

For optimal performance and compatibility, it is recommended to use Python 3.9.

# Chatbot AZ Prompt Flow

This project contains two main components: the Car Inspection Claim Agent and the Motor Insurance Claim Agent. Both agents are designed to assist users with their respective claims processes.

## Car Inspection Claim Agent

Car inspections that traditionally involve long wait times, manual paperwork, and back-and-forth coordination. But what if AI could make these seamless? That’s exactly what I’ve built! Buying or renewing car insurance? AI agent ensures the inspection process is quick and hassle-free, leveraging real-time image processing. Snap, submit, done!

## Motor Insurance Claim Agent

Motor insurance claims can be a tedious process, involving multiple stakeholders and manual verification. But what if AI could make it seamless? That’s exactly what I’ve built! Imagine an AI agent that helps users raise a claim in real time, guiding them through the process effortlessly. No more endless calls — just a smooth, automated experience.

## How to Deploy Prompt Flow

To deploy the prompt flow for this project, follow the detailed guide provided by Microsoft. You can find step-by-step instructions on how to deploy a flow at the following link: [How to Deploy a Flow](https://microsoft.github.io/promptflow/how-to-guides/deploy-a-flow/index.html).

## Steps to Deploy to Azure Container Registry

### Build a flow as docker format app:

```sh
pf flow build --source . --output dist --format docker
```

### Build a Docker Image

```sh
docker build dist -t <Image-Name>
```

### Login to ACR

```sh
az login
az acr login --name <ACR-Name>
```

### Tag the local Docker image to ACR

```sh
docker tag <Image-Name>:latest <ACR-Name>.azurecr.io/<Image-Name>:latest
```

### Push the image to ACR

```sh
docker push <ACR-Name>.azurecr.io/<Image-Name>:latest
```

For more information, visit the [Prompt Flow Documentation](https://microsoft.github.io/promptflow/).
