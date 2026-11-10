---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.4 ReportOrError <RptOrErr>", "17.4.4.1 Movements <Mvmnts>", "17.4.4.1.5 Movement <Mvmnt>", "17.4.4.1.5.11 MovementDetails <MvmntDtls>", "17.4.4.1.5.11.11 Linkages <Lnkgs>", "17.4.4.1.5.11.11.3 Reference <Ref>"]
file_pages: [418]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.4.1.5.11.11.3 Reference <Ref>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 418 to 418.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 418

```text
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C21 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 2917
Or   LongNumber <LngNb> [1..1] Text 2917
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 2917
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
17.4.4.1.5.11.11.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Reference <Ref> contains one of the following References34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 418
Or   IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 418
Or   IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 419
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 419
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 419
Or   PoolIdentification <PoolId> [1..1] Text 419
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 419
17.4.4.1.5.11.11.3.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 3328
17.4.4.1.5.11.11.3.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 418 August 2026
```

