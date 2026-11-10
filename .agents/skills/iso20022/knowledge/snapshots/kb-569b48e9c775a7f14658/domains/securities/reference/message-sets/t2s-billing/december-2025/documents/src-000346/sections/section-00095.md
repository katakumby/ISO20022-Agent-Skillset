---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.6 Miscellaneous", "4.1.6.3 OriginalBusinessQuery1", "4.1.6.3.1 MessageIdentification <MsgId>"]
file_pages: [121]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.6.3.1 MessageIdentification <MsgId>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 121 to 121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 121
   MessageNameIdentification <MsgNmId> [0..1] Text 121
   CreationDateTime <CreDtTm> [0..1] DateTime 121
4.1.6.3.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original query message.
Datatype: "Max35Text" on page 153
4.1.6.3.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the query message name identifier to which the message refers.
Datatype: "Max35Text" on page 153
4.1.6.3.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 148
4.1.6.4  MarketInfrastructureIdentification1Choice
Definition: Specifies the market infrastructure identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 121
Or}   Proprietary <Prtry> [1..1] Text 121
4.1.6.4.1  Code <Cd>
Presence: [1..1]
Definition: Infrastructure through which the payment instruction is processed, as published in an
external clearing system identification code list.
Datatype: "ExternalMarketInfrastructure1Code" on page 145
4.1.6.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Clearing system identification in a proprietary form.
.
Datatype: "Max35Text" on page 153
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 121 December 2025
```

