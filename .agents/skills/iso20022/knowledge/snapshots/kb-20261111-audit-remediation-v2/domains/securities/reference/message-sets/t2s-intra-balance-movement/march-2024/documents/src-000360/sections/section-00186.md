---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>", "10.4.4.1.5 Movement <Mvmnt>", "10.4.4.1.5.11 MovementDetails <MvmntDtls>", "10.4.4.1.5.11.11 Linkages <Lnkgs>", "10.4.4.1.5.11.11.3 Reference <Ref>"]
file_pages: [227]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1.5.11.11.3 Reference <Ref>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 227 to 227.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 227

```text
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C21 "ShortLongNumberRule"
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
10.4.4.1.5.11.11.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Reference <Ref> contains one of the following References34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 227
Or   IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 227
Or   IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 228
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 228
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 228
Or   PoolIdentification <PoolId> [1..1] Text 228
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 228
10.4.4.1.5.11.11.3.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 497
10.4.4.1.5.11.11.3.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
227 March 2024
```

