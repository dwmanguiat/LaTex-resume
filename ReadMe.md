![Resume](resume.png)

## About

This repository stores my LaTeX-authored resume. On every push to `master`, a GitHub Actions workflow automatically compiles the `.tex` source into a PDF and renders it as a PNG — keeping the rendered outputs always in sync with the source.

## Workflow

```mermaid
flowchart TD
    A([Edit resume.tex]) -->|git push to master| B

    subgraph B[GitHub Actions]
        direction TB
        B1[Install TeX Live + poppler-utils]
        B2[pdflatex resume.tex → resume.pdf]
        B3[pdftoppm resume.pdf → resume.png]
        B4[Commit & push rendered files]
        B1 --> B2 --> B3 --> B4
    end

    B -->|bot commit with skip ci| C([resume.pdf + resume.png on master])
```
