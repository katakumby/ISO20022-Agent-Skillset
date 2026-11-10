---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.7 Document", "16.1.7.1 DocumentIdentification32", "16.1.7.1.2 DocumentNumber <DocNb>"]
file_pages: [859]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.7.1.2 DocumentNumber <DocNb>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 859 to 859.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 859

```text
Datatype: "Max35Text" on page 1251
16.1.7.1.2  DocumentNumber <DocNb>
Presence: [0..1]
Definition: Identification of the type of document.
Impacted by: C6 "ShortLongNumberRule"
DocumentNumber <DocNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 859 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 860
Or   LongNumber <LngNb> [1..1] Text 860
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 860
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
16.1.7.1.3  LinkageType <LkgTp>
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
16.1.7.2  DocumentNumber5Choice
Definition: Choice between a short document number, a long document number or a proprietary
document number.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 859 February 2026
```

