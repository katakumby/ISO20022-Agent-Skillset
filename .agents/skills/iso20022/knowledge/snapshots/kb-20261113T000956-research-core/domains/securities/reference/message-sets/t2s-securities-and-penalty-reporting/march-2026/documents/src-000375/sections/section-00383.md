---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.8 AcknowledgementReason12Choice", "7.1.28.8.2 Proprietary <Prtry>"]
file_pages: [475]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.8.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 475 to 475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 475

```text
CodeName Name Definition
RQWV AcceptedWithoutVotingRights Instruction registration is accepted but
the registration is not in full, that is, not
with voting rights.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
7.1.28.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.28.9  GeneratedReason5
Definition: Specifies the reason why the transaction was generated.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 475
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 475
7.1.28.9.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the transaction was generated.
Code <Cd> contains one of the following elements (see "GeneratedReasons5Choice" on page 482 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 482
Or}   Proprietary <Prtry> [1..1] ± 482
7.1.28.9.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 556
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 475 March 2026
```

