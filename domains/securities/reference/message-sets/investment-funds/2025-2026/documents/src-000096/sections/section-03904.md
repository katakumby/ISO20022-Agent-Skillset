---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.20 PendingOpeningStatusReason1Choice", "66.1.45.20.2 Reason <Rsn>", "66.1.45.20.2.1 Code <Cd>", "66.1.45.20.2.1.2 Proprietary <Prtry>"]
file_pages: [5196]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.20.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5196 to 5196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5196

```text
Definition: Reason for the pending account opening status expressed as a code.
Datatype: "PendingOpeningStatusReason1Code" on page 5337
CodeName Name Definition
ATHR Authorisation Authorisation is required.
ATHP AuthorisedButPending Authorisation is provided but account
opening is still pending.
FRDM FATCAReportingDateMissing FATCA reporting date is missing.
KYCM KnowYourCustomerDocumentMissing Know Your Customer (KYC) document is
missing.
NOTO NotOpened Account is not yet open, even for partial
use.
REST Restrictions Account will be opened when restrictions
are addressed.
RIGH RightsHolderMissing Rights holder information is missing.
66.1.45.20.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the pending account opening status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.20.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the pending account opening status.
Datatype: "Max350Text" on page 5403
66.1.45.21  TransferUnmatchedStatus4Choice
Definition: Reason for the unmatched status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5197
Or   Reason <Rsn> [1..1] CodeSet 5197
Or   ExtendedReason <XtndedRsn> [1..1] Text 5197
Or}   DataSourceScheme <DataSrcSchme> [1..1] ± 5198
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5196 May 2026
```

