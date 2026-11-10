---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.15 CorporateActionOption41Choice", "16.1.15.15.1 Code <Cd>"]
file_pages: [914]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.15.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 914 to 914.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 914

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 914
Or}   Proprietary <Prtry> [1..1] ± 915
16.1.15.15.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
Datatype: "CorporateActionOption17Code" on page 1202
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
CTEN ConsentAndTender Vote to consent to change the terms of
the securities agreement and to tender
securities for cash.
EXER Exercise Exercise intermediate securities or
warrants.
LAPS Lapse Allow event or entitled security to expire.
MKDW MarkDown Mark down the global certificate as a
result of a corporate action (instruction
from International Central Securities
Depositories (ICSDs) to common
depositories who are holding the global
certificate on behalf of the International
Central Securities Depositories (ICSDs)).
MKUP MarkUp Mark up the global certificate as a result
of a corporate action (instruction from
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 914 February 2026
```

