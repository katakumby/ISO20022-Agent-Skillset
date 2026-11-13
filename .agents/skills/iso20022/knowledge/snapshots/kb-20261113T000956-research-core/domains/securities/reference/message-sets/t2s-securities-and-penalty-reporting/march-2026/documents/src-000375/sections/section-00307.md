---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.28 HoldIndicator6", "7.1.18.28.1 Indicator <Ind>"]
file_pages: [386]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.28.1 Indicator <Ind>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 386 to 386.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 386

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 386
   Reason <Rsn> [0..*] ± 386
7.1.18.28.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.18.28.2  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the registration status.
Reason <Rsn> contains the following elements (see "RegistrationReason5" on page 372 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  372
{Or     Code <Cd> [1..1] CodeSet 372
Or}     Proprietary <Prtry> [1..1] ± 373
   AdditionalInformation <AddtlInf> [0..1] Text 373
7.1.18.29  DeliveryReturn3Choice
Definition: Choice of format for the delivery return information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 386
Or}   Proprietary <Prtry> [1..1] ± 387
7.1.18.29.1  Code <Cd>
Presence: [1..1]
Definition: Delivery return expressed as an ISO 20022 code.
Datatype: "DeliveryReturn1Code" on page 502
CodeName Name Definition
UNRE UnrecognisedDelivery Original delivery is not recognized.
DQUA WrongQuantity Wrong quantity delivered in the original
instruction.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 386 March 2026
```

