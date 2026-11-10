---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.11 DisabledStatusReason1Choice", "66.1.45.11.2 Reason <Rsn>", "66.1.45.11.2.1 Code <Cd>", "66.1.45.11.2.1.1 Code <Cd>"]
file_pages: [5182]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.11.2.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5182 to 5182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5182

```text
66.1.45.11.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the disabled account status expressed as a code.
Datatype: "DisabledReason2Code" on page 5294
CodeName Name Definition
CLOS AccountClosingInProcess Account closing is in process.
BKRP Bankruptcy Bankruptcy.
CMMT Commitment Commitment.
CNFS Confiscation Confiscation.
MORT MortisCausa Reserved in contemplation of death.
PCOM PendingComplianceVerification Pending compliance verification.
PLDG Pledged Pledged.
TRPE Reregistration Reregistration.
SANC Sanctions Sanctions are in place.
TRAN Transfer Transfer.
REJT Rejected Account was pending opening but is now
rejected.
66.1.45.11.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the disabled account status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.11.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the disabled account status.
Datatype: "Max350Text" on page 5403
66.1.45.12  SuspendedStatusReason4Choice
Definition: Reason for a suspended status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5182 May 2026
```

