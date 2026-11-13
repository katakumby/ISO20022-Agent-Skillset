---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.7 Document", "16.1.7.3 DocumentIdentification31", "16.1.7.3.1 Identification <Id>"]
file_pages: [861]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.7.3.1 Identification <Id>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 861 to 861.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 861

```text
16.1.7.3.1  Identification <Id>
Presence: [1..1]
Definition: Identifies the document.
Datatype: "Max35Text" on page 1251
16.1.7.3.2  LinkageType <LkgTp>
Presence: [0..1]
Definition: Specifies when this document is to be processed relative to another referred document.
Impacted by: C22 "WithLinkageRule"
LinkageType <LkgTp> contains one of the following elements (see "ProcessingPosition7Choice" on
page 969 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 969
Or}   Proprietary <Prtry> [1..1] ± 970
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
16.1.7.4  DocumentIdentification33
Definition: Identification of a document as well as the document number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  861
{Or     AccountServicerDocumentIdentification
<AcctSvcrDocId>
[1..1] Text 862
Or}     AccountOwnerDocumentIdentification
<AcctOwnrDocId>
[1..1] Text 862
   DocumentNumber <DocNb> [0..1] ± C6 862
16.1.7.4.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the document (message) assigned either by the account servicer or the
account owner.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 861 February 2026
```

