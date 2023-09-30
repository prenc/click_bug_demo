import torch
import click


@click.command()
def test():
    model = torch.nn.Linear(1, 1)
    model = torch.compile(model)
    print(model)
    t = torch.tensor([1], dtype=torch.float32)
    print(model(t))
