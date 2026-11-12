---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.15 RepairStatus12Choice"]
file_pages: [484]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.15 RepairStatus12Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 484 to 484.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 484

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.28.15  RepairStatus12Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 484
Or}   Reason <Rsn> [1..*]  484
     Code <Cd> [1..1]  485
{Or       Code <Cd> [1..1] CodeSet 485
Or}       Proprietary <Prtry> [1..1] ± 486
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 486
7.1.28.15.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.15.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the repair status.
Reason <Rsn> contains the following RepairReason8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  485
{Or     Code <Cd> [1..1] CodeSet 485
Or}     Proprietary <Prtry> [1..1] ± 486
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 486
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 484 March 2026
```

