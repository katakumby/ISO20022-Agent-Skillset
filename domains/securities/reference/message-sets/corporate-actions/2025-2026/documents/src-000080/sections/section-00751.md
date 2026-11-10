---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.37 CorporateActionOption33Choice"]
file_pages: [944]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.37 CorporateActionOption33Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 944 to 944.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 944

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.37  CorporateActionOption33Choice
Definition: Choice between a standard code or a proprietary code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 944
Or}   Proprietary <Prtry> [1..1] ± 945
16.1.15.37.1  Code <Cd>
Presence: [1..1]
Definition: Option type expressed as a code.
Datatype: "CorporateActionOption12Code" on page 1197
CodeName Name Definition
ABST Abstain Vote expressed as abstain. In this case,
the issuing company will add the number
of shares to the quorum of the meeting.
If the voting right is not executed, it will
not be added to the quorum. In this case,
code NOAC should be used.
BSPL BonusSharePlan Receive equities from the share
premium reserve of the company and
considered as a capital distribution
rather than a disbursement of income
with different tax implications (typically
found in Australia).
BUYA BuyUp Buy additional securities to round up
position.
CASE CashAndSecurity Option to choose between different
security and cash options.
CASH Cash Option to choose cash.
CEXC ConsentAndExchange Vote to consent to change the terms of
the securities agreement and to
exchange securities.
CONN ConsentDenied Vote not to approve the event or
proposal.
CONY ConsentGranted Vote to approve the event or proposal.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 944 February 2026
```

