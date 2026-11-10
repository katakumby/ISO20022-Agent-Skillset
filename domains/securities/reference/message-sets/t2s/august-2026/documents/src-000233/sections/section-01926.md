---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>", "74.4.3.4.10 MovementDetails <MvmntDtls>", "74.4.3.4.10.13 Linkages <Lnkgs>", "74.4.3.4.10.13.3 Reference <Ref>"]
file_pages: [2638]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4.10.13.3 Reference <Ref>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2638 to 2638.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2638

```text
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C22 "ShortLongNumberRule"
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
74.4.3.4.10.13.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Reference <Ref> contains one of the following References34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2638
Or   IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2638
Or   IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2639
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2639
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2639
Or   PoolIdentification <PoolId> [1..1] Text 2639
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 2639
74.4.3.4.10.13.3.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 3328
74.4.3.4.10.13.3.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2638 August 2026
```

