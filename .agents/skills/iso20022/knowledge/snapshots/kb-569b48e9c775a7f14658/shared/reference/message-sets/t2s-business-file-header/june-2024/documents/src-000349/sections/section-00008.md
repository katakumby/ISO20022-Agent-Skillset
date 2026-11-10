---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S BusinessFileHeader"
source_ids: ["src-000349"]
source_editions: ["june-2024"]
message_ids: []
heading_path: ["2 head.002.001.01 BusinessFileHeaderV01", "2.4 Message Building Blocks", "2.4.1 PayloadDescription <PyldDesc>", "2.4.1.3 PayloadType <PyldTp>"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 2.4.1.3 PayloadType <PyldTp>

Source: [src-000349](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`. Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
2.4.1.3  PayloadType <PyldTp>
Presence: [1..1]
Definition: Identification of the type of payload.
Datatype: "Max256Text" on page 10
2.4.1.4  ManifestData <MnfstData>
Presence: [0..*]
Definition: Manifest that describes the related items or attachments.
This block is repeated for each different type of item.
ManifestData <MnfstData> contains the following ManifestData2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DocumentType <DocTp> [1..1] Text 8
   NumberOfDocuments <NbOfDocs> [1..1] Quantity 8
2.4.1.4.1  DocumentType <DocTp>
Presence: [1..1]
Definition: Specifies the type of items contained in the document set. An initial list of values can be
found in the ISO20022 message type catalogue such as admi, camt, pacs, sese, semt etc. ISO
messages.
Datatype: "Max35Text" on page 10
2.4.1.4.2  NumberOfDocuments <NbOfDocs>
Presence: [1..1]
Definition: Gives the number of instances (messages) for each declared type.
Datatype: "Number" on page 9
2.4.2 Payload <Pyld>
Presence: [0..*]
Definition: File Payload is used to include the exchanged documents within the file structure.
Type: (External Schema)
Specifies a data structure that allows to include any valid XML Structure (e.g. through an XML
Schema). The property namespace is set to 'any'.
The processContents value is 'lax' which according to the above specification and to Iso20022:2013
means: If the item has a uniquely determined declaration available, it must be ·valid· with respect to that
definition, that is, ·validate· if you can, don't worry if you can't, i.e. it MAY be validated or not.
Approved by the Cross SEG Harmonisation Group (CSH) on the 18th of June
2024.
head.002.001.01 BusinessFileHeaderV01
Target2-Securities - Business File Header 8 June 2024
```

