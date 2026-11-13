---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.7 Document", "16.1.7.4 DocumentIdentification33", "16.1.7.4.1 Identification <Id>", "16.1.7.4.1.1 AccountServicerDocumentIdentification <AcctSvcrDocId>"]
file_pages: [862]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.7.4.1.1 AccountServicerDocumentIdentification <AcctSvcrDocId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 862 to 862.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 862

```text
Identification <Id> contains one of the following DocumentIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountServicerDocumentIdentification <AcctSvcrDocId> [1..1] Text 862
Or}   AccountOwnerDocumentIdentification <AcctOwnrDocId> [1..1] Text 862
16.1.7.4.1.1  AccountServicerDocumentIdentification <AcctSvcrDocId>
Presence: [1..1]
Definition: Identification of the document assigned by the account servicer.
Datatype: "Max35Text" on page 1251
16.1.7.4.1.2  AccountOwnerDocumentIdentification <AcctOwnrDocId>
Presence: [1..1]
Definition: Identification of the document assigned by the account owner.
Datatype: "Max35Text" on page 1251
16.1.7.4.2  DocumentNumber <DocNb>
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
16.1.8 Financial Institution Identification
16.1.8.1  FinancialInstitutionIdentification18
Definition: Specifies the details to identify a financial institution.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 862 February 2026
```

