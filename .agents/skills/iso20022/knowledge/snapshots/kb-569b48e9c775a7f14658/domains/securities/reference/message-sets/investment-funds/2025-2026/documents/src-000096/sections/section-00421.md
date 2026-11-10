---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.7.14 SettlementPartiesDetails <SttlmPtiesDtls>"]
file_pages: [577]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.7.14 SettlementPartiesDetails <SttlmPtiesDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 577 to 577.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 577

```text
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 5131 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  5131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5131
     Identification <Id> [0..1] Text 5131
Or   Country <Ctry> [1..1] CodeSet C12 5132
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 5132
Or   TypeAndIdentification <TpAndId> [1..1]  5132
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5132
     Identification <Id> [1..1] IdentifierSet C4 5133
Or}   Proprietary <Prtry> [1..1] ± 5133
26.4.7.14  SettlementPartiesDetails <SttlmPtiesDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of the transaction.
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters26
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeTransactionCondition <TradTxCond> [0..*] ± 577
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 578
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 578
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
578
     Depository <Dpstry> [0..1] ± 580
     Party1 <Pty1> [0..1] ± 581
     Party2 <Pty2> [0..1] ± 581
     Party3 <Pty3> [0..1] ± 581
     Party4 <Pty4> [0..1] ± 582
     Party5 <Pty5> [0..1] ± 582
26.4.7.14.1  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 577 May 2026
```

