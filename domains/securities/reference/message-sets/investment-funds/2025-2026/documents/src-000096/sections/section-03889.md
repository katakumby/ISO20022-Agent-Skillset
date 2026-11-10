---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.10 PendingStatusReason2Choice"]
file_pages: [5180]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.10 PendingStatusReason2Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5180 to 5180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5180

```text
Reason <Rsn> contains the following elements (see "PendingStatusReason14" on page 5174 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 5174
   AdditionalInformation <AddtlInf> [0..1] Text 5174
66.1.45.10  PendingStatusReason2Choice
Definition: Choice of formats for pending reason code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5180
Or}   Proprietary <Prtry> [1..1] ± 5180
66.1.45.10.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the pending account status expressed as a code.
Datatype: "PendingStatusReason1Code" on page 5339
CodeName Name Definition
KYCM KnowYourCustomerDocumentMissing Know Your Customer (KYC) document is
missing.
FRDM FATCAReportingDateMissing FATCA reporting date is missing.
RIGH RightsHolderMissing Rights holder information is missing.
ATHR Authorisation Authorisation is required.
ATHP AuthorisedButPending Authorisation is provided but the account
change is still pending.
MODI ModificationInProcess Modification to the account data is in
process.
66.1.45.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the pending account status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5180 May 2026
```

