---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.7 Document"]
file_pages: [858]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.7 Document

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 858 to 858.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 858

```text
Definition: Standard code to specify the type of period.
Datatype: "DateType8Code" on page 1206
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.7 Document
16.1.7.1  DocumentIdentification32
Definition: Identification of a document as well as the document number and type of link.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  858
{Or     AccountServicerDocumentIdentification
<AcctSvcrDocId>
[1..1] Text 858
Or}     AccountOwnerDocumentIdentification
<AcctOwnrDocId>
[1..1] Text 858
   DocumentNumber <DocNb> [0..1] ± C6 859
   LinkageType <LkgTp> [0..1] ± C22 859
16.1.7.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned either by the account servicer or the
account owner.
Identification <Id> contains one of the following DocumentIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountServicerDocumentIdentification <AcctSvcrDocId> [1..1] Text 858
Or}   AccountOwnerDocumentIdentification <AcctOwnrDocId> [1..1] Text 858
16.1.7.1.1.1  AccountServicerDocumentIdentification <AcctSvcrDocId>
Presence: [1..1]
Definition: Identification of the document assigned by the account servicer.
Datatype: "Max35Text" on page 1251
16.1.7.1.1.2  AccountOwnerDocumentIdentification <AcctOwnrDocId>
Presence: [1..1]
Definition: Identification of the document assigned by the account owner.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 858 February 2026
```

