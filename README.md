# sourmash_plugin_venn: generate a simple Venn diagram for two sourmash sketches

<b><span style="color:red">This plugin is deprecated.</span></b>

Please use the `venn` command in
[the `betterplot` plugin](https://github.com/sourmash-bio/sourmash_plugin_betterplot/)
instead, as that plugin is maintained and supported as of August 2024.

## Legacy documentation

Generate Venn diagrams showing overlaps between two
[sourmash sketches](https://sourmash.readthedocs.io/) of DNA or
protein sequences:

![simple Venn diagram](doc/simple.png)

## Examples

```
sourmash scripts venn examples/a.sig.gz examples/b.sig.gz -o a-b.png

sourmash scripts venn examples/a.sig.gz examples/b.sig.gz -o a-b.png --name1 A --name2 B

sourmash scripts venn examples/a.sig.gz examples/b.sig.gz examples/c.sig.gz -o a-b-c.png 

sourmash scripts venn examples/a.sig.gz examples/b.sig.gz examples/c.sig.gz -o a-b-c.png --name1 A --name2 B --name3 C
```

## Installation

```
pip install sourmash_plugin_venn
```

## Dev docs

`venn` is developed at https://github.com/sourmash-bio/sourmash_plugin_venn.

### Testing

Run:
```
pytest tests
```

### Generating a release

Bump version number in `pyproject.toml` and push.

Make a new release on github.

Then pull, and:

```
python -m build
```

followed by `twine upload dist/...`.
