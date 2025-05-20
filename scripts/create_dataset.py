from langsmith import Client

from prompting_workshop.utils import get_root_dir, load_yaml

client = Client()

PATH_TO_EVALUATION_DATASET = get_root_dir() / "data" / "rag" / "evaluation_dataset.yml"

data = load_yaml(PATH_TO_EVALUATION_DATASET)["evaluation_dataset_langsmith"]


if __name__ == "__main__":
    dataset = client.create_dataset(
        dataset_name="TheSpoon Evaluation Dataset", description="Simple evaluation dataset for TheSpoon FAQ"
    )
    client.create_examples(dataset_id=dataset.id, examples=data)
