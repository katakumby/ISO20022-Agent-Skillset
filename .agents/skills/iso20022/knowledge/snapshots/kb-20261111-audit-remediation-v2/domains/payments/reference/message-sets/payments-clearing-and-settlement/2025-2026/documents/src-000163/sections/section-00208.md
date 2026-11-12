---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.1 ReturnIdentification <RtrId>"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.1 ReturnIdentification <RtrId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
ReturnedInterbankSettlementAmount/attribute::Currency
Following Must be True
    /ExchangeRate Must be present
• ReturnedInstructedAmountAndExchangeRate2Rule
If ReturnedInstructedAmount is present and the currency is the same as the currency in
ReturnedInterbankSettlementAmount, then ExchangeRate is not allowed.
On Condition
    /ReturnedInstructedAmount is present
 And    /ReturnedInstructedAmount/attribute::Currency is equal to /
ReturnedInterbankSettlementAmount/attribute::Currency
Following Must be True
    /ExchangeRate Must be absent
4.4.3.1  ReturnIdentification <RtrId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the returned transaction.
Usage: The instructing party is the party sending the return message and not the party that sent the
original instruction that is being returned.
Datatype: "Max35Text" on page 1246
4.4.3.2  OriginalGroupInformation <OrgnlGrpInf>
Presence: [0..1]
Definition: Provides information on the original message.
OriginalGroupInformation <OrgnlGrpInf> contains the following OriginalGroupInformation33
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 309
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 309
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 310
4.4.3.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Point to point reference assigned by the original instructing party to unambiguously identify
the original message.
Datatype: "Max35Text" on page 1246
4.4.3.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
309 March 2026
```

