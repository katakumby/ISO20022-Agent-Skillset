---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.5 InitialPositionAmount <InitlPosAmt>"]
file_pages: [207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.5 InitialPositionAmount <InitlPosAmt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 207 to 207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 207

```text
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
• OtherIdentificationPresenceRule
(Rule)
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
5.4.5.5  InitialPositionAmount <InitlPosAmt>
Presence: [0..1]
Definition: Provides the initial position amount.
InitialPositionAmount <InitlPosAmt> contains the following elements (see AmountAndDirection21 on
page 377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
5.4.5.6  NetPositionAmount <NetPosAmt>
Presence: [1..1]
Definition: Provides the net position amount.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 207
```

