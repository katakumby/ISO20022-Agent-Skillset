---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.1 SettlementStatus32Choice", "7.1.28.1.1 Pending <Pdg>", "7.1.28.1.1.2 Reason <Rsn>", "7.1.28.1.1.2.1 Code <Cd>", "7.1.28.1.1.2.1.2 Proprietary <Prtry>"]
file_pages: [463]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.1.1.2.1.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 463 to 463.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 463

```text
CodeName Name Definition
CDLR ConditionalDeliveryAwaitingRelease Instruction is in a hold/frozen/preadvice
mode. Market infrastructure platform is
awaiting release.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
PATD PartialDiffer Disagreement on partial indicator
preventing partial settlement.
PREL PartiallyReleased Transaction has been partially released.
7.1.28.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.28.1.1.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 556
7.1.28.1.2  Failing <Flng>
Presence: [1..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
Failing <Flng> contains one of the following FailingStatus15Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 463
Or}   Reason <Rsn> [1..*]  464
     Code <Cd> [1..1]  464
{Or       Code <Cd> [1..1] CodeSet 464
Or}       Proprietary <Prtry> [1..1] ± 468
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 468
7.1.28.1.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 463 March 2026
```

