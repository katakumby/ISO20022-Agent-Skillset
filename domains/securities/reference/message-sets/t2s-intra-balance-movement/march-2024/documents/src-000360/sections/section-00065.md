---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "5.4 Message Building Blocks", "5.4.5 RequestDetails <ReqDtls>", "5.4.5.7 Linkages <Lnkgs>", "5.4.5.7.1 ProcessingPosition <PrcgPos>"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 5.4.5.7.1 ProcessingPosition <PrcgPos>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
5.4.5.7.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C16 "WithLinkageRule"
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition7Choice" on page 412 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 413
Or}   Proprietary <Prtry> [1..1] ± 413
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
5.4.5.7.2  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C14 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 399 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 399
Or   LongNumber <LngNb> [1..1] Text 399
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 399
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
5.4.5.7.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
79 March 2024
```

