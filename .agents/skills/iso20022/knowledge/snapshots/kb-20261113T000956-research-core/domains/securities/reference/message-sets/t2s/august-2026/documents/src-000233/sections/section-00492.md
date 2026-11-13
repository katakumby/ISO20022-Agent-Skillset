---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["26 head.002.001.01 BusinessFileHeaderV01", "26.4 Message Building Blocks", "26.4.1 PayloadDescription <PyldDesc>", "26.4.1.3 PayloadType <PyldTp>"]
file_pages: [618]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 26.4.1.3 PayloadType <PyldTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 618 to 618.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 618

```text
26.4.1.3  PayloadType <PyldTp>
Presence: [1..1]
Definition: Identification of the type of payload.
Datatype: "Max256Text" on page 3327
26.4.1.4  ManifestData <MnfstData>
Presence: [0..*]
Definition: Manifest that describes the related items or attachments.
This block is repeated for each different type of item.
ManifestData <MnfstData> contains the following ManifestData2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DocumentType <DocTp> [1..1] Text 618
   NumberOfDocuments <NbOfDocs> [1..1] Quantity 618
26.4.1.4.1  DocumentType <DocTp>
Presence: [1..1]
Definition: Specifies the type of items contained in the document set. An initial list of values can be
found in the ISO20022 message type catalogue such as admi, camt, pacs, sese, semt etc. ISO
messages.
Datatype: "Max35Text" on page 3328
26.4.1.4.2  NumberOfDocuments <NbOfDocs>
Presence: [1..1]
Definition: Gives the number of instances (messages) for each declared type.
Datatype: "Number" on page 3324
26.4.2 Payload <Pyld>
Presence: [0..*]
Definition: File Payload is used to include the exchanged documents within the file structure.
Type: (External Schema)
Specifies a data structure that allows to include any valid XML Structure (e.g. through an XML
Schema). The property namespace is set to 'any'.
The processContents value is 'lax' which according to the above specification and to Iso20022:2013
means: If the item has a uniquely determined declaration available, it must be ·valid· with respect to that
definition, that is, ·validate· if you can, don't worry if you can't, i.e. it MAY be validated or not.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
head.002.001.01 BusinessFileHeaderV01
Target2-Securities 618 August 2026
```

