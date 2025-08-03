---
name: AI/ML Model Issue
about: Report issues related to AI/ML models, embeddings, or inference
title: '[ML] '
labels: ['ml', 'needs-investigation']
assignees: ''

---

## Model Issue Description
Describe the issue with the AI/ML model or inference pipeline.

## Model Information
- Model name: [e.g. all-mpnet-base-v2]
- Model version: [e.g. 2.2.2]
- Framework: [e.g. sentence-transformers, transformers]
- Hardware: [e.g. NVIDIA A100, CPU Intel i7]

## Problem Category
- [ ] Model inference errors
- [ ] Embedding quality issues
- [ ] Performance/latency problems
- [ ] Memory/resource issues
- [ ] Model loading failures
- [ ] Vector database integration
- [ ] Test generation quality

## Detailed Description
Provide detailed information about the issue:

### Input Data
```
[Example input that causes the issue]
```

### Expected Output
```
[What you expected to happen]
```

### Actual Output
```
[What actually happened]
```

### Error Messages/Stack Trace
```
[Full error message and stack trace if applicable]
```

## Performance Metrics (if applicable)
- Inference time: [e.g. 500ms]
- Memory usage: [e.g. 4GB]
- Batch size: [e.g. 32]
- Embedding dimension: [e.g. 768]

## Reproduction Steps
1. Load model with: `model = LanguageModel('model-name')`
2. Call method: `embeddings = await model.generate_embeddings('text')`
3. Observe: [describe the issue]

## Environment
- Python version: [e.g. 3.11]
- PyTorch version: [e.g. 2.1.0]
- CUDA version: [e.g. 12.1]
- Available GPU memory: [e.g. 24GB]

## Additional Context
- Is this a regression? [Yes/No]
- Does it work with different models? [Yes/No/Unknown]
- Frequency of occurrence: [Always/Sometimes/Rare]

## Potential Solutions
If you have ideas about what might be causing this or how to fix it, please share.

## Checklist
- [ ] I have checked the model documentation
- [ ] I have verified the input format
- [ ] I have tried with different batch sizes
- [ ] I have provided complete error information