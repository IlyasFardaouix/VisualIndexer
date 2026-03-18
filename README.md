# VisualIndexer

**Production-grade multimodal search engine combining CLIP embeddings, OCR extraction, and vector similarity search**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-0EA5E9?style=for-the-badge)

## Demo

<!-- Add demo GIF here -->

The demo showcases end-to-end multimodal retrieval: indexing a folder of images, encoding them with CLIP, extracting text via OCR, and returning top-k results for both text and image queries. It highlights similarity ranking scores and OCR overlays to explain why each match is relevant. The UI demonstrates fast retrieval behavior on medium-to-large image collections and gives a practical view of production usage.

## Problem Statement

Traditional keyword search performs poorly for visual content because many images either have little metadata or noisy filenames that do not represent semantic meaning. This creates a retrieval gap where users know what they are looking for conceptually but cannot retrieve it through exact token matches.

By combining CLIP embeddings with OCR extraction, VisualIndexer solves both semantic and textual discovery paths. CLIP captures visual-language similarity across modalities, while OCR extracts explicit text signals from images; together they produce stronger ranking quality, better recall, and more explainable search results.

## Architecture

```mermaid
flowchart LR
    A[User Input<br/>(image or text query)]
    B[CLIP Encoder<br/>(512-dim vector)]
    C[Vector Store<br/>(ChromaDB / FAISS)]
    D[Similarity Search<br/>(cosine similarity)]
    E[Ranked Results<br/>(score-ordered)]
    F[OCR Text Overlay<br/>on result images]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
```

## Features

- Multimodal input support for both text queries and image queries
- CLIP-based embedding pipeline for robust semantic retrieval
- OCR extraction with Tesseract to enrich visual indexing with text signals
- Vector similarity search with cosine scoring for fast nearest-neighbor retrieval
- Streamlit interface for interactive exploration and result inspection
- Fast batch indexing workflow for practical production datasets
- Scales to large image collections with vector-store-backed retrieval
- Extensible modular pipeline for custom encoders, rerankers, and stores

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Vision-Language Encoder | CLIP | Encode images/text into a shared embedding space |
| OCR Engine | Tesseract OCR | Extract textual cues from image regions |
| Vector Database | ChromaDB | Store and query embeddings with metadata |
| Similarity Engine | FAISS | Efficient nearest-neighbor search at scale |
| Application Layer | Python | Core orchestration and indexing/search logic |
| Model Hub | HuggingFace | Access model weights and tokenizer utilities |
| Numeric Processing | NumPy | Vector ops and similarity preprocessing |
| Image Handling | Pillow | Image loading and preprocessing utilities |
| Frontend | Streamlit | Interactive search UI and diagnostics |

## Installation

```bash
git clone https://github.com/IlyasFardaouix/VisualIndexer.git
cd VisualIndexer
pip install -r requirements.txt
```

Sample `requirements.txt`:

```txt
numpy>=1.24.0
pandas>=2.0.0
torch>=2.0.0
transformers>=4.35.0
sentence-transformers>=2.2.2
opencv-python>=4.8.0
pillow>=10.0.0
pytesseract>=0.3.10
chromadb>=0.5.0
faiss-cpu>=1.7.4
streamlit>=1.30.0
scikit-learn>=1.3.0
```

## Usage

### Example 1 - Indexing images

```python
from visual_indexer import VisualIndexer

indexer = VisualIndexer()
indexer.index_directory("./images")
```

### Example 2 - Querying

```python
results = indexer.search("a red car on a highway", top_k=5)
for r in results:
    print(r.image_path, r.score, r.ocr_text)
```

## Running the Streamlit UI

```bash
streamlit run app.py
```

## Example Results

| Query | Top Match | Score | OCR Text Found |
|---|---|---:|---|
| `a red car on a highway` | `images/highway_red_sedan.jpg` | 0.912 | `A7 Toll - Casablanca` |
| `invoice with VAT number` | `images/docs/invoice_2024_11.png` | 0.884 | `VAT: MA-2049-8891` |
| `conference slide about transformers` | `images/slides/llm_architecture.png` | 0.861 | `Attention Is All You Need` |

## Roadmap

- [x] CLIP-based image indexing
- [x] OCR text extraction
- [x] Streamlit search UI
- [ ] Support for video keyframe indexing
- [ ] REST API with FastAPI

## Contributing

Contributions are welcome and strongly encouraged.
Please open an issue describing your proposal before large changes so architecture decisions stay consistent.
If you are adding a new retriever, encoder, or vector backend, include tests and a reproducible benchmark snippet.

## License

MIT

## Author

Built by **Ilyas Fardaoui** - AI Engineering Intern at MAPMDREF
GitHub: https://github.com/IlyasFardaouix
LinkedIn: https://linkedin.com/in/ilyas-fardaoui-44081224a
