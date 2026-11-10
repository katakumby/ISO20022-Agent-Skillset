---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.2 BorrowingReason2Choice", "7.1.28.2.2 Proprietary <Prtry>"]
file_pages: [586]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.2.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 586 to 586.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 586

```text
Definition: Borrowing reason expressed as an ISO 20022 code.
Datatype: "BorrowingReason1Code" on page 616
CodeName Name Definition
SFCT SelfConsumption The borrowing reason is for Self
consumption.
TTTP TransferToThirdParty The borrowing reason is for Transfer to
thrid party.
MMPP MarketMakingPurpose The borrowing reason is for Market
making purpose.
7.1.28.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Borrowing reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.3  PendingProcessing2Choice
Definition: Choice of format for the Pending Processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 586
Or}   Reason <Rsn> [1..*]  587
     Code <Cd> [1..1]  587
{Or       Code <Cd> [1..1] CodeSet 587
Or}       Proprietary <Prtry> [1..1] ± 587
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 588
7.1.28.3.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 636
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 586 February 2025
```

