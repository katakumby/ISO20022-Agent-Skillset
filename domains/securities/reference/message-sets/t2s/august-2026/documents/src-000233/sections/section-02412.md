---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.31 System Identification"]
file_pages: [3203]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.31 System Identification

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3203 to 3203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3203

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus34Choice" on page 3198 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  3198
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3199
Or}     Reason <Rsn> [1..*] ± 3199
Or   Failing <Flng> [1..1]  3199
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3199
Or}     Reason <Rsn> [1..*] ± 3200
Or}   Proprietary <Prtry> [1..1] ± 3200
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
82.1.31 System Identification
82.1.31.1  SystemIdentification2Choice
Definition: Information used to identify a cash clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 3203
Or}   Country <Ctry> [1..1] CodeSet C3 3203
82.1.31.1.1  MarketInfrastructureIdentification <MktInfrstrctrId>
Presence: [1..1]
Definition: Clearing service selected for a transaction.
MarketInfrastructureIdentification <MktInfrstrctrId> contains one of the following elements (see
"MarketInfrastructureIdentification1Choice" on page 3044 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3044
Or}   Proprietary <Prtry> [1..1] Text 3044
82.1.31.1.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which the system is located.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3203 August 2026
```

