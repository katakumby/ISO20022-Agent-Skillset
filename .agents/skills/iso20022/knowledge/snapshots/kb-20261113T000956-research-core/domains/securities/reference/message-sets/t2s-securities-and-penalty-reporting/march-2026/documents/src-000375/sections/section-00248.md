---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.10 Date Time Period", "7.1.10.2 DateTimePeriod1", "7.1.10.2.2 ToDateTime <ToDtTm>"]
file_pages: [324]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.10.2.2 ToDateTime <ToDtTm>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 324 to 324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 551
7.1.10.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 551
7.1.11 Document
7.1.11.1  DocumentNumber5Choice
Definition: Choice between a short document number, a long document number or a proprietary
document number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 324
Or   LongNumber <LngNb> [1..1] Text 324
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 324
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
7.1.11.1.1  ShortNumber <ShrtNb>
Presence: [1..1]
Definition: Message type number of the document referenced.
Datatype: "Exact3NumericText" on page 555
7.1.11.1.2  LongNumber <LngNb>
Presence: [1..1]
Definition: MX Message identifier of the referenced document.
Datatype: "ISO20022MessageIdentificationText" on page 555
7.1.11.1.3  ProprietaryNumber <PrtryNb>
Presence: [1..1]
Definition: Proprietary document identification.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 324 March 2026
```

