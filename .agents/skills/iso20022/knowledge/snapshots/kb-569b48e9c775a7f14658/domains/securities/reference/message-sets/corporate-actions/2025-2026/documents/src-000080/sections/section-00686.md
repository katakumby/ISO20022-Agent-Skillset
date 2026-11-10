---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.13 Identification Information", "16.1.13.2 CorporateActionEventReference3", "16.1.13.2.2 LinkageType <LkgTp>"]
file_pages: [877]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.13.2.2 LinkageType <LkgTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 877 to 877.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 877

```text
16.1.13.2.2  LinkageType <LkgTp>
Presence: [0..1]
Definition: Specifies when this corporate action event is to be processed relative to a linked corporate
action event.
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
16.1.13.3  DocumentIdentification9
Definition: Identifies a document by a unique identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 877
16.1.13.3.1  Identification <Id>
Presence: [1..1]
Definition: Identifies the document.
Datatype: "Max35Text" on page 1251
16.1.13.4  IdentificationType42Choice
Definition: Choice between a code and a data source scheme to specify the type of alternate
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 877
Or}   Proprietary <Prtry> [1..1] ± 878
16.1.13.4.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification is defined using a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 877 February 2026
```

